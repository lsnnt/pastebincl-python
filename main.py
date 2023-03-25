import requests
filename=input("Input file location ==> ")
#filename = "pi.txt" # replace with the path of your file

with open(filename, "rb") as file:

	data = {
	    'api_dev_key': '<--enter your apidev key here-->', # enter your apidev key here
	    'api_paste_code': file,
	    'api_option': 'paste',
	}

	response = requests.post('https://pastebin.com/api/api_post.php', data=data)

	print(response.text)
