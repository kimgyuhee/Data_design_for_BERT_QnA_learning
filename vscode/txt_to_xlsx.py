from hanspell import spell_checker
from pykospacing import Spacing
# import xlwt
import pandas as pd
import kss
import re
import os

# TXT 파일을 XLS 파일로 변환해주는 클래스 
class Converter:
    """
    * 클래스 내부에 정의된 함수인 메서드의 첫번째 인자는 반드시 self여야 한다.
    파이썬의 첫번째 인자로 항상 클래스 인스턴스가 전달되기 때문에
    -> Converter의 대한 정보
    즉, 클래스 내에 정의된 self는 클래스 인스턴스이다.
    """
    # TXT 파일의 저장 경로를 지정 받는 함수
    def open_txt(self) : 
        
        while True : # 올바른 txt 파일을 입력받을 때 까지 돌아가는 반복문 생성
            # 'C:\\Data_design_for_BERT_QnA_learning\\country\\F_China.txt'
            # 'C:\Data_design_for_BERT_QnA_learning\country\F_China.txt'
            file_path = input('txt 파일 경로: ' )
            if file_path.strip() == '' : # 아무것도 입력하지 않았을 경우
                print('아무것도 입력하지 않았습니다.\n')
                continue
            if file_path[-1:-5:-1][::-1] != '.txt' : # 입력값 마지막이 .txt 가 아닐 경우
                print('txt 파일을 찾아 경로를 입력해주세요.\n')
                continue
            try :
                # 입력 받은 txt 파일을 읽기 모드로 불러옵니다. 프로그램이 끝나면 자동으로 닫힌다.
                with open(file_path, 'r', encoding='UTF-8') as data :
                    lines = data.readlines() # 모든 줄을 읽고 각 요소를 리스트형태로 돌려준다.
            except FileNotFoundError :
                print('입력 경로에 txt 파일이 존재하지 않습니다.\n')
                continue
            else :
                break # 올바르게 입력 받았을 경우 반복문을 빠져나간다.

        return lines

    # XLS 저장할 경로 입력 받을지 묻는 함수
    def ask_directory(self) :
        default_xls_path = 'C:\\Data_design_for_BERT_QnA_learning\\check\\xlsx\\' # 기본경로
        while True :
            ask = input('xls 파일은 {}에 저장됩니다.\n다른 경로에 저장하시겠습니까?: [Y/N] '.format(default_xls_path))
            if ask in ['Y', 'y'] :
                file_directory = self.directory()
                break
            elif ask in ['N','n'] :
                file_directory = default_xls_path
                break
            else :
                print('Y 또는 N으로만 응답해주세요.\n')
                continue
        return file_directory

    # XLS로 변환하여 저장할 경로를 지정 받는 함수 
    def directory(self):

        while True :
            file_directory = input('xls 파일 저장 경로: ')
            if file_directory.strip() == '' : # 아무것도 입력하지 않았을 경우
                print('아무것도 입력하지 않았습니다.\n')
                continue
            if file_directory[-1:-5:-1][::-1] == '.xls' : # 입력값 마지막이 .txt 가 아닐 경우
                print('xls 파일 저장 경로만 입력해주세요.\n')
                continue
            if not os.path.exists(file_directory) : # 입력 받은 경로가 존재하지 않을 경우
                os.makedirs(file_directory)

            if file_directory[-1:-2:-1] != '\\' :
                file_directory = file_directory + '\\'
            break

        return file_directory
    
    # 각 요소의 줄바꿈을 제거해주는 함수
    def line_check(self, lines) :
        sentence_tokenised_text = []
        for i in range(len(lines)):
            try:
                if ( lines[i] == '\n') :
                    continue
                else :
                    sentence_tokenised_text.append(lines[i].strip())
            except IndexError:
                break
        return sentence_tokenised_text

    # 기초적인 전처리를 위한 함수
    def clean_punc(self, text, punct, mapping):
        for p in mapping:
            text = text.replace(p, mapping[p])
        
        for p in punct:
            text = text.replace(p, f' {p} ')
        
        specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
        for s in specials:
            text = text.replace(s, specials[s])
        
        return text.strip()

    # 특수문자를 제거해주는 함수
    def special_characters_remove(self, sentence_tokenised_text) :
        punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
        punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }

        cleaned_corpus = []
        for sent in sentence_tokenised_text:
            cleaned_corpus.append(self.clean_punc(sent, punct, punct_mapping))
        
        return cleaned_corpus


converter = Converter() # 인스턴스 생성
lines = converter.open_txt()
#d = converter.ask_directory()
sentence_tokenised_text = converter.line_check(lines)
cleaned_corpus = converter.special_characters_remove(sentence_tokenised_text)

count = 0
for i in range(len(sentence_tokenised_text)) :
    if(sentence_tokenised_text[i]==cleaned_corpus[i]) :
        continue
    else :
        print(sentence_tokenised_text[i])
        print(cleaned_corpus[i])
        count+=1

