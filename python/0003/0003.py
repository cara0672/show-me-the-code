__author__ =  'CARA'


import redis


def read_cdk(path):
	cdk = []
	with open(path,'r') as f:
		for line in f.readlines():
			cdk.append(line.strip())
	return cdk

def write_redis(path,key_name):
	try:
		cr = redis.Redis(host='loalhost',port=6379)
		for line in read_cdk(path):
			r.rpush(key_name,line)
	except Exception as e:
		print(e)

write_redis('CDK.txt','keys')

if __name__  ==  ' __main__ ':
	save('CDK.txt')