import requests
import bs4 as bs

def extract_token(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	for i in soup.form.findChildren('input'):
		if i.get('name') == 'csrfmiddlewaretoken':
			return i.get('value')
	return None

def main():
	ses = requests.session()
	
	with open('./keys.txt', 'r') as file:
		ckdict = file.read().split(",")
	
	resp = ses.get("http://localhost:8000/polls/1/")
	
	csrft = requests.utils.dict_from_cookiejar(resp.cookies)	# Doesn't seem to work if read from the keyfile, but can be re-stolen like this
	
	ses.cookies.set('csrftoken', csrft['csrftoken']) 
	ses.cookies.set('sessionid', ckdict[1])
	
	csrfmwt = extract_token(resp)
	
	data = {'csrfmiddlewaretoken': csrfmwt, "choice" : 1}
		
	result = ses.post("http://localhost:8000/polls/1/vote/", data)
	
	print(result.text)

if __name__ == '__main__':
    main()