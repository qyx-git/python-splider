#借助request和json模块
import requests
import json

def get_hot_comments(res):
	comments_json = json.loads(res.text)
	hot_comments = comments_json['hotComments']
	with open('hot_comments.txt','w',encoding='utf-8') as file:
		for each in hot_comments:
			file.write(each['user']['nickname']+':\n\n')
			file.write(each['content']+'\n')
			file.write("--------------------------------\n")

def get_commons(url):
	headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'referer':'http://music.163.com/song?id=548651034'
	}

	params ='nNMVvGpyajZLf46sX8u6rGxNKV5kPuJj3T3TVxXQWgU1KBUeqt3X+d/5v6tM63a9nrW/Z2PSa7JB/g+lgjbEVObMLE6NhK5UPhy5C0lSphk6pcZJ0Id/PupGM28N0jn+rP8zONrCx1SGDniNHEQXiT9DrJpCuHpQWRcbYnZIZC3jrWanH7vPvcqGAnidSEZr'
	encSecKey = 'bb5b7ffee6ecb3d33e81efa61b0abf03e6774475271f3e27b9220a7470d78bc59c8f53675447eb90e3ef7fabe77ad2728d10e151736aaa5a83780376e0c6cbd6ed073f067a371a4cfe4704718626a3cb0e8f51eced690b091b502e7a31f91682a087b6559a5b1fd9aa0fd3417448d47b3efeb67b4a2e4894bb93e5383a12597f'
	
	data = {
		'params' : params,
		'encSecKey' : encSecKey
	}
	name_id = url.split("=")[1]
	target_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)
	res = requests.post(target_url,headers=headers,data = data)
	return res
def main():
	url = input("请输入链接地址")
	res = get_commons(url)
	get_hot_comments(res)

	with open('data.txt','w',encoding='utf-8') as file:
		file.write(res.text)

if __name__ == "__main__":
	main()
