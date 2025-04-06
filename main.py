import asyncio
import os
from core.recon import run_recon

TARGET_FILE = "data/targets.txt"

def load_targets(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    targets = load_targets(TARGET_FILE)
    asyncio.run(run_recon("targets.txt"))