__author__ =  'CARA'

import random
import os
def cdk_gen(cdk_num,cdk_len):
	cdk = []
	with open('CDK.txt','w') as f:
		for x in range(cdk_num):
			cdkList = random.sample("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789",cdk_len)
			x = ''.join(cdkList)
			#添加到列表cdk
			cdk.append(x)
			#保存到文本
			f.write(x + '\n')
		f.close()
		return cdk


if __name__ == '__main__':
	cdk_gen(200,12)
