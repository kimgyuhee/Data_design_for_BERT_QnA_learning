import pandas as pd # xlsx 파일을 읽기 위한 모듈
import os.path # 파일의 경로를 불러와 확인하기 위한 모듈
from tqdm._tqdm import tqdm # 작업진행률 표시 모듈 
import sys # 프로그램을 중간에 종료하기 위한 모듈
import datetime # 동일한 파일명이 존재할 경우 날짜데이터를 추가하기 위한 모듈
# pip install openpyxl -> 설치 해야함
# ------------------------------------ 20220408 변수명 수정1 [변수명 -> self.변수명]------------------------------------
# xlsx에 저장된 문장 합쳐주는 클래스
class CombineSentence() :
    def __init__(self): # CombineSentence 프로그램 시작시 호출되는 welcoming 함수 
        print('\n')
        print('='*60)
        print('\t\t문장 통합 프로그램을 시작합니다.')
        print('='*60)
    '''
    함수명 : input_xlsx
    함수 : xlsx 파일들이 존재하는 폴더 불러오는 함수
    매겨변수 : self(CombineSentence)
    반환값 : self.path(str) -> xlsx 파일들이 존재하는 경로 데이터(str)
    '''
    def input_xlsx(self) :
        print('\n')
        print('='*60)
        while True :                                                            # 컴퓨터에 존재하는 경로를 입력할 때까지 돌아가는 반복문
            self.path = input('xlsx 파일들이 존재하는 폴더를 입력해주세요.\n기본경로: /Users/deankim/Desktop/xlsx\n경로입력: ')
            print('='*60)
            self.path = self.path.strip()                                       # 양 옆 공백제거
            if not os.path.isdir(self.path) :                                   # 만약 입력받은 경로가 현재 컴퓨터에 존재하지 않으면
                if self.path == '0' :                                           # 입력 값이 0일 경우 종료                              
                    #sys.exit()
                    return ''                                                   # 프로그램 종료
                print('해당 파일이 존재하지 않습니다. 다시 입력해주세요.')       # 경로 다시 입력받기
                print('0을 입력하여 종료할수있습니다.\n')
                continue
            else :                                                              # 입력 받은 경로가 존재한다면
                break                                                           # 반복문 탈출
        return self.path                                                        # 입력받은 xlsx 파일들이 존재하는 경로 리턴

    '''
    함수명 : output_xlsx_list
    함수 : xlsx 리스트 목록을 보여주기 위한 함수
    매겨변수 : self(CombineSentence), dir_path(str) -> xlsx 파일들이 존재하는 경로 데이터(str)
    반환값 : self.text(str), self.xlsx_list(list) -> xlsx 파일들을 메뉴화 시킨 데이터(str), xlsx 파일들만 담긴 데이터(list)
    '''
    def output_xlsx_list(self, dir_path) :
        self.xlsx_list = []                                                      # 엑셀 파일들만 저장하기 위한 리스트 생성
        self.files = os.listdir(dir_path)                                        # 해당경로에 존재하는 파일들을 불러와서 변수에 저장
      #----------수정 1 : if '.xlsx' or 'xls' in i --> if ('.xlsx' in i) or ('.xls' in i ) 로 수정 (20220406)----------
        for i in self.files :                                                    # 해당 경로에 있는 파일들을 하나씩 확인하면서
            if ('.xlsx' in i) or ('.xls' in i ) :                                # 확장자가 xlsx, xls 이면
                self.value = i.split('.')[0]                                     # 파일 이름 + 확장자 를 분리해 파일이름만 value 변수에 저장
                self.xlsx_list.append(self.value)                                # 파일이름을 엑셀 파일 리스트에 추가

        self.text = '--'*44
        for i in range(len(self.xlsx_list)) :                                    # 엑셀 파일들의 목록을 출력하기 위한 반복문
            if i%4 == 0 :                                                        # 4열로 목록을 보여주기 위해 조건문 생성
                self.text = self.text +'\n'                                      # 위에 4번째가 넘어가면 다음 행에 엑셀 파일 이름 보여주기 
            self.text = self.text + str(i) + '. '+ self.xlsx_list[i]+' \t\t'     # 엑셀 파일번호 + 엑셀 파일이름

        self.text = self.text+'\n'+'--'*44+'\n'
        return self.text, self.xlsx_list                                         # 엑셀 파일리스트 출력문(사용자에게 보여질 print문), 엑셀 파일리스트 목록 리턴

    '''
    함수명 : choice_country
    함수 : 경로에 존재하는 xlsx 파일 중 하나를 선택하는 함수
    매겨변수 : self(CombineSentence), text(str), xlsx_list(list) -> xlsx 파일들을 메뉴화 시킨 데이터(str),  xlsx 파일들만 담긴 데이터(list)
    반환값 : self.choice(int), xlsx_list[self.choice](str) -> 메뉴에서 선택된 번호 데이터(int), 메뉴에서 선택된 번호의 값, 즉 파일 이름 데이터(str)
    '''
    def choice_country(self,text, xlsx_list) :
        print('\n')
        print('='*60)
        while True :                                                              # 엑셀 파일 리스트에 존재하는 숫자를 입력할 때까지 돌아가는 반복문
            print('\n')
            self.choice = input(text+'\n문장을 합치기 원하는 나라의 숫자를 입력해주세요 -> ')
            if not self.choice.isdecimal() :                                      # 숫자를 입력하지 않았을 경우 - 예외처리
                print('0~{}사이의 숫자를 입력해주세요.\n숫자 입력: '.format(len(xlsx_list)-1))
                continue
            else :                                                                # 숫자를 입력했을 경우
                self.choice = int(self.choice) 
                if self.choice < 0 or self.choice > len(xlsx_list)-1 :            # 숫자 범위를 벗어난 숫자를 입력받았을 때
      #----------수정 2 : print('0~{}사이의 숫자를 입력해주세요.\n'.format(len(xlsx_list))) --> format(len(xlsx_list)-1)) 로 수정 (20220406)----------
                    print('0~{}사이의 숫자를 입력해주세요.\n'.format(len(xlsx_list)-1))
                    continue
                else :
                    break

        return self.choice, xlsx_list[self.choice]

    '''
    함수명 : open_xlsx
    함수 : 선택된 xlsx 파일을 열어서 문장을 합쳐주는 함수
    매겨변수 : self(CombineSentence), country(str), path(str) -> 파일 이름 데이터(str), 파일이 존재하는 경로 데이터(str)
    반환값 : self.mystr(str), self.txt_name(str) -> 이어진 문장 데이터(str), 자동으로 정해진 txt 파일명(str)
    '''
    def open_xlsx(self, country, path) :
        print('\n')
        print('='*60)
        # 윈도우 사용자용
        # self.df = pd.read_excel(path+'\\'+country+'.xlsx')                           # 선택한 나라의 엑셀파일 열기
        # 맥 사용자용
        self.df = pd.read_excel(path+'/'+country+'.xlsx')                             # 선택한 나라의 엑셀파일 열기
        # sent_count = len(df.index) ----------------------- 20220408 불필요한 코드 주석처리 ------------------------------------------
      
        self.mystr = ''                                                               # 문장을 이어줄 변수 선언
        try :
            self.w = self.df['sentence']                                              # sentence 열을 불러와 w변수에 저장
        except KeyError :                                                             # 우리가 사용할 xlsx 파일 말고 다른 xlsx 파일을 열었을 경우 - 예외처리
            print('xlsx 파일의 내용이 현 프로그램과 관련이 없습니다.')
            return self.mystr, 'no'                                                   # 개발자가 자료형에 맞게 알아서 반환값 정함
        else :
            for i in tqdm(range(len(self.w))):                                        # 각 문장을 이어서 mystr에 붙이기 위한 반복문 생성
                if i == 0 :                                                           # 모든 나라의 첫번째 문장은 나라 이름이어서 
                    self.txt_name = self.w[i]                                         # txt로 저장할 때 txt 이름을 나라이름으로 해주기 위해 txt_name 변수에 저장 
                else :                                                                # 첫번째 문장 이외는 문장이여서
                    self.mystr += str(self.w[i]) + '\n'                               # mystr에 이어서 붙어주기

        print(self.mystr)                                                             # 사용자게에 이어진 문장 보여주기

        return self.mystr, self.txt_name                                              # 이어진 문장과 txt 파일의 이름 리턴

    '''
    함수명 : write_txt
    함수 : 합쳐진 문장을 개발자가 정해준 경로에 txt로 저장해주는 함수 
    매겨변수 : self(CombineSentence), text(str), txt_name(str) -> 이어진 문장 데이터(str), 자동으로 정해진 txt 파일명(str)
    반환값 : 없음
    '''
    def write_txt(self, text, txt_name) :
        print('\n')
        print('='*60)
        # 윈도우 사용자용
        # self.dir_path = 'D:\\2th_project\\check\\'                                    # 개발자가 정한 파일 경로
        # 맥 사용자용
        self.dir_path = '/Users/deankim/Desktop/Developer/'                           # 개발자가 정한 파일 경로
        if not os.path.isdir(self.dir_path) :                                         # 각 사용자에게 그 경로가 존재하지 않으면 
            os.makedirs(self.dir_path)                                                # 경로를 만들어준다.
        file_path = self.dir_path+txt_name+'.txt'                                     # txt 파일을 저장할 경로 
        # ------------------ 20220411 코드 추가 동일한 파일명일 경우 ---------------------
        if os.path.isfile(file_path) :
            date = datetime.datetime.now()
            now = datetime.datetime.strftime(date, '%Y년%m월%d일_%H시%M분')
            file_path = self.dir_path+txt_name+'_'+now+'.txt'
            print('동일한 파일이 존재하여 파밀명에 날짜데이터를 추가하여 저장합니다.\n')
        file = open(file_path, 'w', encoding='utf-8');                                # 파일을 열어서
        file.writelines(text)                                                         # 이어진 문장 써주기
        print()
        print('{} 문장들이 합쳐진 내용이 {} 파일로 저장되었습니다.\n'.format(txt_name, file_path))
        print('='*60)
        file.close()

    '''
    함수명 : continue_sys
    함수 : 프로그램을 계속 진행할지 묻는 함수
    매겨변수 : self(CombineSentence)
    반환값 : True/Faslse(bool) -> 계속 진행할 여부 데이터(bool)
    '''
    def continue_sys(self) :
        print('\n')
        print('='*60)
        while True : 
            answer = input('프로그램을 계속 실행하시겠습니까? [Y, N] ')
            print('='*60)
            answer = answer.strip()
            if answer.upper() == 'Y' :                                                # 대소문자 상관없이 y 입력시
                return True                                                           # True 반환
            elif answer.upper() == 'N' :                                              # 대소문자 상관없이 n 입력시
                return False                                                          # False 반환
            else :                                                                    # Y와 N 이외의 것들을 입력했을 시 다시 입력받기
                print('Y와 N 중에 하나를 입력해주세요.\n')
                continue
    
    # -------------------------------------- 20220408 함수 추가 ----------------------------------------------
    '''
    함수명 : sys_run
    함수 : 프로그램을 실행하기 위한 함수
    매겨변수 : self(CombineSentence)
    반환값 : 없음
    '''
    def sys_run(self) :
        while True :
            self.path = self.input_xlsx()
            if self.path == '' :
                print('프로그램을 종료합니다.')
                break
            self.text, self.xlsx_list = self.output_xlsx_list(self.path)
            if len(self.xlsx_list) == 0 :                                             # 입력 경로에 엑셀 파일이 존재하지 않았을 때
                print('{} 폴더에 xlsx 파일이 존재하지 않습니다.'.format(self.path))     # 존재하지 않다고 사용자에게 알린 후 프로그램 반복
            else :
                self.num, self.country = self.choice_country(self.text, self.xlsx_list)
                self.text, self.txt_name = self.open_xlsx(self.country, self.path)
                if not self.text == '' :                                              # xlsx 파일의 내용이 주제에 알맞을 때!
                    self.write_txt(self.text, self.txt_name)                          # txt 파일에 적어준다.
            
            if self.continue_sys() :
                self.sys_run() 
            else :
                print('프로그램을 종료합니다. \n')
                break

combineSentence =  CombineSentence()
combineSentence.sys_run()