from selenium import webdriver
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time

options = webdriver.ChromeOptions()

#지정한 user-agent로 설정합니다.
user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
options.add_argument('user-agent=' + user_agent)

options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 초반 에러방지(실행에는 문제없으나 무슨영어뜸)

# options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
options.add_argument("disable-gpu") #GPU 를 비활성화 합니다.
# options.add_argument('--window-size= x, y') #실행되는 브라우저 크기를 지정할 수 있습니다.
# options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
# options.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
# options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.
options.add_argument('mute-audio') #브라우저에 음소거 옵션을 적용합니다.
# options.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.


driver = webdriver.Chrome(options=options)

print("qr코드를 5분안에 인식해주세요")

driver.get("https://upbit.com/signin/private/qr_code")

time.sleep(300)

driver.close
