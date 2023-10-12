from selenium                                        import webdriver
from selenium.webdriver.common.by                    import By
from selenium.webdriver.common.keys                  import Keys
from selenium.webdriver.support.ui                   import WebDriverWait
from selenium.webdriver.support                      import expected_conditions as EC
from selenium.webdriver.common.action_chains         import ActionChains
from selenium.webdriver.support                      import expected_conditions
from selenium.webdriver.support.wait                 import WebDriverWait
from selenium.webdriver.common.desired_capabilities  import DesiredCapabilities
from undetected_chromedriver                         import Chrome
from time                                            import sleep
import time, pickle


class Republik:
    def __init__(self) -> None:
        self.url    = 'https://accounts.google.com/ServiceLogin'
        self.driver = Chrome(use_subprocess=True); self.driver.get(self.url)
        self.time   = 2
    
    def login_gmail(self, email, password):
        sleep(1)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')
        sleep(1)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(f'{password}\n')

        print("Sukses Login Google")

    def login_republik(self):
        self.driver.get("https://app.republik.gg/auth/log-in-option")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "ion-label.font-robotomedium:nth-child(7)").click()
        time.sleep(2)
        
        # Menunggu hingga jendela kedua terbuka
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)
        
        # Beralih ke jendela kedua
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Tunggu elemen "Login Google Account" muncul di jendela kedua
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "WBW9sf"))).click()
        except:
            print('Element not found in the second window.')

        # Beralih kembali ke jendela pertama
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(6)
      
        print('Berhasil Login Republik')


    def follow(self):
        self.driver.get("https://app.republik.gg/profile") 
        time.sleep(1)
        follow_button = self.driver.find_element(By.XPATH, '//*[@class="px-4 md ion-activatable"]/span[text()="Followers"]') #Klik Followers
        follow_button.click()
        time.sleep(2)

        print("Follow start")

        while True:
            time.sleep(3)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, '.ion-content-scroll-host > div > div:nth-child(1) > div ion-button.font-bold') #Klik Follow

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
                    print(f"Follow {button.text}")
                    time.sleep(0.1)
                else:
                    # Jika tombol adalah yang lain, lalu 'pass' (tidak lakukan apa-apa)
                    pass

            scroll = self.driver.find_element(By.CSS_SELECTOR, '.ion-content-scroll-host')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)

        print("Follow End")
# Usage:
if __name__ == "__main__":
    #  ---------- EDIT ----------
    email = 'your@gmail.com'  # Replace with your email
    password = 'yourpassword'  # Replace with your password
    #  ---------- EDIT ---------- 

    republik = Republik()
    republik.login_gmail(email, password)
    republik.login_republik()
    republik.follow()

