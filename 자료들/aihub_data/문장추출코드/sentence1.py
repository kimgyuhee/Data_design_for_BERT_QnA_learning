import json

# 현재 파이썬 코드와 JSON 코드가 같은 위치에 존재해야함
with open('./tech.json', 'r', encoding='utf-8') as f :
    json_data = json.load(f)


sentences = json_data['data']
count = len(sentences)
print('================')
print(sentences[0], type(sentences[0]))
print(type(sentences), len(sentences))
print('================')

# 파일이 존재해야지 오류가 안생김
f_txt = open('c:/test/tech.txt', 'w', encoding='utf-8')

for i in range(count) :
    print('{}번째 문장 -> {}'.format(i+1, sentences[i]['ko']))
    f_txt.write(str(i+1)+'번째 문장 \n'+sentences[i]['ko'] + '\n\n')
    print('\n')

f_txt.close()