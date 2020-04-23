# Create Fake info with scritp V0.1



from requests import get,post
from bs4 import BeautifulSoup
from time import sleep
import sys
from os import name,system
from colorama import Fore,Style
from random import choice
import re

colors = [Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.WHITE,Fore.CYAN]


def cleaner():
	if name=="nt":system('cls')
	else:system('clear')

def logo_printer():
	cleaner()
	logo = r""" _____       _            ____                                 _               
|  ___|__ _ | | __ ___   / ___|  ___  _ __    ___  _ __  __ _ | |_  ___   _ __ 
| |_  / _` || |/ // _ \ | |  _  / _ \| '_ \  / _ \| '__|/ _` || __|/ _ \ | '__|
|  _|| (_| ||   <|  __/ | |_| ||  __/| | | ||  __/| |  | (_| || |_| (_) || |   
|_|   \__,_||_|\_\\___|  \____| \___||_| |_| \___||_|   \__,_| \__|\___/ |_|  
     """
	_logo_enumer = 0
	for char in logo:
		sys.stdout.write(f"{choice(colors)}{char}{Style.RESET_ALL}")
		sys.stdout.flush()
		_logo_enumer +=1
		sleep(0.004)
	print(f"{colors[1]}Fake Info Generator by hadinet1\n{colors[2]}\tt.me/hadinet1")

class FakeGenrator:
	def __init__(self,country:str,sex:str):
		self.country = country
		self.sex = sex
		logo_printer()
		self.Generate()

	def hadi_printer(self,string):
		print("\n")
		for char in string:
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(0.05)

	def Generate(self):
		global colors
		req = post('https://datafakegenerator.com/generador.php',
			data={'pais':self.country,'sexo':self.sex,'de':18 ,'hasta':99}).text
		soup = BeautifulSoup(req,'html.parser')
		find = soup.find_all('div',attrs={'class':'6u 12u(mobile)'})
		response = []
		for result in find:
			result = result.text.strip()
			response.append(result)
		del response[:response.index("Name:")]
		output = ""
		i = 0
		while i < len(response):
			output += response[i]
			if i % 2 == 1: output += "\n"
			i = i + 1
		output = output.replace(":", " : ")
		f = open("info.txt", "w+")
		f.write(output)
		f.close()
		print(f"{colors[3]}====> new Info saved in Info.txt")

if __name__ == "__main__":
	try:
		country = sys.argv[1]
		sex = sys.argv[2]
		FakeGenrator(country,sex)
	except IndexError:
		logo_printer()
		for char in f"{colors[3]}[!]python {sys.argv[0]} country sex[Male/Female]\n":
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(0.05)