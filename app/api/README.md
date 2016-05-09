#主IP地址
http://121.42.195.83/api/1.0/test

## Login
url: http://121.42.195.83/api/1.0/test/login

method: post

head: Content-Type: application/json

data:

    {
        "username": [unicode],
        "password": [unicode]
    }
return:

    {"message":"login success"}

## Getmail
url: http://121.42.195.83/api/1.0/test/getmail

method: get

query params: 

    ?username=[unicode]

return:

    {
      "emails": [
        {
          "fid": "1", 
          "from": [unicode], 
          "id": [unicode], 
          "size": [unicode], 
          "subject": [unicode], 
          "time": "2015-11-7-10-46", 
          "to": [unicode]
        }
    }

## Logout
url: http://121.42.195.83/api/1.0/test/logout

method: get

query params: 

    ?username=[unicode]

return:

    {"message": "logout success"}
