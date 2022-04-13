import json # json 파일을 읽고 쓰기 위한 모듈
import sys # 시스템 관련 함수와 파라미터를 포함하는 모듈 (txt 파일에 값을 쓰기 위한 모듈)
import os.path # 파일의 경로를 불러와 확인하기 위한 모듈
import datetime # 동일파일이 존재할 경우 날짜와 시간을 추가해주기 위한 모듈 --- 20220411 추가 ---

# JSON 파일을 TXT 파일로 변환해주는 클래스 
class Converter:
    def __init__(self): # JSON TO TXT 프로그램 시작시 호출되는 welcoming 함수 
        print('\n')
        print('='*60)
        print('\t\t문장 추출 프로그램을 시작합니다.')
        print('='*60)
    '''
    함수명 : open_json
    설명 : JSON 파일의 저장 경로를 지정 받는 함수
    매개변수 : self(Converter)
    반환값 : json_data(dict), sentence(list) -> json의 모든 데이터(dict),  json 데이터 중 sentencce 값만 저장된 데이터(list)
    '''
    # <class '__main__.Converter'> 의 의미는?
    # __main__은 '현재 실행 중인 파일'을 의미하므로, 위 출력 결과는 '이 스크립트에서 정의된, 현재 실행중인 Converter 클래스'를 의미한다고 생각하면 된다.
    def open_json(self):
        print('\n')
        print('='*60)
        while(True): # 파일이 경로에 없는 경우를 방지합니다. 
            self.file_path = input('불러올 json 파일의 경로를 지정해주세요.\n0을 입력하여 종료할수있습니다.\n예) D:\\2th_project\\check\\war2.json \njson 파일 경로: ')                                                     
            print('='*60)
            self.file_path = self.file_path.strip()
            if os.path.isfile(self.file_path):
                print('json 파일의 경로가 확인되었습니다.')
                break
            else:
                # -------------------------------------- 20220407 예외처리 추가1 ------------------------------------------------------
                if self.file_path == '0' :
                    # sys.exit() # 종료방법1
                    return {}, [] # 종료방법2
                print('json 파일이 경로에 없습니다.')
                print('0을 입력하여 종료할수있습니다.\n')
                continue
                # -------------------------------------------------------------------------------------------------------------------
        self.file_path[0]

        with open(self.file_path, 'r', encoding='UTF-8') as f:      # 사용자 지정의 JSON파일을 읽기 모드로 불러옵니다. 
            self.json_data = json.loads(f.read())                 
            self.sentences = self.json_data['sentence']             # JSON 속성중 sentence라고 지정된 속성만 불러올수있게 sentences 변수로 지정합니다. 

        return self.json_data, self.sentences                       # json_data: 읽어온 json 데이터를 저장한 변수, sentences: json 데이터중 sentence 값만 저장된 변수
        
    '''
    함수명 : directory
    설명 : TXT로 변환하여 저장할 경로를 지정 받는 함수
    매개변수 : self(Converter)
    반환값 : self.file_directory(str) -> txt 파일 저장 경로 데이터(str)
    '''
    def directory(self):
        print('\n')
        print('='*60)
        while(True):
            self.file_directory = input('txt 파일로 저장할 경로를 입력해주세요.\n0을 입력하여 종료할수있습니다.\n예) D:\\2th_project\\check\\ \ntxt 파일 저장 경로: ')
            print('='*60)
            self.file_directory = self.file_directory.strip()
            if os.path.isdir(self.file_directory):
                break
            else:
                # -------------------------------------- 20220407 예외처리 추가2 ------------------------------------------------------
                if self.file_directory == '0':
                    # sys.exit() # 종료방법1
                    return "" # 종료방법2
                print('폴더의 경로가 존재하지 않습니다.')
                print('0을 입력하여 종료할수있습니다.\n')
                continue

        
        if not self.file_path[len(self.file_path)-1] == '\\' :
            self.file_directory = self.file_directory+'\\'
                # ------------------------------------------------------------------------------------------------------------------
        return self.file_directory 

    '''
    함수명 : txt_name
    설명 : txt의 파일명을 지정 받는 함수
    매개변수 : self(Converter)
    반환값 : self.file_name(str) -> 저장될 txt 파일의 이름 데이터(str)
    '''
    def txt_name(self, txt_path):
        print('\n')
        print('='*60)   
        while(True):
            self.name = input('txt 파일명(확장자명은 제외해주세요): ')
            self.name = self.name.strip()
            if self.name == '0' :
                return ''
            if '.' in self.name:                                               # 파일명에 확장자를 입력하는것을 방지 
                print('특수문자나 확장자를 제외한 파일명만 입력해주세요.\n예) Turkey\n파일명 입력: ')
                print('0을 입력하여 종료할수있습니다.\n')
                continue
            if self.name == '':                                                # 파일명 미입력을 방지 
                print('파일명을 입력해주세요.\n')
                print('0을 입력하여 종료할수있습니다.\n')
                continue
            else:                                                              # 파일명이 정상 입력된 경우
                 # --------------------------------- 20220411 파일명 같을 경우 수정하기 ----------------------------------------
                if os.path.isfile(txt_path+self.name+'.txt') :
                    #print(txt_path+self.name)
                    date = datetime.datetime.now()
                    now = datetime.datetime.strftime(date, '%Y년%m월%d일_%H시%M분')
                    self.name = self.name+'_'+now
                    print('동일한 파일이 존재하여 {} 이름으로 저장합니다.\n'.format(self.name))
                break
        self.file_name = self.name + '.txt'                                    # 사용자 편의를 위하여 입력 받은 TXT 파일에 자동으로 확장자를 써줍니다. 

        return self.file_name 

    '''
    함수명 : writing_txt_down_to
    설명 : JSON 파일을 불러와 txt로 써주는 함수
    매개변수 : self(Converter), file_directory(str), file_name(str), sentences(list) 
    -> txt 파일 저장 경로 데이터(str), txt 파일 저장 이름 데이터(str), 불러올 json데이터의 문장 데이터(list)
    반환값 : 없음
    '''
    def writing_txt_down_to(self, file_directory,file_name, sentences):           
        num = 0                                                                    # 총 출력된 문장의 개수를 카운팅 하기 위함입니다. 
        count = len(self.sentences)                                                # JSON 파일의 문장 개수를 저장할 함수이며 반복문에 사용됩니다.  
        orig_stdout = sys.stdout                                             
        f_txt = open(self.file_directory+self.file_name, 'w', encoding='utf-8')   
        sys.stdout = f_txt
        domain = []                                                                # JSON이 가지고있는 title 정보를 담을 변수입니다. 

        print('도메인: {}'.format(self.sentences[0]['text']))                        # TXT 파일내 가장 첫번째 줄에 해당하며 변환한 도메인이 어떤것인지 알려주기 위함입니다. 
        print('\n')

        for i in range(count):
            if(i==0):                                                               # 가장 첫번째 정보는 타이틀이므로 TXT파일에 쓰기를 생략합니다. 
                domain.append(self.sentences[i]['text'])                            # append 시킨 타이틀 정보는 아래 시스템 출력문에서 사용자에게 보여줄 용도입니다. 
                pass
            else:
                print(self.sentences[i]['id'],'번째 문장:',self.sentences[i]['text']) # 각 고유 id와 문장의 text만을 JSON에서 추출합니다.                          
                print('\n')
                num += 1                                                            # 문장이 성공적으로 출력되었으며 1씩 증가시켜 출력된 문장 수를 합산합니다. 
            
        sys.stdout = orig_stdout                                                    # txt 파일에 쓰는것은 여기까지로 합니다. 
        f_txt.close()                                                               # 파일 닫기 
       
        print(f'도메인: {domain}\n총 {num}개의 문장이 출력되었고 {self.file_directory} 경로로 저장되었습니다.')
        print('='*60)
        # return sr

    '''
    함수명 : continue_system
    설명 : 프로그램을 계속 진행할지 여부를 묻는 함수
    매개변수 : self(Converter)
    반환값 : 없음
    '''
    def continue_system(self):
        while(True):
            print('\n')
            print('='*60)
            self.ask = input('계속 진행할까요? [Y/N] : ')
            print('='*60)
            if self.ask.upper() == 'Y':
                print('계속 진행합니다.\n')
                self.result = True
                break
            elif self.ask.upper() == 'N':
                print('프로그램을 종료합니다.')
                self.result = False
                break
            else:
                print('Y 또는 N으로만 응답해주세요.\n')
                continue
        return self.result

# 프로그램 실행코드
while True :
    converter = Converter()
    json_data, sentences = converter.open_json()
    if sentences == [] :
        print('프로그램을 종료합니다')
        break
    file_directory = converter.directory()
    if file_directory == '' :
        print('프로그램을 종료합니다')
        break
    file_name = converter.txt_name(file_directory)
    if file_name == '' :
        print('프로그램을 종료합니다.')
        break
    converter.writing_txt_down_to(file_directory, file_name, sentences)
    if converter.continue_system() :
        continue
    else :
        break