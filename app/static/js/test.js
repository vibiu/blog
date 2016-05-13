// 定义默认的错误回调函数
const defaultError = function(xhr) {
    alert('Internal Server Error')
}

// 定义一个ajax函数
function ajaxPost(url, method, fun, data = null, err = defaultError) {

    if (window.XMLHttpRequest) { // Mozilla, Safari, IE7+ ...
        xhr = new XMLHttpRequest()
    } else if (window.ActiveXObject) { // IE 6 and older
        xhr = new ActiveXObject('Microsoft.XMLHTTP')
    }

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                fun(xhr)
            } else {
                err(xhr)
            }
        }
    }

    xhr.open(method, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(data)
}

// 获得表单数据
function userGet() {
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    var jsonObj = {
        'username': username,
        'password': password
    }
    return jsonObj
}

// 为页面插入获取的数据
function insertEmail(resp) {
    var emails = JSON.parse(resp.responseText).emails
    var page = document.getElementsByClassName('passage')[0]
    var link = document.createElement('a')

    page.innerHTML = ''
    for (var index = 0; index < emails.length; index++) {
        var div = document.createElement('div')
        var email = emails[index]

        div.innerHTML = 'from: ' + email['from'] +
            ' to: ' + email['to'] + '<br />' +
            'subject: ' + email['subject'] + '<br />' +
            'time: ' + email['time'] + '<br /><hr />'
        page.appendChild(div)
    }
    page.appendChild(link)
}

// 登陆
function Login() {
    var data = JSON.stringify(userGet())
    var url = '/api/1.0/test/login'
    var fun = function(resp) {
        alert(JSON.parse(resp.responseText)['message'])
        getMail()
    }

    ajaxPost(url, 'post', fun, data)
}

// 获得邮件消息
function getMail() {
    var username = userGet()['username']
    var url = '/api/1.0/test/getmail' +
        '?username=' + username
    var fun = function(resp) {
        insertEmail(resp)
    }

    ajaxPost(url, 'get', fun)
}

// 登出
function Logout() {
    var username = userGet()['username']
    var url = '/api/1.0/test/logout' +
        '?username=' + username
    var fun = function(resp) {
        alert(JSON.parse(resp.responseText)['message'])
    }

    ajaxPost(url, 'get', fun)
}

// Login();

// getMail();

// Logout();
