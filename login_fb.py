from selenium                                        import webdriver
from selenium.webdriver.common.by                    import By
from selenium.webdriver.common.keys                  import Keys
from selenium.webdriver.support                      import expected_conditions as EC
from undetected_chromedriver                         import ChromeOptions
import time,json

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')

class Republik:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        #self.driver.maximize_window()
    
    def login_facebook(self):
        self.driver.get("https://web.facebook.com/")
        time.sleep(2)
        email = self.driver.find_element(By.NAME, 'email')
        password = self.driver.find_element(By.NAME, 'pass')
        email.send_keys("61551934197850")  # Ganti dengan username Facebook yang valid
        password.send_keys("Visual2023@#")  # Ganti dengan password Facebook yang valid
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        print('Berhasil Login Facebook')

    def login_republik(self):
        self.driver.get("https://app.republik.gg/auth/log-in-option")
        time.sleep(8)
        self.driver.find_element(By.CSS_SELECTOR, ".mt-4 > span").click() #Login via Facebook
        time.sleep(15)
        windows = self.driver.window_handles
        if len(windows) >= 10:
            self.driver.switch_to.window(windows[1])
            time.sleep(20)
            self.driver.find_element(By.CSS_SELECTOR, ".xtk6v10 > .x1lliihq").click() #Buka Jendela Baru
            time.sleep(20)
            windows = self.driver.window_handles
            if len(windows) >= 10:
                self.driver.switch_to.window(windows[2])
                time.sleep(20)
                
         # Export and save cookies to a file
        cookies = self.driver.get_cookies()
        with open('aulav.json', 'w') as cookies_file:
            json.dump(cookies, cookies_file)

        print('Berhasil Login Republik')


    def follow(self):
        self.driver.get("https://app.republik.gg/relations/101112895194112442124?following=true") 
        time.sleep(6)

        print("Follow start")

        #for _ in range(5):
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
                if button_text == 'Follow' or button_text == 'Follow Back':
                # Jika tombol adalah "Follow" atau "Follow Back", maka klik tombol
                    button.click()
                    print(f"Followed: {button.text}")
                    time.sleep(0.1)
                else:
                    # Jika tombol adalah yang lain, lalu 'pass' (tidak lakukan apa-apa)
                    pass

            scroll = self.driver.find_element(By.CSS_SELECTOR, '.ion-content-scroll-host')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)

        print("Follow End")

# Penggunaan:
republik = Republik()
republik.login_facebook()
republik.login_republik()
republik.follow()

