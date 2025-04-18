import requests
from tqdm import tqdm
from core.stack_fingerprint import detect_stack
import json
import os
from datetime import datetime

# Color codes for terminal output
class Colors:
    OK = '\033[92m'
    ERROR = '\033[91m'
    INFO = '\033[94m'
    RESET = '\033[0m'

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

    for url in tqdm(targets, desc="Scanning Targets"):
        result = scan_target(url)
        results.append(result)

    print("\n" + Colors.INFO + "Scan Summary:" + Colors.RESET)
    log_lines = []

    for res in results:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if "error" in res:
            msg = f"[ERROR] {res['url']:<40} - {res['error']}"
            print(f"{Colors.ERROR}{msg}{Colors.RESET}")
        else:
            detected_stack = ', '.join(res['stack']) if res['stack'] else "Unknown"
            msg = f"[OK]    {res['url']:<40} - Stack: {detected_stack}"
            print(f"{Colors.OK}{msg}{Colors.RESET}")
        log_lines.append(f"[{timestamp}] {msg}")

    # Write raw logs
    os.makedirs("logs", exist_ok=True)
    with open("logs/scan.log", "w") as log_file:
        for line in log_lines:
            log_file.write(line + "\n")

    # Write JSON report
    with open("logs/scan_report.json", "w") as json_file:
        json.dump(results, json_file, indent=4)

    print(f"\n{Colors.INFO}Scan reports saved to logs/scan.log and logs/scan_report.json{Colors.RESET}")

if __name__ == "__main__":
    main()