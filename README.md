# NeoShell

![Status](https://img.shields.io/badge/status-In%20Development-yellow)
![License](https://img.shields.io/github/license/MrSpecks/NeoShell)

**Author:** MrSpecks  
**License:** MIT  
**Status:** In Development  
**Disclaimer:** For educational and authorized testing purposes only.

## Table of Contents

- [Overview](#overview)
- [Contributing](#contributing)
- [Key Features](#key-features)
- [Use Case](#use-case)
- [How It Works](#how-it-works)
- [Installation](#installation)

---

## Overview

This tool is a high-performance, intelligent **CMS Reconnaissance & Webshell Payload Generator** designed for authorized penetration testing engagements. It detects the backend technologies used by a wide range of websites—including PHP, JSP, Java EE, React, Vue, WordPress, and custom stacks—and generates tailored webshell payloads based on CMS and stack fingerprinting.

Built with concurrency in mind, this tool is meant for offensive security professionals and red teamers who need **automated payload generation** at scale, with **conditional deployment logic** based on target characteristics and real-time detection signals.

---

## Contributing

We welcome pull requests and suggestions! If you’d like to help us build NeoShell into an even more powerful tool, feel free to:

- Fork this repo
- Create a branch
- Make your changes
- Submit a pull request

Let’s build something legendary together.

---

## Key Features

- **CMS & Stack Detection**
  - Fingerprints CMS and frameworks (WordPress, JSP, React, etc.)
  - Passive detection via headers, DOM clues, and paths
- **Custom Payload Matching**
  - Loads dynamic payloads based on tech stack
  - Saves webshells locally for manual or automated drop
- **Concurrency & Scaling**
  - Async or thread-based architecture for mass site scanning
- **Conditional Logic**
  - Only drops payload if target meets detection criteria
- **Extensibility**
  - Modular payload system (JSON/YAML)
  - Easy to integrate new CMS or tech stacks
- **Logging & Reporting**
  - Saves recon and payload activity to timestamped files

---

## Use Case

This tool is ideal for:

- Penetration testers working under legal contracts
- Offensive security engineers building recon automation
- Bug bounty hunters needing rapid CMS identification
- Red team toolchains requiring webshell generation logic

---

## How It Works

1. You feed it a list of target domains or subdomains.
2. It fingerprints each target for CMS/stack using multiple methods.
3. Based on the result, it matches and prepares a fitting webshell payload.
4. Payloads are saved locally and can be optionally deployed in post-exploitation.

---

## Installation

```bash
git clone https://github.com/kaegee/universal-webshell-tool.git
cd universal-webshell-tool
pip install -r requirements.txt
