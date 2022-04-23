import random

def randchoose(path):
	f=open(path)
	lists=f.readlines()
	result=lists[random.randint(0,len(lists)-1)]
	return str(result)