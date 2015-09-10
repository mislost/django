#!/usr/bin/python
import MySQLdb

def get_file():
        f = open('proxy.conf','r')
        s = f.read()
        s = eval(s)
        return s

try:
	conn =  MySQLdb.connect(host='localhost',user='root',passwd='60Bo@db.com',port=3306)
	cur = conn.cursor()
	conn.select_db('ope')
	my_db = get_file()
	for key in my_db:
		name = key
		ip_address = my_db[name]
		command = "insert into apache_client(name,ip_address)values(\"%s\",\"%s\")" % (name,ip_address)
		cur.execute(command)
		conn.commit()
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_file():
	f = open('proxy.conf','r')
	s = f.read()
	s = eval(s)
	return s
