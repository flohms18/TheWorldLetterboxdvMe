import requests

res = requests.get('api.letterboxd.com/api/v0/films')
print(res.status_code)