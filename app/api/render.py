import re
code = """<p>When you see this. I have make my desision  to build my own blog website.But now it seams that there
 are still loads of things waiting for me to do.</p>
<p>I'll talk about the techonical details first. I use python's frame Flask to build my back-end. I write
 the front-end by myself, though I was supposed to ask a guy who is professional of front-end to write
 it. </p>
<p>As for Front-end reverse proxy, Nginx is my choice, beacause it's free and open source(though I maybe
 never have the chance to contribute a single code for nginx).</p>
<p>Since now, I only use sqlite as my database, I guess I would soon turn to Mysql or MongoDB. I was
 weak of Front-end, so I plan to find a Front frame to write my webpage, this could be Bootstrap or React
. Maybe I should also learn Vue.js or Anguler.js. But I think I should choose it carefully for the fact
 that there are to many Front frame coming out these days.</p>
<p>Well, best wishes to myself.</p>
<h1>python code:</h1>
<pre><code>def bubble_sort(bubble_list):
    list_length = len(bubble_list)
    for i in range(list_length):
        for j in range(i, list_length):
            if bubble_list[i] &gt; bubble_list[j]:
                bubble_list[i],bubble_list[j] = bubble_list[j],bubble_list[i]
    return bubble_list
</code></pre>
<h1>shell code:</h1>
<pre><code>for i in {1...9};do
    for j in $(seq 1 $i);do
        echo -ne $ix$j=$((i*j))\\t;
    done;
    echo;
done;
</code></pre>
<h1>javascript code:</h1>
<pre><code>if (window.XMLHttpRequest) { // Mozilla, Safari, IE7+ ...
    httpRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) { // IE 6 and older
    httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
};
httpRequest.onreadystatechange = function(){
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
            // perfect!
        } else {
            // there was a problem with the request,
            // for example the response may contain a 404 (Not Found)
            // or 500 (Internal Server Error) response code
        }
    } else {
        // still not ready
    }
};
httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
httpRequest.open('GET', 'http://www.example.org/some.file', true);
httpRequest.send(null);
</code></pre>
"""
kw_list = ['False', 'class', 'finally', 'is', 'return',
           'None', 'continue', 'for', 'lambda', 'try', 'True', 'def',
           'from', 'nonlocal', 'while', 'and', 'del', 'global', 'not',
           'with', 'as', 'elif', 'if', 'or', 'yield', 'assert', 'else',
           'import', 'pass', 'break', 'except', 'in', 'raise']


def splite_code(markdown):
    codepattern = re.compile('<pre><code>(.+?)</code></pre>', re.S)
    find_code = codepattern.findall(markdown)
    blist = []
    for i, v in enumerate(find_code):
        blist.append(main_replace(v))
    for num, code in enumerate(find_code):
        markdown = markdown.replace(code, main_replace(code))
    return markdown


def search_replace(kw, code):
    kwre = '({kw}\s)+'.format(kw=kw)
    kwpattern = re.compile(kwre)
    replace_word = ' <span class="kw">{kw}</span> '.format(kw=kw)
    return kwpattern.sub(replace_word, code)


def main_replace(code):
    for kw in kw_list:
        code = search_replace(kw, code)
    return code
