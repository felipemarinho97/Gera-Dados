# coding: utf-8
# Felipe MArinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>
# Cria Pessoa

from unicodedata import normalize
from datetime import datetime
import random
import sys
import csv

now = datetime.now()

file1 = open("nome.dat", "r")
file2 = open("sobrenome.dat", "r")
file3 = open("municipios.csv", "rb")

def readCSV(file):
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

nomes = file1.read().split()
sobrenomes = file2.read().split()
cidades = readCSV(file3)


class Pessoa:
	def __init__(self,i=1,f=100):
		self.nome = nomes[random.randint(0,len(nomes)-1)]
		self.sobrenome = sobrenomes[random.randint(0,len(sobrenomes)-1)]
		self.idade = str(random.randint(int(i),int(f)))
		self.email = self.criaEmail()
		self.cidade = cidades[str(random.randint(0,len(cidades)-1))]

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
	print pessoa.cidade[3] + " - " + pessoa.cidade[0]
