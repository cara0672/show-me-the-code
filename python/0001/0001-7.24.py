import random
cdk = []
for x in range(200):
	cdkList = random.sample("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789",12)
	cdk.append(''.join(cdkList))
print(cdk)
print(len(cdk))


