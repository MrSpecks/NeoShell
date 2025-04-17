import aiohttp
import asyncio
import json
import os
from tqdm import tqdm
from core.utils import detect_tech_stack

# Load targets from file
def load_targets(file_path):
    # Validate file_path is a string
    if not isinstance(file_path, str):
        raise ValueError("The file_path must be a string.")

    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        raise

# Smart fetch function with fallback and realistic headers
async def fetch(session, url, retries=2):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    urls_to_try = []
    if not url.startswith("http"):
        urls_to_try = [f"https://{url}", f"http://{url}"]
    elif url.startswith("https://"):
        urls_to_try = [url, url.replace("https://", "http://")]
    elif url.startswith("http://"):
        urls_to_try = [url, url.replace("http://", "https://")]

    for attempt in urls_to_try:
        for _ in range(retries + 1):
            try:
                async with session.get(attempt, timeout=10, ssl=False) as response:
                    html = await response.text()
                    return {
                        "url": attempt,
                        "status": response.status,
                        "html": html,
                        "headers": dict(response.headers)
                    }
            except Exception as e:
                last_error = str(e)
    return {
        "url": url,
        "status": "error",
        "error": last_error,
        "html": "",
        "headers": {}
    }

# Scan each target and detect stack
async def scan_target(session, url):
    result = await fetch(session, url)
    if result["status"] != "error":
        result["tech_stack"] = detect_tech_stack(result["headers"])
        result.pop("html", None)  # Strip heavy data
    else:
        result["tech_stack"] = ["Unknown"]
    return result

# Main async runner
async def run_recon(targets_file="targets.txt", output_path="results/recon.json"):
    targets = load_targets(targets_file)

    if not os.path.exists("results"):
        os.makedirs("results")

    results = []

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
    }

    connector = aiohttp.TCPConnector(limit_per_host=10)
    timeout = aiohttp.ClientTimeout(total=15)

    async with aiohttp.ClientSession(headers=headers, connector=connector, timeout=timeout) as session:
        tasks = [scan_target(session, target) for target in targets]
        for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Recon Scanning"):
            result = await f
            results.append(result)

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    # Auto open in VS Code preview
    os.system(f"code {output_path}")

