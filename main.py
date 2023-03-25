import requests

# Replace with your developer API key
api_key = ''

# Specify the file path
file_path = input("input file path ==> ")

# Read the content of the file
with open(file_path, 'r') as f:
    file_content = f.read()

# Set the parameters for the Pastebin API request
api_url = 'https://pastebin.com/api/api_post.php'
data = {
    'api_dev_key': api_key,
    'api_option': 'paste',
    'api_paste_code': file_content
}

# Make the API request
response = requests.post(api_url, data=data)

# Print the Pastebin URL if successful
f=open("logs.txt","a")
if response.ok:
    print('File uploaded to Pastebin:')
    print(response.text)
	f.writelines(f"{file_path}====>>{response.text}")
	f.close()
else:
    print('Error uploading file to Pastebin')
	f.close()
