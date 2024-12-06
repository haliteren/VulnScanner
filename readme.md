#TR
# VulnScanner - Basit Web Güvenlik Tarayıcısı

**VulnScanner**, bir web uygulamasının temel güvenlik zafiyetlerini tespit etmeye yönelik geliştirilmiş bir araçtır. Bu araç, HTTP yanıtlarını analiz ederek potansiyel güvenlik açıklarını (örneğin, XSS, açık dizinler, güvenlik başlık eksiklikleri) tespit etmeyi hedefler.

---

##Kullanım

Hedef URL'yi taramak için:

python vulnscanner.py https://hedefsite.com

---

### 🚀 Özellikler
- HTTP güvenlik başlıklarının kontrolü
- Açık dizin taraması
- XSS gibi zafiyetleri temel düzeyde algılama
- Hedef URL'ye yönelik kolay tarama

---

### 📋  Gereksinimler
- Python 3.7+
- Gerekli kütüphaneler (aşağıda `requirements.txt` dosyasına bakın):
  - `requests`
  - `beautifulsoup4`

---

### ⚙️Kurulum

git clone https://github.com/kullaniciadi/VulnScanner.git
cd VulnScanner
pip install -r requirements.txt

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#EN
# VulnScanner - Basic Web Security Scanner

VulnScanner is a Python-based tool designed to identify basic security vulnerabilities in web applications. It scans a target website for missing security headers, open directories, and potential XSS (Cross-Site Scripting) vulnerabilities.

---

##Usage

To scan the target URL:

python vulnscanner.py https://targetsite.com

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
