print ("Hello,GitHub!")
import requests

url="https://pyrode 3.com"
"https://raw.githubusercontent.com/your-username/hello-python/main/hello.py"
response=requests.get(url)

if response.status_code == 200:
	print("file content:")
	print (respnose.text)
else:
	print("faild to fetch file.status code:",response.status_code)
	