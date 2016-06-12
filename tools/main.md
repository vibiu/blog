When you see this. I have make my desision  to build my own blog website.But now it seams that there are still loads of things waiting for me to do.
    
I'll talk about the techonical details first. I use python's frame Flask to build my back-end. I write the front-end by myself, though I was supposed to ask a guy who is professional of front-end to write it. 

As for Front-end reverse proxy, Nginx is my choice, beacause it's free and open source(though I maybe never have the chance to contribute a single code for nginx).

Since now, I only use sqlite as my database, I guess I would soon turn to Mysql or MongoDB. I was weak of Front-end, so I plan to find a Front frame to write my webpage, this could be Bootstrap or React. Maybe I should also learn Vue.js or Anguler.js. But I think I should choose it carefully for the fact that there are to many Front frame coming out these days.

Well, best wishes to myself.

# Python Code:

``` python
import time


def timer(func):
    def wrapper(*kw, **kwargs):
        before = time.time()
        func(*kw, **kwargs)
        after = time.time()
        print 'use: ', after - before
    return wrapper
```

# C Code:

``` c
#include <stdio.h>
void swap(int *a, int *b){
    int temp;

    temp = *b;
    *b = *a;
    *a = temp;
}
int main(){
    int x, y;

    scanf("%d %d", &x, &y);
    swap(&x, &y);
    printf("x is %d, y is %d \n", x, y);
    return 0;
}
```

# JavaScript Code:

``` javascript
var ajax = function(method, url, cb, data, dataType) {
    var xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP')
    xhr.open(method.toUpperCase(), url, true)
    if (method.toLowerCase() == 'get') {
        xhr.send(null)
    } else {
        var contentType = 'application/x-www-form-urlencoded'
        if (dataType) {
            if (dataType.toLowerCase() == 'json') {
                contentType = 'application/json'
            }
        }
        xhr.setRequestHeader('Content-type', contentType)
        xhr.send(data)
    }
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                cb(xhr.responseText)
            }
        }
    }
}
```
