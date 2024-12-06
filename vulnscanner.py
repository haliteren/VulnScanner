import requests
from bs4 import BeautifulSoup
import sys

def check_security_headers(response):
    print("\n[+] Güvenlik Başlıkları Kontrol Ediliyor:")
    security_headers = [
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-XSS-Protection"
    ]
    for header in security_headers:
        if header in response.headers:
            print(f"    {header}: BULUNDU")
        else:
            print(f"    {header}: EKSİK")

def check_open_directories(url):
    print("\n[+] Açık Dizin Kontrolü:")
    common_dirs = ["admin", "login", "backup", "uploads"]
    for directory in common_dirs:
        full_url = f"{url}/{directory}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"    {full_url} - AÇIK")
        else:
            print(f"    {full_url} - KAPALI")

def check_xss(response):
    print("\n[+] XSS Açığı Kontrolü:")
    soup = BeautifulSoup(response.text, "html.parser")
    if "<script>" in str(soup):
        print("    Potansiyel XSS tespit edildi!")
    else:
        print("    XSS tespit edilmedi.")

def main(url):
    print(f"[*] {url} adresine bağlanılıyor...")
    try:
        response = requests.get(url)
        print(f"[+] HTTP Durum Kodu: {response.status_code}")
        if response.status_code == 200:
            check_security_headers(response)
            check_open_directories(url)
            check_xss(response)
        else:
            print("[-] Siteye erişilemedi.")
    except requests.exceptions.RequestException as e:
        print(f"[-] Hata: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python vulnscanner.py <URL>")
    else:
        target_url = sys.argv[1]
        main(target_url)
