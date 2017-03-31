# coding: utf-8
# Felipe MArinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>
# Cria Pessoa

from unicodedata import normalize
from datetime import datetime
import random
import sys
import csv
from tools import sqlconverter

now = datetime.now()

class Database:
	file1 = open("data/nome.dat", "r")
	file2 = open("data/sobrenome.dat", "r")
	#file3 = open("data/municipios.csv", "rb")
	
	def __init__(self):
		self.nomes = self.file1.read().split()
		self.sobrenomes = self.file2.read().split()
		self.cidades = sqlconverter.read("data/dados.db")

	def readCSV(self,file):
		l = []
		dic = {}
		reader = csv.reader(file)
		try:
			for e in reader:
				l.append(e)
		except:
			pass
		for i in range(len(l)):
			dic[str(i)] = l[i]
		return dic

class Pessoa:
	db = Database()
	
	def __init__(self,i=1,f=100):
		self.nome = self.db.nomes[random.randint(0,len(self.db.nomes)-1)]
		self.sobrenome = self.db.sobrenomes[random.randint(0,len(self.db.sobrenomes)-1)]
		self.idade = str(random.randint(int(i),int(f)))
		self.email = self.criaEmail()
		self.cidade = self.db.cidades

	def criaEmail(self, sufix="@gmail.com"):
		ano = str(now.year - int(self.idade))
		prefix = str.lower(self._remove_acentos(self.nome) + "." + self._remove_acentos(self.sobrenome) + "." + ano)
		return prefix + sufix

	def _remove_acentos(self, txt, codif='utf-8'):
		return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

if __name__ == "__main__":
	if len(sys.argv) > 1:
		pessoa = Pessoa(sys.argv[1],sys.argv[2])
	else:
		pessoa = Pessoa()
	print pessoa.nome + " " + pessoa.sobrenome + " " + pessoa.idade
	print pessoa.email
	print pessoa.cidade[0] + " - " + pessoa.cidade[1]
