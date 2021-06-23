import requests
from bs4 import BeautifulSoup
import time
import smtplib

def get_current_price():
	#print("get_current_price")
	url=r"https://www.flipkart.com/safari-mosaic-check-in-luggage-30-inch/p/itm136a30fb66bba?pid=STCEWDB3WYHZHFXD&lid=LSTSTCEWDB3WYHZHFXDDJR6MH"
	r=requests.get(url)
	soup=BeautifulSoup(r.content,'html5lib')
	rupee=soup.find("div",class_="_30jeq3 _16Jk6d").text
	rupee=rupee.replace("₹","")
	rupee=rupee.replace(",","")
	#print(f"current price={rupee}")
	return rupee

def get_previous_prices():
	#print("get_previous_prices")
	file=open("prices.txt","r")
	previous_price=0
	for line in file:
		previous_price=line
	file.close()
	#print(f"last_price={previous_price}")
	try:
		return previous_price
	except:
		return 0

def put_current_price(price):
	#print("put_current_price")
	#print(f"putting pricec{price}")
	file =open("prices.txt","a")
	file.write(price)
	file.write("\n")
	file.close()

def mail_me(curr_price,previous_price):
	#print("mail_me")
	#print(f"mailing {curr_price} {previous_price}")
	try:
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login("mathewsamalp@gmail.com", "Am@190603")
		message=f"Price droped in flipkart from {previous_price} to {curr_price}"
		s.sendmail("mathewsamalp@gmail.com", "amalpmathews2003@gmail.com", message)
		s.quit()
	except:
		pass
		#print("mail not send")
	
def main():
	#print("main")
	curr_price=int(float(get_current_price()))
	previous_price=int(float(get_previous_prices()))
	if(curr_price<previous_price):
		mail_me(curr_price,previous_price)
	else:
		mail_me(curr_price,previous_price)
	put_current_price(str(curr_price))
	print("successfull")
	time.sleep(30)
	main()

if __name__ == '__main__':
	main()
