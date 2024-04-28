import requests

url = "http://localhost:7932/split-query/"
query_text = "日本語のテキストを分割してください"

response = requests.post(url, json={'query_text': query_text, 'language': 'ja'})

if response.status_code == 200:
    result = response.json()
    print("Extracted search texts:", result)
else:
    print(f"Failed to get search texts. Status code: {response.status_code}")
