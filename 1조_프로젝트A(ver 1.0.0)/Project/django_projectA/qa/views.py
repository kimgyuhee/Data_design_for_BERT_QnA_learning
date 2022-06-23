from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
import json
import requests


def index(request):
    return render(request, 'qa/index.html')


# Butter Block을 연결한 후 해당 질문에 대한 답을 리턴헤주는 함수
def mrc_run(input_data):
    ip_mrc_machine = "http://192.168.0.132:8888/mrc"

    response = requests.post(ip_mrc_machine, json=input_data)
    response_data = json.loads(response.text)

    answer = response_data[0].get('answer')  # 답만 추출
    return answer  # 해당질문에 대한 답을 리턴


# 질의응답 페이지와 페이지에 필요한 데이터들을 넘겨주는 함수
def country(request):
    # 선택한 나라의 값을 domain에 저장
    domain = request.GET.get('country')

    text = ''  # 본문
    answer = ''  # 정답
    question = ''  # 질문
    cursor = connection.cursor()  # DB와 연동하기 위한 변수

    # 폼에 데이터를 채운 후 submit 했을 때 POST 처리 방식
    if request.method == 'POST':
        temp_content = request.POST.get('text')  # 페이지 폼에 적힌 본문의 내용을 변수에 담기
        temp_question = request.POST.get('question')  # 페이지 폼에 적힌 질문의 내용을 변수에 담기

        # 입력 데이터 구조 정의
        input_data = {'context': [temp_content], 'question': [temp_question]}
        try:
            temp_answer = mrc_run(input_data)  # mrc를 돌리기 위한 함수 호출
            answer = temp_answer  # 해당 질문에 대한 정답
            question = temp_question  # 선택된 또는 입력된 질문
            text = temp_content  # 입력된 본문
            if question.strip() == "":
                question = "질문을 입력해주세요."
                answer = "N/A"
        except:
            text = temp_content  # 입력된 본문
            question = "질의 응답을 할 수 없습니다."
            answer = "butter block을 연결해주세요."

    elif request.method == 'GET':
        sql1 = "SELECT country, country_num, text FROM context WHERE country='{0}';".format(domain)
        cursor.execute(sql1)
        result = cursor.fetchall()
        connection.commit()

        for entry in result:
            text = entry[2]

    questions = []
    sql2 = "SELECT question FROM questions WHERE context_id=any(select ID from context where country='{0}')".format(
        domain)
    cursor.execute(sql2)
    result = cursor.fetchall()
    connection.commit()

    for entry in result:
        questions.append(entry[0])

    if text == '':
        text = 'DB에 해당 국가 데이터가 존재하지 않습니다.'

    print('---------------')

    print(question)
    print(answer)
    print('---------------')

    # html의 웹 페이지에 넘겨줄 데이터 값들
    data = {
        'country': domain,
        'text': text,
        'questions': questions[:],
        'question': question,
        'answer': answer,
    }
    return render(request, 'qa/country.html', data)
