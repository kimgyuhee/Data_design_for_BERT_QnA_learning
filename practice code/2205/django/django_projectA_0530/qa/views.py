from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect

def index(request):
    return render(request, 'qa/index.html')


def main(request):
    i = []
    context = []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT country, text FROM context;")
        result = cursor.fetchall()
        connection.commit()
        connection.close()
    except:
        connection.rollback()
        print("Failed Selecting in StockList")

    for entry in result:
        i.append(entry[0])
        context.append(entry[1])

    # index 가 호출될 때 전달할 contexts
    data = {
        'id': i[0],
        'contexts': context[0],
    }

    return render(request, 'qa/main.html', data)


def quiz(request):
    data = {
        'title': "여기는 퀴즈를 푸는 곳 입니다.",
        'id': '신난다.',
    }
    return render(request, 'qa/quiz.html', data)


def country(request):
    return render(request, 'qa/country.html')


import json
import requests


def mrc_run(input_data):
    response = requests.post('http://192.168.0.132:8888/mrc', json=input_data)
    response_data = json.loads(response.text)

    return response_data



def profile(request):

    if request.method == 'POST':
        context = "로마 가톨릭 사제와 수녀들이 주동하는 독립투쟁은 계속되고 혁명 정부도 수립되었으나 미국은 이를 인정하지 않았다."
        question = "민중들의 독립투쟁으로 수립한것은?"

        input_data = {'context': [context], 'question': [question]}

        mrc_run(input_data)
        
        return redirect('/')

    domain = request.GET.get('country')
    print(domain)

    i = []
    context = []
    domain_num = []

    cursor = connection.cursor()
    sql1 = "SELECT country, country_num, text FROM context WHERE country='{0}';".format(domain)
    # mysql = sql.replace("country_domain", domain)
    print(sql1)
    cursor.execute(sql1)
    result = cursor.fetchall()
    connection.commit()
    # connection.close()

    for entry in result:
        print(entry)
        i.append(entry[0])
        domain_num.append(entry[1])
        print(type(entry[2]))
        context.append(entry[2].strip(""))

    questions = []
    # qid = "SELECT ID FROM context WHERE country='{0}' limit 1;".format(domain)
    sql2 = "SELECT question FROM questions WHERE context_id=any(select ID from context where country='{0}')".format(domain)
    cursor.execute(sql2)
    result = cursor.fetchall()
    connection.commit()
    connection.close()

    for entry in result:
        questions.append(entry[0])

    # index 가 호출될 때 전달할 contexts
    data = {
        'domain_num': domain_num[:],
        'id': i[0],
        'contexts': context[:],
        'country': domain,
        'questions': questions[:],
    }

    return render(request, 'qa/profile.html', data)


