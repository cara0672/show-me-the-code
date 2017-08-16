__author__ =  'CARA'


import pymysql


def read_cdk(path):
	cdk = []
	with open(path,'r') as f:
		for line in f.readlines():
			cdk.append(line.strip())
	return cdk


def save(path):
	for a in read_cdk(path):
		conn = pymysql.connect(user='root',passwd='',db=cdk_base)
		cur = conn.cursor()
		sql= 'insert into cdks(id,cdk) value(0,%s)'
		try:
		   cur.execute(sql,a)
		   conn.commit()
		   conn.close()
		except:
		   conn.rollback()



if __name__  ==  ' __main__ ':
	save('CDK.txt')
