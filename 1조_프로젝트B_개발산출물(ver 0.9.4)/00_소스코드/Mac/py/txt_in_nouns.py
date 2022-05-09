# 기존 txt 파일에서 명사만 추출 txt in nouns 

from konlpy.tag import Okt #형태소 분석 후 명사만 추출하기 위해 
import sys #txt파일 안에 쓰기 위해
import os #220404 추가 #파일 경로 확인을 위해
import datetime # 동일파일이 존재할 경우 날짜와 시간을 추가해주기 위한 모듈 --- 20220411 추가 ---

class NounFilter:       # 학습용 데이터에서 추출한 문장 내용 중 명사만 뽑아주는 클래스 
    '''
    함수명 : __init__(self)
    함수 : 프로그램 시작시 호출되는 함수
    매개변수 : self(NounFilter)
    반환값 : 없음
    '''
    def __init__(self): # NounFilter 프로그램 시작시 호출되는 welcoming 함수 
        print('\n')
        print('='*60)
        print('\t\t명사 추출 프로그램을 시작합니다.')
        print('='*60)
        
    '''
    함수명 : file_dir
    함수 : txt 파일의 저장 경로를 지정 받는 함수 
    매개변수 : self(NounFilter)
    반환값 : file_directory(str) -> txt 파일 저장 경로(str)
    '''        
    # ---------------------  수정사항 1 적용 구간 220404 file_dir 수정 --------------------- 
    def file_dir(self) :                              # 저장할 파일의 폴더 경로를 지정 받는 함수 
        file_directory = '/Users/deankim/Desktop/Developer/Project/wordcloud/noun_text/'
        print('\n')
        print('='*60)
        print('txt 파일을 저장합니다. 저장 경로를 지정해주세요.\n예){}\n0을 입력하여 종료할수있습니다.'.format(file_directory))
        while True :                                  # 파일 경로의 오입력 방지를 위한 반복문
            file_directory = input('파일 저장 경로 : ')
            print('='*60)
            file_directory = file_directory.strip() 
            if file_directory == '':
                print('경로를 입력해주세요.')
                continue
    # --------------------  수정사항 2 적용구간 220407, 0을 입력하여 종료 기능 추가 -------------
            elif file_directory == '0':
#                 print('프로그램을 종료합니다.')
                break
            elif os.path.isdir(file_directory) :        # 입력받은 경로가 존재하는지 확인
                if file_directory[-1] != '/':
                    file_directory = file_directory+'/'
                    return file_directory
                else:
                    return file_directory
            else :                                    # 입력받은 경로가 존재하지 않는다면 다시 입력받기
                print('해당 경로가 존재하지 않습니다. 다시 입력해주세요. \n') 
                continue

            print('='*60)
        return file_directory
    
    '''
    함수명 : file_n
    함수 : txt 파일의 이름을 지정하는 함수 
    매개변수 : self(NounFilter)
    반환값 : file_name (str) -> txt 파일 이름(str)
    '''
        # --------------------- 수정사항 2 적용 구간 220404 file_n 수정 --------------------- 
    def file_n(self) :                                 # 저장할 파일의 이름을 입력
        print('\n')
        print('='*60)
        print('txt 파일의 이름을 지정해주세요.\n예) test\n0을 입력하여 종료할수있습니다.')
        while True :                                   # 파일명 오입력 방지를 위한 반복문
            file_name = input('txt 파일명 지정: ')        # 입력 받은 파일명은 file_name 변수에 담음. 
            if '.' in file_name or '\\' in file_name : # 파일명에 '.' 또는 '\\' 입력 방지 
                print('파일의 이름만 입력해주세요.\n')
                continue
        # --------------------  수정사항 2 적용구간 220407, 0을 입력하여 종료 기능 추가 -------------
            elif file_name == '0':
