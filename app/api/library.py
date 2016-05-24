# coding: utf-8
import requests
from bs4 import BeautifulSoup
from PIL import Image
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper():
        before = time.time()
        func()
        after = time.time()
        print 'use', after-before
    return wrapper


class LibStudent():

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.cookies = None

    def get_cookie(self):
        url = 'http://210.35.251.243/reader/login.php'
        resp = requests.get(url)
        self.cookies = resp.cookies
        print resp.cookies

    def login(self):
        self.get_cookie()
        base_header = {'Content-Type': 'application/x-www-form-urlencoded'}
        login_url = 'http://210.35.251.243/reader/redr_verify.php'
        payload = {
            'captcha': self.captcha,
            'password': self.password,
            'username': self.username
        }
        params = 'number={username}&passwd={password}&captcha=' \
            '{captcha}&select=cert_no&returnUrl='.format(**payload)
        resp = requests.post(login_url, cookies=self.cookies,
                             headers=base_header, data=params)
        print resp.content
        print resp.cookies, 'login'

    def get_captcha(self):
        num_dict = {
            '1110011111000111100001111110011111100111'
            '1110011111100111111001111110011110000001': '1',
            '1100001110011001001111001111110011111001'
            '1111001111100111110011111001111100000000': '2',
            '1000001100111001111111001111100111100011'
            '1111100111111100111111000011100110000011': '3',
            '1111100111110001111000011100100110011001'
            '0011100100000000111110011111100111111001': '4',
            '0000000100111111001111110010001100011001'
            '1111110011111100001111001001100111000011': '5',
            '1100001110011001001111010011111100100011'
            '0001100100111100001111001001100111000011': '6',
            '0000000011111100111111001111100111110011'
            '1110011111001111100111110011111100111111': '7',
            '1100001110011001001111001001100111000011'
            '1001100100111100001111001001100111000011': '8',
            '1100001110011001001111000011110010011000'
            '1100010011111100101111001001100111000011': '9',
            '1110011111000011100110010011110000111100'
            '0011110000111100100110011100001111100111': '0'
        }
        img_dict = {
            0: (6, 14),
            1: (18, 26),
            2: (30, 38),
            3: (42, 50)
        }

        captcha_url = 'http://210.35.251.243/reader/captcha.php'
        resp = requests.get(captcha_url, cookies=self.cookies)
        print resp.cookies
        img = Image.open(StringIO(resp.content))

        def match_catcha(imglist):

            imgstr = ''.join([i.__str__() for i in imglist])
            return num_dict[imgstr]

        def parse_captcha(imgfile, num):

            imglist = (imgfile.getpixel((j, i)) for i in xrange(16, 26)
                       for j in xrange(img_dict[num][0], img_dict[num][1]))
            return imglist

        captcha_string = ''.join(
            (match_catcha(parse_captcha(img, i)) for i in xrange(4)))
        self.captcha = captcha_string
        print self.captcha

    def get_url(self, url, params=None, headers=None):
        resp = requests.get(
            url, headers=headers, cookies=self.cookies, params=params)
        return resp

    def post_url(self, url, data=None, headers=None):
        resp = requests.post(
            url, headers=headers, cookies=self.cookies, data=data)
        return resp

    def get_reader_info(self):
        info_url = 'http://210.35.251.243/reader/redr_info.php'
        info_html = self.get_url(info_url).content
        info_soup = BeautifulSoup(info_html, 'html.parser')
        info_td = info_soup.find_all('td')
        info_dict = {}

        for i in xrange(1, 29):
            try:
                info_dict[info_td[i].contents[0].string] = info_td[
                    i].contents[1].strip()
            except Exception, e:
                pass
        return info_dict

    def get_book_info(self, marc_no):
        book_url = 'http://210.35.251.243/opac/item.php?marc_no={}'.format(
            marc_no)
        # resp = requests.get(book_url)
        info_html = self.get_url(book_url).content
        info_soup = BeautifulSoup(info_html, 'html.parser')

        info_tr = info_soup.find_all('tr', {'class': 'whitetext'})
        if u'此书刊可能正在订购中或者处理中' in info_tr[0].text:
            return {u'message': u'此书刊可能正在订购中或者处理中'}

        detail = lambda tr: {
            u'索书号': tr.contents[1].string,
            u'条码号': tr.contents[3].string,
            u'年卷期': tr.contents[5].string,
            u'校区—馆藏地': tr.contents[7].text.strip(),
            u'书刊状态': tr.contents[9].string
        }

        detail_list = [detail(tr) for tr in info_tr]

        info_dl = info_soup.find_all('dl', {'class': 'booklist'})
        info_dict = [
            (dl.dt.text, dl.dd.text) for dl in info_dl[0:-2]
        ]

        main_info = {
            'detail': info_dict,
            'lib': detail_list
        }
        return main_info

    def get_borrow_info(self):
        borrow_url = 'http://210.35.251.243/reader/book_lst.php'
        info_html = self.get_url(borrow_url).content
        info_soup = BeautifulSoup(info_html, 'html.parser')
        info_tr = info_soup.find_all('tr')

        info_blue = info_soup.find_all('b', {'class': 'blue'})

        current_loan = [blue.string for blue in info_blue]

        detail = lambda contents: {
            u'barcode': contents[1].string,
            u'book': contents[3].text,
            u'marc_no': contents[3].a.get('href')[-10:],
            u'borrow': contents[5].string,
            u'recede': contents[7].string,
            u'renew': contents[9].string,
            u'location': contents[11].string,
            u'extra': contents[13].string,
            u'check': contents[15].input.get('onclick').split('\'')[3]
        }

        booklist = [detail(tr.contents) for tr in info_tr[1:-2]]

        bookinfo = {
            u'current_loan': current_loan,
            u'booklist': booklist
        }
        return bookinfo

    def get_borrow_hist(self):
        hist_url = 'http://210.35.251.243/reader/book_hist.php'
        hist_html = self.get_url(hist_url).content
        hist_soup = BeautifulSoup(hist_html, 'html.parser')
        hist_tr = hist_soup.find_all('tr')

        parsetr = lambda contents: [v.string for i, v in enumerate(
            contents) if i % 2 == 1 and i != 1]

        topic = parsetr(hist_tr[0])

        remark = lambda contents: dict(zip(topic, parsetr(contents)))

        booklist = [remark(tr.contents) for tr in hist_tr[1:]]
        return booklist

    def logout(self):
        logout_url = 'http://210.35.251.243/reader/logout.php'
        resp = requests.head(logout_url, cookies=self.cookies)
        return None
