# coding: utf-8
# Felipe MArinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>
# Cria Pessoa

import random
import sys

file1 = open("nome.dat", "r")
file2 = open("sobrenome.dat", "r")

nomes = file1.read().split()
sobrenomes = file2.read().split()

class Pessoa:
	from unicodedata import normalize
	
	def __init__(self,i,f):
		self.nome = self.nome()
		self.sobrenome = self.sobrenome()
		self.idade = self.idade(i,f)
		self.email = self.email()

	def nome(self):
		return nomes[random.randint(0,len(nomes)-1)]

	def sobrenome(self):
		return sobrenomes[random.randint(0,len(sobrenomes)-1)]

	def idade(self,i,f):
		return str(random.randint(int(i),int(f)))

	def email(self, sufix="@gmail.com"):
		prefix = str.lower(self.remove_acentos(self.nome) + "." + self.remove_acentos(self.sobrenome) + "." + self.idade)
		return prefix + sufix

	def remove_acentos(self, txt, codif='utf-8'):
		return self.normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

if __name__ == "__main__":
	pessoa = Pessoa(sys.argv[1],sys.argv[2])
	print pessoa.nome + " " + pessoa.sobrenome + " " + pessoa.idade
	print pessoa.email
