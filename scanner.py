import requests
from tqdm import tqdm
from core.stack_fingerprint import detect_stack

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

    print("\nScan Results:")
    for res in results:
        if "error" in res:
            print(f"[ERROR] {res['url']} - {res['error']}")
        else:
            print(f"[OK] {res['url']} - Stack: {', '.join(res['stack'])}")

if __name__ == "__main__":
    main()