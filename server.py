# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, url_for, escape, request, render_template, make_response

import re
import os
import random

app = Flask(__name__)

user_name=""
user_class=""
user_school=""

def checkName(name):
    nameRegex = re.compile(r'''(
        ^                                      #begin with
        [ ]*                                   #ignore beginning spaces
        ([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ])([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]{1,6})              #1st name
        ([ ]+([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ])([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]{1,6}))?       #optional 2nd
        ([ ]+([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ])([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]{1,6}))?       #optional 3rd
        ([ ]+([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ])([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]{1,6}))?       #optional 4th
        [ ]*$                                  #ignore last spaces
        )''', re.VERBOSE)

    res = nameRegex.search(name)
    if res == None:
        return False
    else:
        full_name = ""
        for i in range(2,10):
            try:
                temp = res.group(i)
                if i % 3 == 2:
                    full_name += temp.upper()
                elif i % 3 == 0:
                    full_name += temp.lower() + ' '
            except Exception:
                break
    return full_name

def checkClass(name):
    classRegex = re.compile(r'''(
        ^
        [ ]*
        ([0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ])
        ([0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ ]+)
        ([0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ])
        [ ]*
        $
        )''', re.VERBOSE) 
    multipleSpaces = re.compile(r'[ ]{2,}')
    temp = ""
    res = classRegex.search(name)
    if res == None:
        return False
    for i in range(1,20):
        try:
            temp += res.group(i)
        except:
            pass
    res = re.sub(multipleSpaces, ' ', temp)
    return res.title()

def checkSchool(school):
    schoolRegex = re.compile(r'''(
        ^
        [ ]*
        ([0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ])
        ([0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ -]+)
        ([0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ])
        [ ]*
        $
        )''', re.VERBOSE) 
    multipleSpaces = re.compile(r'[ ]{2,}')
    temp = ""
    res = schoolRegex.search(school)
    if res == None:
        return False
    for i in range(1,20):
        try:
            temp += res.group(i)
        except:
            pass
    res = re.sub(multipleSpaces, ' ', temp)
    return res.title()

def checkQuestion(question):
    a = int(question[0])
    b = int(question[1])
    c = int(question[2])
    if ((0 > a) or (a > 4)) and ((0 > b) or (b > 4)) and ((0 > c) or (c > 4)):
        return -1
    if (a + b + c == 0):
        return 0
    if (a == 0):
        if (b == 0):
            return [c]
        else:
            if (b == c):
                return 1
            else:
                if (c == 0):
                    return [b]
                else:
                    return [b, c]
    else:
        if (b == 0):
            if (a == c):
                return 1
            else:
                if (c == 0):
                    return [a]
                else:
                    return [a, c]
        else:
            if (c == 0):
                if (a == b):
                    return 1
                else:
                    return [a, b]
            else:
                if (a == b) or (b == c) or (c == a):
                    return 1
                else:
                    return [a, b, c]

def generate1(question):

    answer = '' 
    os.chdir(r'database')
    os.chdir(r'question_' + str(question))
    
    with open('info.txt', 'r', encoding='utf-8') as f:
        number_of_paragraph = int(f.read())

    for paragraph in range(1, number_of_paragraph + 1):
        answer += '<p>'
        os.chdir(r'paragraph_' + str(paragraph))

        with open('info.txt', 'r', encoding='utf-8') as f:
            number_of_sentence = int(f.read())

        for sentence in range(1, number_of_sentence + 1):

            os.chdir(r'sentence_' + str(sentence))

            with open('info.txt', 'r', encoding='utf-8') as f:
                number_of_choice = int(f.read())

            choice = random.randint(1, number_of_choice)

            with open(str(choice) + r'.txt', 'r', encoding='utf-8') as f:
                choice = f.read()

            answer += choice + ' '
            os.chdir('..')
        answer += '</p>'
        answer += '<br>'
        os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    return answer

def generate2(question):
    answer = ""
    os.chdir(r'database')
    os.chdir(r'question_' + str(question))

    with open('info.txt', 'r', encoding='utf-8') as f:
        number_of_paragraph = int(f.read())

    for paragraph in range(1, number_of_paragraph + 1):
        answer += '<p>'
        os.chdir(r'paragraph_' + str(paragraph))

        with open('info.txt', 'r', encoding='utf-8') as f:
            number_of_sentence = int(f.read())

        for sentence in range(1, number_of_sentence + 1):

            os.chdir(r'sentence_' + str(sentence))

            with open('info.txt', 'r', encoding='utf-8') as f:
                number_of_choice = int(f.readline())
                numb = int(f.read())

            choices = random.sample(range(1, number_of_choice + 1), numb)

            for choice in choices:
                with open(str(choice) + r'.txt', 'r', encoding='utf-8') as f:
                    answer += f.read() + '<br>'
            os.chdir('..')
        answer += '</p>'
        answer += '<br>'
        os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    return answer

def generate(question):
    if question == 1 or question == 3:
        return generate1(question)
    elif question == 2 or question == 4:
        return generate2(question)


@app.route('/')
def homepage():

    title = "Cảm tình Đoàn Generator"

    try:
        return render_template('homepage.html', title=title)
    except Exception as e:
        return str(e)

