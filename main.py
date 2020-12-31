import amazonbot

chrome_driver_path = "C:\\Users\\hussain.parbtani\\Downloads\\chromedriver_win32\\chromedriver.exe"

chrome_profile_path = "user-data-dir=C:\\Users\\hussain.parbtani\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"

asin = 'B06X3W3TM4'

name = 'Joe Johnson'

add_line_1 = '2710 Guillot st.'

add_line_2 = 'Apt 1'

city = 'Dallas'

state = 'TX'

zip_code = '75204'

phone_number = '2819049402'

card_number = 'your card number here'

msg = 'Happy Birthday! Hope you have a good one!'

Bot = amazonbot.Amazon_Purchase_Bot(chrome_driver_path,chrome_profile_path,asin,name,add_line_1,add_line_2,city,state,zip_code,phone_number,card_number,msg)

Bot.Auto_Order()


