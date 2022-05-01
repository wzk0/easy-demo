# 简单的Python函数!

1. 从txt文件随机抽取:

* name:
**randchoose**

* src:
```
import random

def randchoose(path):
	f=open(path)
	lists=f.readlines()
	result=lists[random.randint(0,len(lists)-1)]
	return str(result)
  ```
* raw:
https://raw.githubusercontent.com/wzk0/simple-python-demo/main/randchoose.py

* usage:
> randchoose(path)

---