#                 print('프로그램을 종료합니다.')
                break
    
            elif file_name == '':
                print('파일 이름을 입력해주세요.')
                continue
            else :
        # --------------------  수정사항 3 적용구간 220411, 동일 파일명 존재시 파일명 변경 -------------
                if os.path.isfile(file_directory+file_name+'.txt') :
                    date = datetime.datetime.now()
                    now = datetime.datetime.strftime(date, '%Y년%m월%d일_%H시%M분')
                    file_name = file_name+'_'+now
                    print('동일한 파일이 존재하여 {} 이름으로 저장합니다.\n'.format(file_name))
                break
        print('='*60)
        return file_name                                # 변수 file_name에 파일명을 담아 리턴시킴 
    
    '''
    함수명 : confirming_file_name
    함수 : file_dir(파일 저장 경로), file_n(파일이름)에 입력한 경로대로 txt 파일을 저장하는 함수 
    매개변수 : self(NounFilter)
             file_directory(str) ->  txt 파일 저장 경로
             file_name(str) -> txt 파일 이름
    반환값 : self.txt_file (str) ->  txt 파일 저장 경로 + txt 파일 이름 + .txt
    '''                                                           # 앞서 입력받은 파일 경로와 파일명을 종합하고 사용자에게 안내해주는 함수
    def confirming_file_name(self, file_directory, file_name):  # file_directory: 사용자 지정의 파일 경로, file_name: 사용자 지정의 파일 이름
        print('\n')
        print('='*60)
        print('txt 파일을 아래와 같이 저장합니다.')
        print(f'경로: {file_directory}\n이름: {file_name}')
        print('='*60)
        self.txt_file = file_directory + file_name + '.txt'     # 사용자 지정의 파일 경로 + 파일명 + .txt
        return self.txt_file                                    # 파일 경로와 파일명 그리고 확장명이 더해진것을 txt_file 변수에 담음

    '''
    함수명 : open_raw_data
    함수 : 명사를 추출할 txt 파일의 경로를 입력받는 함수 
    매개변수 : self(NounFilter)
    반환값 : self.raw_data (str) ->  명사를 추출할 txt 파일 경로
    '''   
    def open_raw_data(self):                           # 명사만 추출할 txt 파일을 불러오는 함수 
        self.raw_data = '/Users/deankim/Desktop/Developer/Project/clean_text/F_Korea.txt'
        print('\n')
        print('='*60)
        print('명사를 추출할 데이터 파일의 경로를 입력해주세요.\n예){}\n0을 입력하여 종료할수있습니다.'.format(self.raw_data))
        while True :                                   # 불러올 파일의 위치 오입력 방지를 위한 반복문
            self.raw_data = input('데이터 파일 경로: ')    # txt 파일의 경로를 raw_data 변수에 담기
            if self.raw_data == '0':
#                 print('프로그램을 종료합니다.')
                break
    
            if os.path.isfile(self.raw_data) :          # raw_data에 담은 파일 경로가 존재하는지 확인
                break
            else :
                print('해당 경로에 txt 파일이 존재하지 않습니다. 다시 입력해주세요.')
                continue
        # --------------------  수정사항 2 적용구간 220407, 0을 입력하여 종료 기능 추가 -------------
        print('='*60)
        return self.raw_data

    '''
    함수명 : read_file
    함수 : 명사를 추출할 txt파일을 읽어주는 함수
    매개변수 : self(NounFilter)
             raw_data(str) -> 명사를 추출할 txt 파일 경로
    반환값 : self.text (str) ->  읽어 온 명사를 추출할 txt파일
    '''     
                                           # 명사만 추출할 txt 파일을 읽어주는 함수 
    def read_file(self, raw_data):         # raw_data: txt 파일의 경로를 담고있음 
        with open(self.raw_data, 'r', encoding='utf-8') as self.f:
            self.text = self.f.read()      # 읽어온 txt 파일은 text 변수에 담음
        return self.text
    
    '''
    함수명 : write_file
    함수 : 새로운 txt 파일에 형태소 분석 후 추출한 명사만 담아주는 함수
    매개변수 : self(NounFilter)
             text(str) -> 읽어 온 명사를 추출할 txt파일
             txt_file(str) -> txt 파일 저장 경로 + txt 파일 이름 + .txt
    반환값 : 없음
    '''     
                                           # 새로운 txt 파일에 형태소 분석 후 명사만 담아줄 함수
    def write_file(self, text, txt_file):  # text: 말뭉치가 담긴 text 파일(읽기모드), txt_file: 파일경로와 파일명을 담고있는 함수
        self.okt = Okt()                   # 형태소 분석기인 Okt를 okt 변수에 담음 
        self.noun = self.okt.nouns(text)   # text 변수로 불러온 데이터에서 명사만 추출 text: 말뭉치가 담긴 text 파일(읽기모드)

        self.orig_stdout = sys.stdout      # 화면 출력 X, 문서에 출력되는 구간 시작 
        with open(txt_file, 'w', encoding='utf-8') as self.file:
            sys.stdout = self.file

            for i in self.noun:               # noun: 명사 정보만 담고있는 변수 
                if len(i) > 1 and i != '문장': # 글의 길이가 1자 이하이거나 txt 문서에 '문장'으로 구분지어둔 단어는 생략
                    print(i)
                    
            sys.stdout = self.orig_stdout     # 화면 출력 X, 문서 출력 구간 종료 
        print('\n')    
        print('='*60)
        print('명사 추출이 완료되었으며 파일이 정상적으로 저장되었습니다.')
        print('='*60)
        

noun_f = NounFilter()  
file_directory = noun_f.file_dir()

if file_directory == '0':
    print('\n프로그램을 종료합니다.')
else:
    file_name = noun_f.file_n()        
    if file_name == '0':
        print('\n프로그램을 종료합니다.')
    else:
        txt_file = noun_f.confirming_file_name(file_directory, file_name) 
        raw_data = noun_f.open_raw_data()  
        if raw_data == '0':
            print('\n프로그램을 종료합니다.')
        else:
            text = noun_f.read_file(raw_data) 
            noun_f.write_file(text, txt_file)  
