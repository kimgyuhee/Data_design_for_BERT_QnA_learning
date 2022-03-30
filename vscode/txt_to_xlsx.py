from hanspell import spell_checker
from pykospacing import Spacing
# import xlwt
import pandas as pd
import kss
import re
import os
import openpyxl

# TXT 파일을 XLSX 파일로 변환해주는 클래스 
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
            except OSError :
                print('입출력 오류가 발생했습니다. 다시입력해주세요\n')
                continue
            else :
                break # 올바르게 입력 받았을 경우 반복문을 빠져나간다.
        
        print('{} 파일을 읽어오겠습니다.\n'.format(file_path)) # 입력받은 파일 읽겠다는 안내문 출력
        return lines

    """
    --------- 저장하는 방법 - 2 [아직 코드 작성중] --------- 
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
    """

    # 각 요소의 줄바꿈을 제거해주는 함수
    def line_check(self, lines) :
        sentence_tokenised_text = [] # 수정된 요소를 저장할 변수
        for i in range(len(lines)): # txt 에서 읽어온 각각의 요소 검사
            try:
                if ( lines[i] == '\n') : # 요소가 줄바꿈으로 이루어져 있다면 리스트에 넣지 않기
                    continue
                else :
                    sentence_tokenised_text.append(lines[i].strip()) # 요소의 마지막 줄바꿈 문자를 제거해준 후 리스트에 추가
            except IndexError: # 에러처리 중
                break
        return sentence_tokenised_text # 수정한 요소 리스트 반환

    # 특수문자를 제거하기 쉽게 각 요소 변환하는 함수 - 2
    def clean_punc(self, text, punct, mapping):
        for p in mapping:
            text = text.replace(p, mapping[p])
        
        for p in punct:
            text = text.replace(p, f' {p} ')
        
        specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
        for s in specials:
            text = text.replace(s, specials[s])
        
        return text.strip()

    # 특수문자를 제거하기 쉽게 각 요소 변환하는 함수 - 1
    def special_characters_remove(self, sentence_tokenised_text) :
        # 특수문자 .과 ,는 살려둠
        # punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
        # punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }

        punct = "/-'?!#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
        punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }

        cleaned_corpus = []
        for sent in sentence_tokenised_text:
            cleaned_corpus.append(self.clean_punc(sent, punct, punct_mapping))
        
        return cleaned_corpus

    # 특수문자를 제거하는 함수
    def clean_text(self, texts):
        corpus = []
        for i in range(0, len(texts)):
            # 특수문자 .과 ,는 살려둠
            # review = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\.\:\;\!\-\,\_\~\$\'\"]', '',str(texts[i])) #remove punctuation
            review = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\:\;\!\-\_\~\$\'\"]', '',str(texts[i])) #remove punctuation
            review = review.lower() #lower case
            review = re.sub(r'\s+', ' ', review) #remove extra space
            review = re.sub(r'<[^>]+>','',review) #remove Html tags
            review = re.sub(r'\s+', ' ', review) #remove spaces
            review = re.sub(r"^\s+", '', review) #remove space from start
            review = re.sub(r'\s+$', '', review) #remove space from the end
            corpus.append(review)

        return corpus

    # 띄어쓰기와 맞춤법 확인하는 함수
    def spacing_spell_checker(self, basic_preprocessed_corpus) :
        spacing = Spacing()
        sents = [] # 원하는 문장들을 저장할 리스트 선언
        num = [] # 문장들의 순서를 저장할 변수 선언
        count = 1
        for i in range(len(basic_preprocessed_corpus)) :
            try:
                sent = basic_preprocessed_corpus[i]
                if(i==1) : 
                    xls_name = sent
                # if(i%2==1 and i!=1) :
                if ('번째 문장' in sent) :
                    continue 
                else :
                    spelled_sent = spell_checker.check(sent)
                    checked_sent = spelled_sent.checked
                    num.append(count)
                    count+=1
                    sents.append(spacing(checked_sent))
            except IndexError:
                break

        return sents, num, xls_name

    # 시스템의 진행여부를 묻는 함수 생성
    def continue_system(self):
        question = False
        while True :
            ask = input('계속 진행할까요?: [Y/N] ')
            if(ask in ['Y', 'y']):
                print('계속 진행합니다.\n')
                question = True
                break
            elif(ask in ['N', 'n']) :
                print('시스템을 종료합니다.\n')
                break
            else :
                print('Y 또는 N으로만 응답해주세요.\n')
                continue
        return question

    def write_xls(self, xls_name, num, sents) :
        path = 'C:\\Data_design_for_BERT_QnA_learning\\check\\xlsx\\'
        if not os.path.exists(path) :
            os.makedirs(path)
        xls_path = path+xls_name+'.xlsx'
        sentences = pd.DataFrame()
        sentences['id'] = num
        sentences['sentence'] = sents
        
        # 엑셀 형태로 저장하기
        sentences.to_excel(xls_path , index=False)
        print('xlsx 파일 저장 경로 : %s' %xls_path)

        print("요청하신 데이터 수집 작업이 정상적으로 완료되었습니다.")


# 프로그램 실행
print('-------------------------------------------')
print('txt 내용을 전처리 후 xlsx로 저장하는 프로그램')
print('xlsx 파일 저장 경로 : C:\\Data_design_for_BERT_QnA_learning\\check\\xlsx\\')
print('xlsx 파일 이름은 txt의 주제로 자동으로 정해집니다.')
print('-------------------------------------------')
while True :
    converter = Converter() # 인스턴스 생성
    lines = converter.open_txt()
    # 저장하는 방법 -2 [코드 작성 중] d = converter.ask_directory()
    sentence_tokenised_text = converter.line_check(lines)
    cleaned_corpus = converter.special_characters_remove(sentence_tokenised_text)
    basic_preprocessed_corpus = converter.clean_text(cleaned_corpus)
    sents, num, xls_name = converter.spacing_spell_checker(basic_preprocessed_corpus)
    # 저장하는 방법 -1 [코드 작성 완료]
    converter.write_xls(xls_name, num, sents)
    go = converter.continue_system()
    if not go :
        break