import requests
from tqdm import tqdm
from core.stack_fingerprint import detect_stack
from collections import defaultdict
import logging
import os

# Setup logging
os.makedirs("results", exist_ok=True)
logging.basicConfig(
    filename='results/scan.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def load_targets(file_path="targets.txt"):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def scan_target(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        body = response.text
        stack = detect_stack(headers, body)
        return {"url": url, "stack": stack}
    except Exception as e:
        return {"url": url, "error": str(e)}

def main():
    targets = load_targets()
    results = []

    # Summary tracking
    total_targets = 0
    successful_scans = 0
    failed_scans = 0
    stack_counter = defaultdict(int)

    print("[*] Starting scan...\n")

    for url in tqdm(targets, desc="Scanning Targets"):
        total_targets += 1
        result = scan_target(url)
        results.append(result)

        if "error" in result:
            failed_scans += 1
            stack_counter["Error"] += 1
            logging.error(f"{result['url']} - ERROR: {result['error']}")
        else:
            successful_scans += 1
            for stack in result["stack"]:
                stack_counter[stack] += 1
            logging.info(f"{result['url']} - Stack: {', '.join(result['stack'])}")

    print("\nScan Results:")
    for res in results:
        if "error" in res:
            print(f"[ERROR] {res['url']} - {res['error']}")
        else:
            print(f"[OK] {res['url']} - Stack: {', '.join(res['stack'])}")

    # Summary output
    summary_text = "\n=== SCAN SUMMARY ===\n"
    summary_text += f"Total Targets Scanned: {total_targets}\n"
    summary_text += f"Successful Scans: {successful_scans}\n"
    summary_text += f"Failed Scans: {failed_scans}\n"
    summary_text += "\nDetected Stacks:\n"
    for stack, count in stack_counter.items():
        summary_text += f" - {stack}: {count} site(s)\n"

    print(summary_text)

    # Save summary
    with open('results/summary.txt', 'w') as f:
        f.write(summary_text)

    logging.info("Scan complete.")
    logging.info(summary_text)

if __name__ == "__main__":
    main()