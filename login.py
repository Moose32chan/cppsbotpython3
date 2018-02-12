#simple login with requests (Not tested)
#
#will be unfinished for a while cause i'm lazy :(
#
#Also this will probably be an early outline for the final one so it may seem a bit weird.
#
#TODO: Fix login_data and c.post, Connect bot to server, basic bot functions
import requests

#number of bots
b = input('Amount of bots:\n')

#server (only Covfefe is supported atm)
s = input('Server:\n')

#login ip // may be used in future version
l = "172.104.66.25:6114"

if s == Covfefe:
	s == "45.79.161.185:6113"
	if b > 1:
	print('Sorry only 1 bot is supported at the moment!')
	exit()
	if s != 'Covfefe':
		print('Sorry, this server isn\'t supported yet!')
		exit()

		with requests.Session() as c: #to login the account
			url = 'media.cpps.me/play' #filler url
			USER = '' #put username here
			PASS = '' #put password here
			login_data = dict(PenguinName=USER, Password = PASS)  #fix this
			c.post(url, data=login_data, headers={"Referer": "cpps.me"}) #fix this