@app.route('/information')
def information():

    title = "Điền thông tin cá nhân"
    
    try:
        return render_template('information.html', title=title, user_name=user_name, user_class=user_class, user_school=user_school)
    except Exception as e:
        return str(e)

@app.route('/checking', methods=['POST', 'GET'])
def checking():

    title = "Đang kiểm tra..."

    if request.method == 'GET':
        return redirect('/information')

    error = None

    try: 
        user_name = request.form['name']
        user_class = request.form['class']
        user_school = request.form['school']
        user_question = [request.form['question1'], request.form['question2'], request.form['question3']]
    except Exception as e:
        return str(e)

    if not checkName(user_name):
        error = "Tên không hợp lệ"
        title = "Kiểm tra lại tên"
        try:
            return render_template('error.html', error=error, title=title, user_name=user_name, user_class=user_class, user_school=user_school)
        except Exception as e:
            return str(e)
    
    # Check Class
    if not checkClass(user_class):
        error = "Lớp không hợp lệ"
        title = "Kiểm tra lại lớp"
        try:
            return render_template('error.html', error=error, title=title, user_name=user_name, user_class=user_class, user_school=user_school)
        except Exception as e:
            return str(e)

    # Check School
    if not checkSchool(user_school):
        error = "Trường không hợp lệ"
        title = "Kiểm tra lại trường"
        try:
            return render_template('error.html', error=error, title=title, user_name=user_name, user_class=user_class, user_school=user_school)
        except Exception as e:
            return str(e)

    # Check Question
    try:
        check = checkQuestion(user_question)
        if check == -1:
            return redirect('/information')
        elif check == 0:
            error = "Bạn vẫn chưa chọn câu hỏi"
            title = "Kiểm tra lại câu hỏi"
            return render_template('error.html', error=error, title=title, user_name=user_name, user_class=user_class, user_school=user_school)
        elif check == 1: 
            error = "Bạn chọn trùng câu hỏi"
            title = "Kiểm tra lại câu hỏi"
            return render_template('error.html', error=error, title=title, user_name=user_name, user_class=user_class, user_school=user_school)
    except Exception as e:
        return str(e)
    
    response = make_response(redirect('/result'))
    response.set_cookie('user_name', value=user_name)
    response.set_cookie('user_class', value=user_class)
    response.set_cookie('user_school', value=user_school)
    for i in range(0,3):
        try:
            response.set_cookie('user_question' + str(i+1), value=str(check[i]))
        except IndexError:
            response.set_cookie('user_question' + str(i+1), expires=0)
        
    return response

@app.route('/result')
def result():
    
    title = "Bài văn của bạn"

    try:
        user_name = request.cookies.get('user_name')
        user_class = request.cookies.get('user_class')
        user_school = request.cookies.get('user_school')
        question_1 = request.cookies.get('user_question1')
        paragraph_1 = generate(int(question_1))

        os.chdir(r'database')
        os.chdir(r'question_' + str(question_1))
        with open('debai.txt', 'r') as f:
            question_1 = f.read()
        os.chdir('..')
        os.chdir('..')

    except KeyError:
        return redirect('/information')
    except Exception as e:
        return str(e)

    try:
        question_2 = request.cookies.get('user_question2')
        if question_2 != None:
            paragraph_2 = generate(int(question_2))

            os.chdir(r'database')
            os.chdir(r'question_' + str(question_2))
            with open('debai.txt', 'r') as f:
                question_2 = f.read()
            os.chdir('..')
            os.chdir('..')

        else:
            return render_template('result.html', title=title, user_name=user_name, user_class=user_class, user_school=user_school, question_1=question_1, paragraph_1=paragraph_1)
    except KeyError:
        return render_template('result.html', title=title, user_name=user_name, user_class=user_class, user_school=user_school, question_1=question_1, paragraph_1=paragraph_1)
    except Exception as e:
        return str(e)

    try:
        question_3 = request.cookies.get('user_question3')
        if question_3 != None:
            paragraph_3 = generate(int(question_3))

            os.chdir(r'database')
            os.chdir(r'question_' + str(question_3))
            with open('debai.txt', 'r') as f:
                question_3 = f.read()
            os.chdir('..')
            os.chdir('..')

        else:
            return render_template('result.html', title=title, user_name=user_name, user_class=user_class, user_school=user_school, question_1=question_1, paragraph_1=paragraph_1, question_2=question_2, paragraph_2=paragraph_2)
    except KeyError:
        return render_template('result.html', title=title, user_name=user_name, user_class=user_class, user_school=user_school, question_1=question_1, paragraph_1=paragraph_1, question_2=question_2, paragraph_2=paragraph_2)
    except Exception as e:
        return str(e)
    
    try:
        return render_template('result.html', title=title, user_name=user_name, user_class=user_class, user_school=user_school, question_1=question_1, paragraph_1=paragraph_1, question_2=question_2, paragraph_2=paragraph_2, question_3=question_3, paragraph_3=paragraph_3)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=port, passthrough_errors=True, threaded=True)
