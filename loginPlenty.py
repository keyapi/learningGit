print ("Login")

import requests
import getpass #no showing the input username and password

sellerUrl = sellerUrl
def login(sellerUrl, username, password):
    sellerUrl = sellerUrl
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
			login_re_js = re.json()
			token_type = login_re_js['token_type']
			access_token = login_re_js['access_token']
			refresh_token = login_re_js['refresh_token']
			head = {'Authorization': token_type + " " + access_token}
			
            return re
			return login_re_js
			return token_type
			return access_token
			return refresh_token
			return head
            break
        else:
            print ("Your " + str(count) + ". login failed, please try again! (max. 3 tries)")
    else:
        print ("Your 3 tries all failed, please contact admin!")

#username = ""
#password = ""
#loginRe = login(sellerUrl, username, password)

#return login_re_js = loginRe.json()
#return token_type = login_re_js['token_type']
#return access_token = login_re_js['access_token']
#return refresh_token = login_re_js['refresh_token']
#return head = {'Authorization': token_type + " " + access_token}