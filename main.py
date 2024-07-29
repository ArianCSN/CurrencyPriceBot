import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
from jdatetime import date as jdate
import requests
import pytz

# Constants
CHROME_DRIVER_PATH = "path_to_your_chromedriver"
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_telegram_chat_id"

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

# Start the WebDriver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the webpage
driver.get('https://www.navasan.net')

# Wait for the main table to be present
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-code]"))
    )
    # Wait an additional few seconds to ensure complete loading
    time.sleep(5)
    # Get the page source after waiting
    page_source = driver.page_source
finally:
    # Ensure the browser is closed properly
    driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract currency exchange rates
currency_rows = soup.find_all('tr', {'data-code': True})
currency_data = {}

# Helper function to safely extract price text
def get_price_text(element):
    if element:
        return element.text.strip().replace(',', ',')
    return "N/A"

for row in currency_rows:
    code = row['data-code']
    price_element = row.find(class_='price')
    price = get_price_text(price_element)
    currency_data[code] = price

# Validate that data was extracted correctly
required_codes = ["usd", "usd_sherkat", "eur", "gbp", "aed", "try", "try_hav", "cad", "cny", "rub", "aud", "sekkeh",
                  "nim", "rob", "usd_xau", "18ayar", ]
for code in required_codes:
    if code not in currency_data or currency_data[code] == "N/A":
        print(f"Warning: Missing or invalid data for {code}")

# Get the current Gregorian date
now = datetime.now()

# Get the current Iran time
IranTz = pytz.timezone("Iran")
timeInIran = datetime.now(IranTz)
currentTimeInIran = timeInIran.strftime("%H:%M")

# Convert to Shamsi (Persian) date
shamsi_date = jdate.fromgregorian(date=now.date())
day_names = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه"]
day_of_week = day_names[shamsi_date.weekday()]
formatted_shamsi_datetime = shamsi_date.strftime(f"{day_of_week} %Y/%m/%d ساعت {currentTimeInIran}")

# Create the formatted message
formatted_message = f"""
🇺🇸 دلار آمریکا تهران: {currency_data["usd"]}
🇺🇸 دلار آمریکا حواله: {currency_data["usd_shakhs"]}
🇪🇺 یورو اروپا: {currency_data["eur"]}
🇬🇧 پوند انگلیس: {currency_data["gbp"]}
🇦🇪 درهم امارات: {currency_data["aed"]}
🇹🇷 لیر ترکیه: {currency_data['try']}
🇹🇷 حواله لیر ترکیه: {currency_data['try_hav']}
🇨🇦 دلار کانادا: {currency_data['cad']}
🇨🇳 یوان چین: {currency_data['cny']}
🇷🇺 روبل روسیه: {currency_data['rub']}
🇦🇺 دلار استرالیا: {currency_data['aud']}

🌕 سکه: {currency_data['sekkeh']}
🌕 نیـم سکه: {currency_data['nim']}
🌕 ربـع سکه: {currency_data['rob']}

🌞 انس طلا: {currency_data['usd_xau']}
🌞 طلای 18 عیار: {currency_data['18ayar']}

📅 {formatted_shamsi_datetime}

🔗 @dollarprice
"""

# Send the message via Telegram (if applicable)
if 23 > int(timeInIran.strftime("%H")) > 10:
    # Remove leading/trailing spaces
    formatted_message = formatted_message.strip()

    # Replace the placeholders with actual values if needed
    response = requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                             params={"chat_id": TELEGRAM_CHAT_ID, "text": formatted_message},
                             )

    # Check if the request was successful
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Error sending message. Status code: {response.status_code}")
