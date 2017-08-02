__author__ =  'CARA'


import random
import pymysql
cdk = []
conn = pymysql.connect(user='root',passwd='',db='cdk_base')
cur = conn.cursor()

def cdk_generate(suiji):
	for x in range(suiji):
		cdkList = random.sample("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789",12)
		cdk.append(''.join(cdkList))
	return(cdk)

def save():
	for a in cdk_shengcheng(200):
		sql= """insert into cdks(id,cdk) value(0,'%s')""" % (a)
		try:
		   cur.execute(sql)
		   conn.commit()
		except:
		   conn.rollback()
	conn.close()
if __name__  ==  ' __main__ ':
	cdk = []
	conn = pymysql.connect(user='root',passwd='',db='cdk_base')
	cur = conn.cursor()
	save()

