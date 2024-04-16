import os
import time
import requests
import colorama
import subprocess
import argparse
from colorama import Fore

parse = argparse.ArgumentParser("NavigateNet");
parse.add_argument("-d", "--direccion", help="direccion remota");
parse.add_argument("-w", "--wordlist", help="wordlist");
args = parse.parse_args();
class Decores:
	def banner():
		try:
			subprocess.run(["cat", "banner/banner.txt"]);
		except OSError:
			print("Error al imprimir banner");
	def creator():
		try:
			print("creador: DigitalNinja00")
			print("version: 1.0.0")
		except OSError as error:
			print(error)
class Codificar:
	def requests_get(url, pasa):
		try:
			while True:
				file = open(f"{pasa}", "r");
				manager = file.readlines();
				for x in manager:
					more = x.strip();
					res = requests.get(url+more)	
					if(res.status_code != 404):
						print(res.status_code, more)
					else:
						print(res.status_code, url+more)
						os.system("tput cuu1 && tput el")
		except OSError as error:
			print(error);
if(args.direccion):
	if(args.wordlist):
		Decores.banner();
		Decores.creator();
		print(Fore.RESET);
		Codificar.requests_get(args.direccion, args.wordlist);
