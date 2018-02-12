#simple login with requests (Not tested)
#
#im aware it doesnt work, im learning python3 so as i know more this will get better
#
#Also this will probably be an early outline for the final one so it may seem a bit weird.
#
#TODO: Fix login_data and c.post, Connect bot to server, basic bot functions
import requests

#number of bots
b = 1

#server // may be used in future version
s = ('Covfefe')

#login ip // may be used in future version
l = "172.104.66.25:6114"

if s == 'Covfefe':
        s == "45.79.161.185:6113"
        if b > 1:
                print('Sorry only 1 bot is supported at the moment!')
                
        if s != 'Covfefe':
                print('Sorry, this server is not supported yet!')

        with requests.Session() as c: #to login the account
                        url = 'http://media.cpps.me/play/?lang=en' #filler url
                        USER = 'ISuckAtFind4' #put username here
                        PASS = 'mason1234' #put password here
                        headers = {'user-agent': 'my-app/0.0.1'} #put header here
                        login_data = dict(Penguin_Name=USER, Password = PASS)  #this might work?
                        c.post(url, data=login_data, headers=headers) #this might work?
