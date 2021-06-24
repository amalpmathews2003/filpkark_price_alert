from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import time
import smtplib
import os

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
	return os.environ["prev_price"]

def put_current_price(price):
	os.environ["prev_price"]=price
def mail_me(curr_price,previous_price):
	account_sid = os.environ['account_sid']
	auth_token = os.environ['auth_token']
	client = Client(account_sid, auth_token)
	body=f"Price droped in flipkart from {previous_price} to {curr_price}"
	message = client.messages.create(
                              from_='+18326375819',
                              body =body,
                              to =os.environ['phone']
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
	time.sleep(5*60)
	main2()

if __name__ == '__main__':
	main2()