print(count)

"""

print(lines)
for i in lines :
    print(i.strip()) # 각 문단 요소의 줄바꿈 문자를 제거하고 출력
"""
"""


def clean_punc(text, punct, mapping):
    for p in mapping:
        text = text.replace(p, mapping[p])
    
    for p in punct:
        text = text.replace(p, f' {p} ')
    
    specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
    for s in specials:
        text = text.replace(s, specials[s])
    
    return text.strip()

def clean_text(texts):
    corpus = []
    for i in range(0, len(texts)):
        review = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\.\:\;\!\-\,\_\~\$\'\"]', '',str(texts[i])) #remove punctuation
        #review = re.sub(r'\d+','', str(texts[i]))# remove number
        review = review.lower() #lower case
        review = re.sub(r'\s+', ' ', review) #remove extra space
        review = re.sub(r'<[^>]+>','',review) #remove Html tags
        review = re.sub(r'\s+', ' ', review) #remove spaces
        review = re.sub(r"^\s+", '', review) #remove space from start
        review = re.sub(r'\s+$', '', review) #remove space from the end
        corpus.append(review)

    return corpus

def open_txt() :
    # 자신의 path 넣기
    file_path = 'C:\\Data_design_for_BERT_QnA_learning\\country\\'
    file_name = input('불러올 txt 이름을 입력하세요: ')

    file = file_path+file_name+'.txt'
    data = open(file, 'r', encoding='utf-8')
    lines = data.readlines()
    return lines

def line_check(lines) :
    sentence_tokenised_text = []
    for i in range(len(lines)):
        try:
            if ( lines[i] == '\n') :
                continue
            else :
                sentence_tokenised_text.append(lines[i].strip())
        except IndexError:
            break
    return sentence_tokenised_text
    
# kss 실행하면 에러 발생
# 이 함수의 기능은 현 코드에서 사용 불필요
def kss_exe(lines) :
    sentence_tokenised_text = []
    for i, line in enumerate(lines):
        print(line)
        line = line.strip()
        what_kss = kss.split_sentences(line)
        print(what_kss, type(what_kss))
        for sent in what_kss:
            sentence_tokenised_text.append(sent.strip())

    return sentence_tokenised_text

# 특수문자를 제거하는 함수
def special_characters_remove(sentence_tokenised_text) :
    punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
    punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }

    cleaned_corpus = []
    for sent in sentence_tokenised_text:
        cleaned_corpus.append(clean_punc(sent, punct, punct_mapping))
    
    return cleaned_corpus

# 맞춤법 검사기 설치 : !pip install git+https://github.com/ssut/py-hanspell.git
# pip install py-hanspell
# 띄어쓰기 검사기 설치 : !pip install git+https://github.com/haven-jeon/PyKoSpacing.git

# 엑셀 형태로 파일에 저장하기 위한 함수
def write_xls(xls_name, num, sents) :
    
    # 자신의 path 넣기
    path = 'C:\\Data_design_for_BERT_QnA_learning\\check\\xlsx\\'
    xls_path = path+xls_name+'.xls'
    sentences = pd.DataFrame()
    sentences['id'] = num
    sentences['sentence'] = sents
    
    # 엑셀 형태로 저장하기
    sentences.to_excel(xls_path , index=False)
    print('xls 파일 저장 경로 : %s' %xls_path)

    print("요청하신 데이터 수집 작업이 정상적으로 완료되었습니다.")
    
# 띄어쓰기 맞춤법 확인하는 함수 생성
def spacing_spell_checker(basic_preprocessed_corpus) :
    spacing = Spacing()
    sents = []
    num = []
    count = 1
    for i in range(len(basic_preprocessed_corpus)) :
        try:
            sent = basic_preprocessed_corpus[i]
            if(i==1) :
                xls_name = sent
            if(i%2==1 and i!=1) :
                spelled_sent = spell_checker.check(sent)
                checked_sent = spelled_sent.checked
                num.append(count)
                count+=1
                sents.append(spacing(checked_sent))
        except IndexError:
            break

    return sents, num, xls_name

# 시스템의 진행여부를 묻는 함수 생성
def continue_system():
    question = False
    ask = input('계속 진행할까요?: [Y/N] ')
    if(ask in ['Y', 'y']):
        print('계속 진행합니다.')
        question = True
    elif(ask in ['N', 'n']) :
        print('시스템을 종료합니다.')
    else :
        print('Y 또는 N으로만 응답해주세요.')

    return question

# 함수를 호출 시켜서 프로그램 실행하기
while True :
    lines = open_txt()
    sentence_tokenised_text = line_check(lines)
    cleaned_corpus = special_characters_remove(sentence_tokenised_text)
    basic_preprocessed_corpus = clean_text(cleaned_corpus) 
    sents, num, xls_name =  spacing_spell_checker(basic_preprocessed_corpus)
    write_xls(xls_name, num, sents)
    go = continue_system()
    if not go :
        break
"""