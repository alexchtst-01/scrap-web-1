from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import argparse

def main(url):
    
    print(url)
    # driver = Driver(uc=True)

    # driver.get(url)
    # time.sleep(5)

    # target_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/eproc4/') and contains(@href, '/pengumumanlelang')]")

    # # List untuk menyimpan semua data sebagai dictionary
    # data_list = []

    # for link in target_links:
    #     main_window = driver.current_window_handle
    #     href = link.get_attribute("href")

    #     driver.execute_script("window.open(arguments[0]);", href)
    #     time.sleep(2)

    #     driver.switch_to.window(driver.window_handles[-1])
    #     time.sleep(3)

    #     print(f"\n=== Mengambil Data dari Halaman Baru ===")
    #     print(f"Title: {driver.title}")
    #     print(f"URL: {driver.current_url}\n")

    #     # Dictionary untuk menyimpan data 1 halaman
    #     data_dict = {
    #         "URL": driver.current_url,
    #         "Judul": driver.title
    #     }

    #     try:
    #         table = driver.find_element(By.TAG_NAME, "table")
    #         tbody = table.find_element(By.TAG_NAME, "tbody")
    #         rows = tbody.find_elements(By.TAG_NAME, "tr")

    #         for row in rows:
    #             col_names = row.find_elements(By.TAG_NAME, "th")
    #             col_values = row.find_elements(By.TAG_NAME, "td")

    #             for col_name, col_value in zip(col_names, col_values):
    #                 data_dict[col_name.text.strip()] = col_value.text.strip()

    #         print(data_dict)  # Cetak hasil untuk debugging
    #         data_list.append(data_dict)

    #     except Exception as e:
    #         print("Tidak dapat mengambil isi halaman:", e)

    #     driver.close()
    #     driver.switch_to.window(main_window)

    # driver.quit()

    # # Simpan ke CSV menggunakan Pandas
    # df = pd.DataFrame(data_list)
    # df.to_csv("hasil_scraping.csv", index=False, encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a URL.")

    # Add the -url argument
    parser.add_argument("-url", type=str, required=True, help="The URL to process")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the URL argument
    main(args.url)
