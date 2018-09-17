import getpass
import requests
import json

def userInput():
    print("Please enter your PM username and press Enter button")
    username = input("username: ")
    #print("Please enter your password and press Enter button")
    password = getpass.getpass("password: ")
    return username, password

def login(sellerUrl, username, password):
    sellerUrl = sellerUrl
    username, password = userInput()
    route = "/rest/login"
    paras = f"?username={username}&password={password}"
    loginUrl = sellerUrl + route + paras  
    re = requests.post(loginUrl)
    return re

def loginTries(sellerUrl):
    sellerUrl = sellerUrl
    count = 0
    while count < 3:
        count += 1
        re = login(sellerUrl, username, password)
        if re.status_code == 200:
            print ("login successful")
            login_re_js = re.json()
            token_type = login_re_js['token_type']
            access_token = login_re_js['access_token']
            refresh_token = login_re_js['refresh_token']
            head = {'Authorization': token_type + " " + access_token}
            
            return token_type, access_token, refresh_token, head
            break
        else:
            print ("Your " + str(count) + ". login failed, please try again! (max. 3 tries)")
    else:
        print ("Your 3 tries all failed, please contact admin!")

	
if __name__== "__main__":
    loginTries(sellerUrl)
