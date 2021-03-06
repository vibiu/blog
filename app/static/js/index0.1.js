function commentSubmit() {
    var commentButton = document.getElementById('comment-submit');
    var commentBody = document.getElementById('comment-body');
    var commentEmail = document.getElementById('comment-email');

    if (commentBody.value =='') {
        alert('you haven\'t write your comment.');
    } else if  (commentEmail.value == '') {
        alert('you haven\'t remain your email address.');
    } else {
        var data = {
            "body": commentBody.value,
            "email": commentEmail.value
        }
        jsonData = JSON.stringify(data);
        ajaxPost(jsonData, '/api/1.0/comment');
        commentBody.value = '';
        commentEmail.value = '';
    }
}

function ajaxPost(data, url) {
    if (window.XMLHttpRequest) { // Mozilla, Safari, IE7+ ...
        xhr = new XMLHttpRequest();
    } else if (window.ActiveXObject) { // IE 6 and older
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 201) {
                alert(JSON.parse(xhr.responseText)['message'])
            } else {
                alert('Internal Server Error');
            }
        }
    }
    xhr.open('POST',url,true);
    xhr.setRequestHeader('Content-Type','application/json');
    xhr.send(data)
}

function insertMarkdown() {
    markdownGet('/api/1.0/markdown');
}

function markdownGet(url) {
    if (window.XMLHttpRequest) { // Mozilla, Safari, IE7+ ...
        xhr = new XMLHttpRequest();
    } else if (window.ActiveXObject) { // IE 6 and older
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                document.getElementsByClassName('passage')[0].innerHTML = xhr.responseText;
            } else {
                document.getElementsByClassName('passage')[0].innerHTML = null;
            }
        }
    }
    xhr.open('GET',url,true);
    xhr.send(null)
}
