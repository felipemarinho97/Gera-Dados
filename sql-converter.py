# coding: utf-8
# SQLTest
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

import sqlite3

# def concerta(string):
# 	nova_string = ""
# 	for e in string:
# 		if e == "'":
# 			nova_string += "'" 
# 		if e != ".":
# 			nova_string += e

# 	nova_nova = ""
# 	for i in range(len(nova_string)):
# 		if i == 0:
# 			nova_nova += "\'" + nova_string[i]
# 		elif i == 1:
# 			nova_nova += nova_string[i] + "\'"
# 		elif i == 12:
# 			nova_nova += "\'" + nova_string[i]
# 		elif i > 11 and nova_string[i] == ",":
# 			nova_nova += "\'" + nova_string[i]
# 		elif nova_string[-1] == ")" and i >= (len(nova_string)-6):
# 			nova_nova += ""
# 			print "entrei"
# 		else:
# 			nova_nova += nova_string[i]
# 	return nova_nova

import random

def concerta(string):
	nova_string = ""
	for e in string:
		if e == "'":
			nova_string += "'" 
		if e != ".":
			nova_string += e
	info = nova_string.split(",")
	return "'%s',%s,%s,'%s',%s" % (info[0], info[1], info[2], info[3], info[4].split()[0])

def write():
	# print concerta("RO,11,00015,Alta Floresta D'Oeste,25.506")

	file = open("municipios.csv", "r")
	l = []

	for e in xrange(5570):
		l.append(file.readline())

	conn = sqlite3.connect("gera-dados.db")

	c = conn.cursor()

	# Create table
	c.execute('''CREATE TABLE municipios (
				id INTEGER PRIMARY KEY,
				uf text,
				cod_uf real,
				cod_munic real,
				nome text,
				populacao real
			)''')

	# Insert a row of data
	for e in l:
		line = concerta(e)
		print line
		# c.execute("INSERT INTO municipios VALUES (%s)" % line)
		c.execute("INSERT INTO municipios(uf,cod_uf,cod_munic,nome,populacao) VALUES (%s)" % concerta(e))

	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

def read():
	conn = sqlite3.connect("gera-dados.db")

	c = conn.cursor()

	c.execute("""SELECT nome,uf FROM municipios
		WHERE ID = '%i'""" % random.randint(0,5500))
	
	for e in c.fetchall():
		print e


read()