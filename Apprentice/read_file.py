
import json

if __name__ == "__main__":

	with open('config.json', 'r') as content_file:
    		content = content_file.read()

	print(content)

	json_obj = json.loads(content)

	print(json_obj)

	print(json_obj['config']['character'])
