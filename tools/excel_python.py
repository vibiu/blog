# coding:utf-8
import xlrd
import sys
sys.path.append("..")
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from app.models import Role, Student, Course, Post
from app.models import Course


from config import ProductConfig


app = Flask(__name__)
# app.config[
#     'SQLALCHEMY_DATABASE_URI'
# ] = 'mysql://pythonadmin:123456@localhost/pythonDB'
app.config['SQLALCHEMY_DATABASE_URI'] = ProductConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


data = xlrd.open_workbook("info/infos.xlsx")
table = data.sheets()[0]

nrows = table.nrows
ncols = table.ncols


def table_row(num):
    alist = [i for i in table.row_values(num)]
    return alist


def table_col(num):
    blist = [i for i in table.col_values(num)]
    return blist


def get_classifies_dict():

    classify_set = set(table_row(0))
    classify_dict = {}
    for i, v in enumerate(classify_set):
        if i != 0:
            classify_dict[v] = i
    return classify_dict


def classify_course(course_name):

    classify_dict = get_classifies_dict()
    return classify_dict[course_name]


def get_course(col_num):

    course_info = table_col(col_num)
    course = Course()
    # course_classify_name = course_info[0]
    course.classify = course_info[0]
    course.topic = course_info[1]
    course.teacher = course_info[2]
    course.introduction = course_info[3]
    course.form = course_info[4]
    course.frequency = course_info[5]
    course.dispass = course_info[6]
    return course


def insert_course():

    for i in range(1, ncols):
        course = get_course(i)
        db.session.add(course)
        db.session.commit()

    print 'insert course done!'

if __name__ == '__main__':

    insert_course()
    # insert_classifies()
    # for i,v in get_classifies_dict().items():
    #     print i,v

    # x = get_course(4)
    # print x.topic
