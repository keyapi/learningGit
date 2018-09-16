print ("Login")

import requests
import getpass #no showing the input username and password


def login(username, password):
    route = "/rest/login"
    count = 0
    while count < 3:
        count += 1
        
        username = input("username: ")
        password = getpass.getpass("password: ")
        paras = f"?username={username}&password={password}"
        loginUrl = sellerUrl + route + paras
        
        re = requests.post(loginUrl)
        if re.status_code == 200:
            print ("Your login is successful!")
            return re
            break
        else:
            print ("Your " + str(count) + ". login failed, please try again! (max. 3 tries)")
    else:
        print ("Your 3 tries all failed, please contact admin!")

username = ""
password = ""
loginRe = login(username, password)

login_re_js = loginRe.json()
token_type = login_re_js['token_type']
access_token = login_re_js['access_token']
refresh_token = login_re_js['refresh_token']
head = {'Authorization': token_type + " " + access_token}