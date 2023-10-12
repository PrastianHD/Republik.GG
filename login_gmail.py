from selenium                                        import webdriver
from selenium.webdriver.common.by                    import By
from selenium.webdriver.common.keys                  import Keys
from selenium.webdriver.chrome.service               import Service
from selenium.webdriver.support.ui                   import WebDriverWait
from selenium.webdriver.support                      import expected_conditions as EC
from selenium.webdriver.common.action_chains         import ActionChains
from selenium.webdriver.support                      import expected_conditions
from selenium.webdriver.support.wait                 import WebDriverWait
from selenium.webdriver.common.desired_capabilities  import DesiredCapabilities
from undetected_chromedriver                         import ChromeOptions
from time                                            import sleep
import time, pickle

user_agent = "Mozilla/5.0 (Linux; Android 6.0.1; SM-J510GN Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
chrome_options = ChromeOptions()
chrome_options.add_argument(f"user-agent={user_agent}")
#chrome_options.add_argument('--headless')


driver_path = r"C:\Script Bot\chromedriver.exe"  # Replace with your Chromedriver path

class Republik:
    def __init__(self) -> None:
        self.url    = 'https://accounts.google.com/ServiceLogin'
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path), options=chrome_options)
        self.driver.get(self.url)
        self.time   = 5
        
        
    def login_gmail(self, email, password):
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(f'{password}\n')

        print("Sukses Login Google")

    def login_republik(self):
        self.driver.get("https://app.republik.gg/auth/log-in-option")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "ion-label.font-robotomedium:nth-child(7)").click()
        time.sleep(2)

        # Menunggu semua jendela terbuka
        while len(self.driver.window_handles) < 2:
            time.sleep(1)

        # Beralih ke jendela kedua
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Tunggu elemen "Use your Google Account" muncul
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "WBW9sf"))).click()
        except:
            print('Element not found in the second window.')

        # Tunggu semua jendela terbuka
        while len(self.driver.window_handles) < 3:
            time.sleep(1)

        # Beralih ke jendela ketiga
        self.driver.switch_to.window(self.driver.window_handles[2])
        print('Berhasil Login Republik')



    def follow(self):
        self.driver.get("https://app.republik.gg/relations/a1c07f21-4f2a-4b99-91b2-d3e26473e81f?following=true") 
        time.sleep(6)
        print("Follow start")

        #for _ in range(5):
        while True:
            time.sleep(3)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, '.ion-content-scroll-host > div > div:nth-child(1) > div ion-button.font-bold')

            if not buttons:
                print("Follow End")
                break  # Keluar dari loop jika tidak ada tombol "Follow" lagi

            for button in buttons:
                # Dapatkan teks pada tombol (Follow, Follow Back, atau yang lain)
                button_text = button.text

                # Periksa teks tombol
                if button_text == 'Follow Back':
                # Jika tombol adalah "Follow" atau "Follow Back", maka klik tombol
                    button.click()
                    time.sleep(0.3)
                else:
                    # Jika tombol adalah yang lain, lalu 'pass' (tidak lakukan apa-apa)
                    print(f"No action required: {button.text}")

            scroll = self.driver.find_element(By.CSS_SELECTOR, '.ion-content-scroll-host')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)

        print("Follow End")

# Penggunaan:
if __name__ == "__main__":
    #  ---------- EDIT ----------
    email = 'prastianhd01@gmail.com' # replace email
    password = 'Prastianhd01@#' # replace password
    #  ---------- EDIT ---------- 

    republik = Republik()
    republik.login_gmail(email, password)
    republik.login_republik()
    republik.follow()

