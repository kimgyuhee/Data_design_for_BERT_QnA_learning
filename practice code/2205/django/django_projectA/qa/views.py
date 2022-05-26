from django.shortcuts import render
from django.db import connection


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


def profile(request):
    return render(request, 'qa/profile.html')
