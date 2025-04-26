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
git clone git clone https://github.com/MrSpecks/NeoShell.git
   cd NeoShell
```

### **1.Install Dependencies**
```bash
pip install -r requirements.txt
```
Note: If pip fails, try python3 -m pip install -r requirements.txt.

### **2.Verify the installation**
```bash
python neoshell.py --help
```
---

## Usage**

### **Running a Scan**

Start a recon scan by providing a list of target URLs and a scan profile:
```bash 
python neoshell.py --targets targets.txt --profile aggressive
```

Profiles: Aggressive maximizes speed; passive prioritizes stealth.

## **Available Commands**
--targets <file>: Input file with target URLs (e.g., targets.txt).
--profile <profile>: Scan profile (aggressive, passive, etc.).
--output <directory>: Output directory for reports.
--help: Display help and options.

### **Example Output**
```bash
$ python neoshell.py --help
NeoShell v1.0 - CMS Recon & Webshell Payload Generator
Usage: neoshell.py [options]
...
```

## **Configuration**
### **Payload Settings**
Configure NeoShell to deploy specific payloads based on CMS type, version, or detected plugins in config.json. The default_payload is used when no specific match is found.
```json
{
  "payloads": {
    "wordpress": ["wp-shell.php", "wp-reverse-shell.php"],
    "joomla": ["joomla-shell.php"]
  },
  "default_payload": "wp-shell.php",
  "log_config": {
    "path": "logs/",
    "format": "timestamped"
  }
}
```
Note: Validate changes with a JSON linter to avoid errors.

### **Logging**
Logs are generated in the logs/ directory by default. Modify log_config in config.json to change the path or format.

## **Development & Contributions**
We welcome contributions to make NeoShell better! 
Follow these steps:
1. Fork the repository on GitHub.
2. Create a new branch:
```bash
git checkout -b feature-name
```
3. Commit your changes:
```bash
git commit -m "Add feature X"
```
4. Push to your fork:
```bash
git push origin feature-name
```
5. Submit a pull request to merge into the main repository.

---

## FAQ

**Q: Can I use NeoShell for unauthorized pentesting?**  
A: No, NeoShell is strictly for authorized engagements. Always obtain written consent from the target organization.

**Q: How do I contribute to NeoShell?**  
A: See the [Development & Contributions](#development--contributions) section for guidelines.

**Q: Can I run NeoShell on a cloud server?**  
A: Yes, NeoShell works on any system with Python 3.7+ and dependencies, including AWS or Azure.

---

## License

NeoShell is licensed under the MIT License. See the [LICENSE](https://github.com/MrSpecks/NeoShell/blob/main/LICENSE) file for details.

---

## 🛡️ NeoShell: Built for Pentesters, Powered by Community

*Explore, contribute, and secure the web responsibly.*  
[Back to NeoShell Repository](https://github.com/MrSpecks/NeoShell)