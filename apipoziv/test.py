import requests
import json

url = "https://getpantry.cloud/apiv1/pantry/3ab3757e-2586-4248-8cd5-843b30ae8ab8/basket/ivantest"

payload = json.dumps({
	"id": "7634",
	"ime": "Ivan",
	"prezime": "Vasic",
	"smer": "mreze",
	"predmeti": [
		"engleski1",
		"arhitektura",
		"java",
		"fizicko",
		"dos"
	],
	"prosek": 8.66,
	"kontakt": {
		"adresa": "Marsala Birjuzova",
		"mesto": "Beograd",
		"telefon": "060 123 1232"
	}
})
headers = {
	'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
