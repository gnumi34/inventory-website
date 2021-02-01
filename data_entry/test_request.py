import requests

response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'USD'})
rates = response.json()['rates']
print(f"Today's USD to IDR currency: {rates['IDR']}")