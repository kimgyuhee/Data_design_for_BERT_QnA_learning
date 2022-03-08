import json

# 현재 파이썬 코드와 JSON 코드가 같은 위치에 존재해야함
with open('./war.json', 'r', encoding='utf-8') as f : # json 파일 읽기 위한 변수 생성
    json_data = json.load(f) # json 코드 불러오기


sentences = json_data['sentence']
count = len(sentences)
print('================')
print(sentences[0], type(sentences[0]))
print(type(sentences), len(sentences))
print('================')

# 파일이 존재해야지 오류가 안생김
f_txt = open('c:/test/war.txt', 'w', encoding='utf-8')

for i in range(count) :
    print('{}번째 문장 -> {}'.format(i+1, sentences[i]['text']))
    f_txt.write(str(i+1)+'번째 문장 \n'+sentences[i]['text'] + '\n\n')
    print('\n')

f_txt.close()