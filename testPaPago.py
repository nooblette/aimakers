import requests
 
request_url = "https://openapi.naver.com/v1/papago/n2mt"
text = "Python is an easy to learn, powerful programming language.\
 It has efficient high-level data structures and\
 a simple but effective approach to object-oriented programming.\
 Python’s elegant syntax and dynamic typing, together with its interpreted nature,\
 make it an ideal language for scripting and rapid application development\
 in many areas on most platforms."
 
headers = {"X-Naver-Client-Id": "f4rciXG4MXTJUKmWNdOj", "X-Naver-Client-Secret": "O__t6k5YWe"}
params = {"source": "en", "target": "ko", "text": text}
response = requests.post(request_url, headers=headers, data=params)
 
result = response.json()
 
print(result) # ptrint result (JSON format)
print('\n')
print(result["message"]["result"]["translatedText"]) # print only translatedText 
