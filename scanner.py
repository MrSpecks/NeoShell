import requests
from tqdm import tqdm
from core.stack_fingerprint import detect_stack
from datetime import datetime

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

def log_results(content, log_file="scan.log"):
    with open(log_file, "a") as log:
        log.write(content + "\n")

def main():
    targets = load_targets()
    results = []

    print(f"\nStarted scan at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for url in tqdm(targets, desc="Scanning Targets"):
        result = scan_target(url)
        results.append(result)

    # Categorize results
    success = [r for r in results if "stack" in r and r["stack"]]
    unknown = [r for r in results if "stack" in r and not r["stack"]]
    errors = [r for r in results if "error" in r]

    # Display scan results
    print("\nScan Results:")
    for res in results:
        if "error" in res:
            print(f"[ERROR] {res['url']} - {res['error']}")
        elif res["stack"]:
            print(f"[KNOWN] {res['url']} => {', '.join(res['stack'])}")
        else:
            print(f"[UNKNOWN] {res['url']}")

    # Build summary with tagging
    summary = "\n--- Scan Summary ---\n"
    summary += f"Total Targets: {len(results)}\n"
    summary += f"Successful Detections: {len(success)}\n"
    summary += f"Unknown Stacks: {len(unknown)}\n"
    summary += f"Errors: {len(errors)}\n"

    summary += "\n[+] Successful Detections:\n"
    for s in success:
        summary += f"[KNOWN] {s['url']} => {', '.join(s['stack'])}\n"

    summary += "\n[~] Unknown Stack:\n"
    for u in unknown:
        summary += f"[UNKNOWN] {u['url']}\n"

    summary += "\n[!] Errors:\n"
    for e in errors:
        summary += f"[ERROR] {e['url']} - {e['error']}\n"

    print(summary)
    log_results(summary)

if __name__ == "__main__":
    main()