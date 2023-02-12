from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import hashlib
import json


class Scrapper:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_data(self):
        self.driver.get(
            "https://www.tokopedia.com/search?st=product&q=laptop&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=")

        counter_page = 0
        datas = []

        while counter_page < 10:
            for _ in range(0, 6500, 500):
                time.sleep(0.1)
                self.driver.execute_script("window.scrollBy(0, 500)")
            elements = self.driver.find_elements(
                by=By.CLASS_NAME, value='css-y5gcsw')
            for element in elements:
                my_string = time.time()
                id_res = str(hash(my_string))[1:13]
                nama_produk = element.find_element(
                    by=By.CLASS_NAME, value='css-3um8ox').text
                harga_produk = element.find_element(
                    by=By.CLASS_NAME, value='css-1ksb19c').text
                nama_penjual = element.find_element(
                    by=By.CLASS_NAME, value='css-1kdc32b').text
                rating_produk = element.find_element(
                    by=By.CLASS_NAME, value='css-yaxhi2').text
                jumlah_terjual = element.find_element(
                    by=By.CLASS_NAME, value='css-yaxhi2').text

            # des = self.driver.find_element(
            #     by=By.XPATH, value="//div[@class='css-y5gcsw']")
            # des.click()
            # # for desc in des:
            # deskripsi = des.find_element(
            #     by=By.CLASS_NAME, value='css-16inwn4').text
            # print("DESKRIPSI BOS: ", deskripsi)

                datas.append({
                    'id': id_res,
                    'nama': nama_produk,
                    'harga': harga_produk,
                    'penjual': nama_penjual,
                    # 'deskripsi': deskripsi,
                    'rating': rating_produk,
                    'jumlah_terjual': jumlah_terjual
                })
                counter_page += 1
                next_page = self.driver.find_element(
                    by=By.XPATH, value="//button[@class='css-16uzo3v-unf-pagination-item']")
                next_page.click()

            return datas
