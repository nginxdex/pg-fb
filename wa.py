from selenium import webdriver

driver = webdriver.Chrome ()
driver.get ( 'https://web.whatsapp.com/')

input ('Read the QR code.')
name = input ('Enter user name or group name:')
msg = input ('Enter your message:')
count = int (input ('Enter the number of messages:'))


user = driver.find_element_by_xpath ('// span [@title = "{}"]'. format (name))
user.click ()

msg_box = driver.find_element_by_class_name ('_ 2S1VP')

for i in range (count):
    msg_box.send_keys (msg)
    button = driver.find_element_by_class_name ('_ 2lkdt')
    button.click ()
