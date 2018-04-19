#借助request和json模块
import requests

def get_url(url):
	headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
	}
	result = requests.get(url,headers=headers)
	return result
def main():
	url = input("请输入链接地址")
	res = get_url(url)

	with open('res.txt','w',encoding='utf-8') as file:
		file.write(res.text)

if __name__ == "__main__":
	main()
