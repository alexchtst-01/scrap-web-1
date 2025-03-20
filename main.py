from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

def record_pagination(links):
    filename = f"links_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "a") as f:
        for link in links:
            f.write(f"Title: {link.text.strip()} | Links: {link.get_attribute('href')}\n")

# Inisialisasi driver dengan mode stealth
driver = Driver(uc=True)  # Gunakan undetected_chromedriver bawaan SeleniumBase

driver.get("https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2014")  # Ganti dengan URL target
time.sleep(5)  # Tunggu halaman termuat

while True:
    try:
        # Cari tombol Next menggunakan SeleniumBase
        next_button = driver.find_element(By.CSS_SELECTOR, "a.page-link[aria-label='Next']")
        
        # target_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/eproc4/*/pengumumanlelang']")
        
        target_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/eproc4/') and contains(@href, '/pengumumanlelang')]")
        
        record_pagination(target_links)
        
        break

        # Jika tombol memiliki atribut disabled atau tidak bisa diklik, hentikan loop
        if "disabled" in next_button.get_attribute("class") or not next_button.is_displayed():
            print("Pagination selesai.")
            break
        
        # Simulasi interaksi manusia (scroll dan klik)
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        time.sleep(1)  # Tunggu sejenak agar tampak alami
        next_button.click()
        print("Klik tombol Next")

        time.sleep(3)  # Tunggu data baru termuat
    except Exception as e:
        print("Tidak ada tombol Next atau terjadi error:", e)
        break

driver.quit()
