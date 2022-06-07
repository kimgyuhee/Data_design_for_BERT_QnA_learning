from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from .models import mrcdata
import json
import requests


def index(request):
    return render(request, 'qa/index.html')


def mrcTest(request):
    data_obj = mrcdata.objects.order_by('pk').last()
    context = {'data': data_obj}

    if request.method == 'POST':
        temp_content = request.POST.get('content')
        temp_question = request.POST.get('question')

        # 입력 데이터 구조 정의
        input_data = {'context': [temp_content], 'question': [temp_question]}
        temp_answer = mrc_run(input_data)

        # NerData 객체 생성
        data_obj = mrcdata(content=temp_content, question=temp_question, answer=temp_answer)
        data_obj.save()

        return redirect('mrcTest')

    return render(request, 'ButterBlockTest/mrcTest.html', context)


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


def mrc_run(input_data):
    ip_mrc_machine = "http://192.168.0.132:8888/mrc"

    response = requests.post(ip_mrc_machine, json=input_data)
    response_data = json.loads(response.text)

    answer = response_data[0].get('answer')
    return answer


def profile1(request):
    domain = request.GET.get('country')

    i = []
    context = []
    domain_num = []

    data_obj = mrcdata.objects.order_by('pk').last()
    print(data_obj)
    contextmrc = {'data': data_obj}
    print(contextmrc)

    answer = ''
    print('--------------')
    print('졸리다.')
    if request.method == 'POST':
        print('--------------')
        temp_content = request.POST.get('content')
        print(temp_content)
        temp_question = request.POST.get('qqq')
        print(temp_question)
        print('--------------')

        # 입력 데이터 구조 정의
        input_data = {'context': [temp_content], 'question': [temp_question]}
        temp_answer = mrc_run(input_data)

        print(temp_answer)
        answer = temp_answer[0].get('answer')
        # MrcData 객체 생성
        data_obj = mrcdata(content=temp_content, question=temp_question, answer=temp_answer)
        data_obj.save()
        print(answer)

        return redirect('profile')

    cursor = connection.cursor()
    sql1 = "SELECT country, country_num, text FROM context WHERE country='{0}';".format(domain)
    cursor.execute(sql1)
    result = cursor.fetchall()
    connection.commit()
    # connection.close()

    print('-------- 값 확인하기 -------- ')
    for entry in result:
        print(entry[0])
        i.append(entry[0])
        domain_num.append(entry[1])
        print(entry[1])
        context.append(entry[2].strip(""))
        print(entry[2])
    print('-------------- ')

    questions = []
    # qid = "SELECT ID FROM context WHERE country='{0}' limit 1;".format(domain)
    sql2 = "SELECT question FROM questions WHERE context_id=any(select ID from context where country='{0}')".format(
        domain)
    cursor.execute(sql2)
    result = cursor.fetchall()
    connection.commit()
    # connection.close()

    for entry in result:
        print(entry)
        questions.append(entry[0])

    counts = []
    for c in range(15):
        counts.append(str(c + 1))
    # index 가 호출될 때 전달할 contexts
    data = {
        'domain_num': domain_num[:],
        'id': i[0],
        'contexts': context[:],
        'country': domain,
        'questions': questions[:],
        'count': counts[:],
        'answer': answer,
    }
    # connection.close()
    # if request.method == 'POST':
    #     return redirect('profile')
    return render(request, 'qa/profile.html', data)


def profile2(request):
    data_obj = mrcdata.objects.order_by('pk').last()
    print(data_obj)
    temp_content = ''
    temp_question = ''
    temp_answer = ''

    if request.method == 'POST':
        print('--------------')
        temp_content = request.POST.get('content')
        print(temp_content)
        temp_question = request.POST.get('question')
        print(temp_question)
        print('--------------')

        # 입력 데이터 구조 정의
        input_data = {'context': [temp_content], 'question': [temp_question]}
        temp_answer = mrc_run(input_data)
        print(temp_answer)

        data_obj = mrcdata(content=temp_content, question=temp_question, answer=temp_answer)
        data_obj.save()

        context = {
            'data': data_obj,
            'content': temp_content,
            'question': temp_question,
            'answer': temp_answer,
        }
        print(context)

        return redirect('profile')

    context = {
        'data': data_obj,
        'content': temp_content,
        'question': temp_question,
        'answer': temp_answer,
    }

    return render(request, 'qa/profile.html', context)


def profile(request):
    # 선택한 나라의 값을 domain에 저장
    domain = request.GET.get('country')

    print('-------------------------------------------------------------------')
    # 폼에 데이터를 채운 후 submit 했을 때 POST 처리 방식
    data_obj = mrcdata.objects.order_by('pk').last()
    print(data_obj)
    context = {'data': data_obj}
    print(context)

    answer = ''
    question = ''
    if request.method == 'POST':
        print('--------------')
        temp_content = request.POST.get('text')
        print(temp_content)
        temp_question = request.POST.get('question')
        print(temp_question)
        print('--------------')

        # 입력 데이터 구조 정의
        input_data = {'context': [temp_content], 'question': [temp_question]}
        temp_answer = mrc_run(input_data)

        print(temp_answer)
        # global answer
        # answer = temp_answer[0].get('answer')
        # MrcData 객체 생성
        data_obj = mrcdata(content=temp_content, question=temp_question, answer=temp_answer)
        data_obj.save()
        print(answer)

        # return redirect('profile')
        answer = temp_answer
        question = temp_question

    cursor = connection.cursor()
    sql1 = "SELECT country, country_num, text FROM context WHERE country='{0}';".format(domain)
    cursor.execute(sql1)
    result = cursor.fetchall()
    connection.commit()
    # connection.close()
    print(result)

    print('-------- 값 확인하기 -------- ')
    for entry in result:
        country_domain = entry[0]
        print(country_domain)
        text = entry[2]
        print(text)
    print('-------------- ')

    questions = []
    sql2 = "SELECT question FROM questions WHERE context_id=any(select ID from context where country='{0}')".format(
        domain)
    cursor.execute(sql2)
    result = cursor.fetchall()
    connection.commit()
    # connection.close()

    for entry in result:
        print(entry)
        questions.append(entry[0])

    # index 가 호출될 때 전달할 contexts
    data = {
        'country': domain,
        'text': text,
        'questions': questions[:],
        'question': question,
        'answer': answer,
    }
    return render(request, 'qa/profile.html', data)
