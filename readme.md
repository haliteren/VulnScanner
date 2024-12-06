# VulnScanner - Basic Web Security Scanner

VulnScanner is a Python-based tool designed to identify basic security vulnerabilities in web applications. It scans a target website for missing security headers, open directories, and potential XSS (Cross-Site Scripting) vulnerabilities.

---

## 🚀 Features
- **Security Header Analysis:** Detects missing HTTP headers such as Content-Security-Policy, X-Content-Type-Options, etc.
- **Open Directory Scanning:** Checks for commonly exposed directories like `/admin`, `/login`, `/uploads`, etc.
- **Basic XSS Detection:** Analyzes the webpage for signs of Cross-Site Scripting vulnerabilities.

---

## 📋 Requirements
- Python 3.7 or higher
- Required libraries (install via `requirements.txt`):
  - `requests`
  - `beautifulsoup4`

---

## ⚙️ Installation
Clone the repository and install the dependencies:

```bash
git clone https://github.com/<your-username>/VulnScanner.git
cd VulnScanner
pip install -r requirements.txt
