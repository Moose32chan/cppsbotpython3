#simple login with requests (Not tested)
#
#will be unfinished for a while cause i'm lazy :(
#
#Also this will probably be an early outline for the final one so it may seem a bit weird.
#
#TODO: Fix login_data and c.post, Connect bot to server, basic bot functions
import requests

#number of bots
b = 1

#server // may be used in future version
s = input('Server:\n')

#login ip // may be used in future version
l = "172.104.66.25:6114"

if s == 'Covfefe':
        s == "45.79.161.185:6113"
        if b > 1:
                print('Sorry only 1 bot is supported at the moment!')
        exit()
        if s != 'Covfefe':
                print('Sorry, this server is not supported yet!')
        exit()

        with requests.Session() as c: #to login the account
                        url = 'http://media.cpps.me/play/?lang=en' #filler url
                        USER = 'd' #put username here
                        PASS = 'd' #put password here
                        headers = {'user-agent': 'my-app/0.0.1'} #put header here
                        login_data = dict(username=USER, password = PASS)  #this might work?
                        c.post(url, data=login_data, headers=headers) #this might work?
                        print('Logged in!')
                        r.status_code
                        if r.status_code == 101: #honestly not sure if this works lmao
                                print('Wrong Password, Try Again.')
                                end()
                                if r.status_code == 100:
                                        print('Wrong Username, Try Again.')
