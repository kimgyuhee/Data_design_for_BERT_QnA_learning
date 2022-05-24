from django.shortcuts import render
from django.db import connection


def index(request):
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
        'contexts': context[:],
    }

    return render(request, 'qa/index.html', data)
