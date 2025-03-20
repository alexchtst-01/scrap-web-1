from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time

def main():
    driver = Driver(uc=True)

    driver.get("https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2014")
    time.sleep(5)

    target_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/eproc4/') and contains(@href, '/pengumumanlelang')]")

    for link in target_links:
        main_window = driver.current_window_handle
        
        href = link.get_attribute("href")
        
        driver.execute_script("window.open(arguments[0]);", href)
        
        time.sleep(2)
        
        driver.switch_to.window(driver.window_handles[-1])
        
        time.sleep(3)

        print(f"\n=== Data dari Halaman Baru ===")
        print(f"Title: {driver.title}")
        print(f"URL: {driver.current_url}\n")

        try:
            table = driver.find_element(By.TAG_NAME, "table")
            tbody = table.find_element(By.TAG_NAME, "tbody")
            rows = tbody.find_elements(By.TAG_NAME, "tr")
            
            for row in rows:
                col_names = row.find_elements(By.TAG_NAME, "th")
                col_values = row.find_elements(By.TAG_NAME, "td")
                
                for col_name, col_value in zip(col_names, col_values):
                    print(f"{col_name.text.strip()}: {col_value.text.strip()}")
            # break
        except Exception as e:
            print("Tidak dapat mengambil isi halaman:", e)

        driver.close()
        driver.switch_to.window(main_window)

    driver.quit()
    