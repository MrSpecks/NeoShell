import aiohttp
import asyncio
from tqdm import tqdm
from core.stack_fingerprint import detect_stack
import json
import os
import csv
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

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            body = await response.text()
            headers = dict(response.headers)
            stack = detect_stack(headers, body)
            return {"url": url, "stack": stack}
    except Exception as e:
        return {"url": url, "error": str(e)}

async def scan_targets_async(targets):
    results = []
    connector = aiohttp.TCPConnector(limit=100)  # Increase for higher concurrency
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch(session, url) for url in targets]
        for future in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Scanning Targets"):
            result = await future
            results.append(result)
    return results

def save_reports(results):
    log_lines = []
    successful_scans = []

    print("\n" + Colors.INFO + "Scan Summary:" + Colors.RESET)
    for res in results:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if "error" in res:
            msg = f"[ERROR] {res['url']:<40} - {res['error']}"
            print(f"{Colors.ERROR}{msg}{Colors.RESET}")
        else:
            detected_stack = ', '.join(res['stack']) if res['stack'] else "Unknown"
            msg = f"[OK]    {res['url']:<40} - Stack: {detected_stack}"
            print(f"{Colors.OK}{msg}{Colors.RESET}")
            successful_scans.append({"url": res["url"], "stack": detected_stack})
        log_lines.append(f"[{timestamp}] {msg}")

    os.makedirs("logs", exist_ok=True)

    # Write raw logs
    with open("logs/scan.log", "w") as log_file:
        for line in log_lines:
            log_file.write(line + "\n")

    # Write JSON report
    with open("logs/scan_report.json", "w") as json_file:
        json.dump(results, json_file, indent=4)

    # Write CSV report
    with open("logs/scan_results.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["url", "stack"])
        writer.writeheader()
        for row in successful_scans:
            writer.writerow(row)

    print(f"\n{Colors.INFO}Scan reports saved to logs/scan.log, scan_report.json, and scan_results.csv{Colors.RESET}")

def main():
    targets = load_targets()
    results = asyncio.run(scan_targets_async(targets))
    save_reports(results)

if __name__ == "__main__":
    main()