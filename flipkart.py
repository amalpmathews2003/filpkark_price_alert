from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import time
import smtplib

def get_current_price():
	print("get_current_price")
	url=r"https://www.flipkart.com/safari-mosaic-check-in-luggage-30-inch/p/itm136a30fb66bba?pid=STCEWDB3WYHZHFXD&lid=LSTSTCEWDB3WYHZHFXDDJR6MH"
	r=requests.get(url)
	soup=BeautifulSoup(r.content,'html5lib')
	rupee=soup.find("div",class_="_30jeq3 _16Jk6d").text
	rupee=rupee.replace("₹","")
	rupee=rupee.replace(",","")
	print(f"current price={rupee}")
	return rupee

def get_previous_prices():
	print("get_previous_prices")
	file=open("prices.txt","r")
	previous_price=0
	for line in file:
		previous_price=line
	file.close()
	print(f"last_price={previous_price}")
	try:
		return previous_price
	except:
		return 0

def put_current_price(price):
	print("put_current_price")
	print(f"putting pricec{price}")
	file =open("prices.txt","w")
	file.write(price)
	file.write("\n")
	file.close()

def mail_me(curr_price,previous_price):
	"""
	print("mail_me")
	print(f"mailing {curr_price} {previous_price}")
	
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("mathewsamalp@gmail.com", "Am@190603")
	
	s.sendmail("mathewsamalp@gmail.com", "amalpmathews2003@gmail.com", message)
	s.quit()
	"""
	account_sid = 'AC5e6191cbffc187290e346dc24e6b82c1'
	auth_token = '96a00d587ab6af8197d779f0b400a4d1'
	client = Client(account_sid, auth_token)
	body=f"Price droped in flipkart from {previous_price} to {curr_price}"
	message = client.messages.create(
                              from_='+18326375819',
                              body =body,
                              to ='+918547756528'
                          )
		

def main2():
	print("main")
	curr_price=int(get_current_price())
	previous_price=int(get_previous_prices())
	if(curr_price<previous_price):
		mail_me(curr_price,previous_price)
	else:
		print("wait")
		pass
	put_current_price(str(curr_price))
	print("successfull")
	time.sleep(30)
	main2()

if __name__ == '__main__':
	main2()
