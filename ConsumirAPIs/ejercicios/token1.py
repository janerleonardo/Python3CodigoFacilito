import requests

url = "http://169.45.237.245:8043/SiesaEnterpriseApi/Token"

payload = 'grant_type=password&connection=1&company=1&username=unoee&password=unoee'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': '.AspNet.Cookies=W32XbiR6QjwOQ1bSysqifB0fWknc7ySGeZZkp9h8fCiFYu4onUcVERYxtRqq3RhnS745z118scnpRl03-iW2hERNu06beJ6W3w2KYHnh7urWrYo9TrhvhbdT3yExk_7tf6mZGEqSMmDVovUy7nvopswrpA5HEq7EHXlW9yQ7bUkvAnDq0LlE_vb49dFQp2nrdvENC-PA7dFekWT8_aBeX9m_XF5ZEmakf6QxsDFvdx_4j_XapU0cVGjLG82wGJXlNCzmF1i3g3gz-tEnsZNMliVl7xVXZTEvbLw-p4MK4-uE5r9hSdsfYut7s27U51NBPNCee5d44zJuygb3vPWbqQ'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
