import requests
import json

if __name__ == '__main__':
    url = 'http://169.45.237.245:8043/SiesaEnterpriseApi/Token'
    data = {
        'grant_type': 'password',
        'connection': '1',
        'company': '1',
        'username': 'unoee',
        'password': 'unoee',
        'Janer': '1'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': '.AspNet.Cookies=W32XbiR6QjwOQ1bSysqifB0fWknc7ySGeZZkp9h8fCiFYu4onUcVERYxtRqq3RhnS745z118scnpRl03-iW2hERNu06beJ6W3w2KYHnh7urWrYo9TrhvhbdT3yExk_7tf6mZGEqSMmDVovUy7nvopswrpA5HEq7EHXlW9yQ7bUkvAnDq0LlE_vb49dFQp2nrdvENC-PA7dFekWT8_aBeX9m_XF5ZEmakf6QxsDFvdx_4j_XapU0cVGjLG82wGJXlNCzmF1i3g3gz-tEnsZNMliVl7xVXZTEvbLw-p4MK4-uE5r9hSdsfYut7s27U51NBPNCee5d44zJuygb3vPWbqQ'
    }
    payload = ''
    for key, value in data.items():
        payload = payload + key + '='+value+'&'

    payloads = payload[0:len(payload)-1]
    print(payload, payloads)
    # si lo enviamos los datos  en json, post se encarg de serializarlo
    response = requests.post(url, data=payloads, headers=headers)
    token = response.json()
    print(token['access_token'])
