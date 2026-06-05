Markdown

# Linux Command Executor API

A secure, high-performance REST API built with Python and FastAPI designed to execute selective Linux system diagnostics and return real-time metrics in clean JSON format.

## 📌 Project Overview

This project serves as a bridge between the web application layer and native Linux system utilities. It provides structured endpoints to monitor core system health (uptime, disk storage, volatile memory, and active user context) while strictly adhering to system security best practices to avoid shell vulnerability exposure.

## 🔒 Security Architecture (RCE Prevention)

A primary engineering constraint of this project is the mitigation of **Remote Code Execution (RCE)** and **Shell Injection** vulnerabilities. 

* **The Problem:** Accepting dynamic user strings and executing them directly through a system shell allows malicious users to append destructive commands (e.g., `; rm -rf /`).
* **The Solution:** This API completely bypasses intermediate system shells (`shell=False`). System commands are hardcoded inside the application logic as strict argument arrays (e.g., `["df", "-h"]`). The Linux kernel evaluates these inputs strictly as passive flags rather than executable instructions, entirely neutralizing injection bugs.

## 📂 Project Architecture

The repository enforces a clean **Separation of Concerns (SoC)** by decoupling web routing from underlying system operations:

```text
project/
│
├── main.py             # Application entry point, configuration, and health routes
├── requirements.txt    # Project package dependency manifest
├── README.md           # System and API documentation
├── routes/
│   └── system.py       # Web layer: HTTP requests, API documentation, and routing logic
└── utils/
    └── executor.py     # System layer: Isolated, secure subprocess execution wrapper