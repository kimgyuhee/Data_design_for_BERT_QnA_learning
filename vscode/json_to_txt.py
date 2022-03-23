import json
import sys 

# JSON 파일을 TXT 파일로 변환해주는 클래스 
class Converter:
    def open_json(self):                                                # JSON 파일의 저장 경로를 지정 받는 함수 

        while True :                                                    # 올바른 형식으로 입력받을 때까지 돌아가도록 반복문 생성
            self.file_path = input('json 파일 경로: ')                  # file_path = '/Users/deankim/Desktop/Developer/Project/war1.json'
            if self.file_path == '' :                                   # 파일명을 쓰지 않고 엔터 누르는 경우를 방지합니다.
                print('아무것도 입력하지 않았습니다. 다시 입력해주세요\n')
                continue
            if self.file_path[-1:-6:-1][::-1] != '.json' :              # 파일명 확장자가 json이 아니면 입력을 반복합니다.
                print('json 파일을 찾아 경로를 입력해주세요.\n')
                continue
            try :
                with open(self.file_path, 'r', encoding='UTF-8') as f:          
                    # 사용자 지정의 JSON파일을 읽기 모드로 불러옵니다. 프로그램이 끝나면 자동으로 close 해준다.
                    self.json_data = json.loads(f.read())                 
                    self.sentences = self.json_data['sentence']         # JSON 속성중 sentence라고 지정된 속성만 불러올수있게 sentences 변수로 지정합니다.
            except FileNotFoundError :
                print('json 파일 경로가 존재하지 않습니다.\n')             # 입력받은 경로가 존재하지 않았을 경우 다시 입력받기
                continue
            else :
                break                    
        return self.json_data, self.sentences 
        
    def directory(self):                                            # TXT로 변환하여 저장할 경로를 지정 받는 함수 
        self.file_directory = input('TXT 파일 저장 경로: ')
        try:                                                        # 사용자 지정의 TXT 파일 경로를 지정받습니다.
            self.file_directory[0]                                  # 파일 경로를 지정하지 않는 경우를 시험합니다. 
        except IndexError:                                          # 파일 경로 지정이 되지 않았으므로 directory 함수를 재 호출시킵니다. 
            print('txt 파일로 저장할 경로를 입력해주세요.')
            converter.directory()
        return self.file_directory 

    def txt_name(self):                                                           # TXT의 파일명을 지정 받는 함수
        self.name = input('TXT 파일명(확장자명은 제외해주세요): ')
        try:                                                                          # TXT 파일명을 지정하지 않고 엔터를 누른 경우를 시험합니다. 
            self.name[0]
        except IndexError:                                                        # 파일명을 지정하지 않았으므로 txt_name 함수를 재 호출시킵니다.
            print('파일명을 입력해주세요.')
            converter.txt_name()
        self.file_name = self.name + '.txt'                                       # 사용자 편의를 위하여 입력 받은 TXT 파일에 자동으로 확장자를 써줍니다. 
        return self.file_name 

    def writing_txt_down_to(self, file_directory, file_name, sentences):           # JSON파일을 불러오며 txt로 변환하여 저장해주는 함수
        num = 0                                                                    # 총 출력된 문장의 개수를 카운팅 하기 위함입니다. 
        count = len(self.sentences)                                                # JSON 파일의 문장 개수를 저장할 함수이며 반복문에 사용됩니다.  
        orig_stdout = sys.stdout                                                   # 화면에 출력되지 않고 TXT 파일로 직접 쓰기 위함입니다. 
        f_txt = open(self.file_directory+self.file_name, 'w', encoding='utf-8')    # 앞서 사용자 지정의 파일 경로로 TXT 파일을 씁니다. 
        sys.stdout = f_txt
        # sr = []                                                                  # 출력한 문장을 담을 변수입니다. 
        domain = []                                                                # JSON이 가지고있는 title 정보를 담을 변수입니다. 

        print('도메인: {}'.format(self.sentences[0]['text']))                        # TXT 파일내 가장 첫번째 줄에 해당하며 변환한 도메인이 어떤것인지 알려주기 위함입니다. 
        print('\n')

        for i in range(count):
            if(i==0):                                                               # 가장 첫번째 정보는 타이틀이므로 TXT파일에 쓰기를 생략합니다. 
                domain.append(self.sentences[i]['text'])                            # append 시킨 타이틀 정보는 아래 시스템 출력문에서 사용자에게 보여줄 용도입니다. 
                pass
            else:
                print(self.sentences[i]['id'],'번째 문장:',self.sentences[i]['text']) # 각 고유 id와 문장의 text만을 JSON에서 추출합니다. 
                # sr.append(self.sentences[i]['text'])                                
                print('\n')
                num += 1                                                            # 문장이 성공적으로 출력되었으며 1씩 증가시켜 출력된 문장 수를 합산합니다. 
            
        sys.stdout = orig_stdout                                                    # txt 파일에 쓰는것은 여기까지로 합니다. 
        f_txt.close()                                                               # 파일 닫기 
        
        print(f'도메인: {domain}\n총 {num}개의 문장이 출력되었고 {self.file_directory}경로로 저장되었습니다.')
        # return sr

    def continue_system(self):
        while(True):
            self.ask = input('계속 진행할까요?: [Y/N]')
            if(self.ask in ['Y', 'y']):
                print('계속 진행합니다.')
                while(True):
                    converter = Converter()
                    json_data, sentences = converter.open_json()
                    file_directory = converter.directory()
                    file_name = converter.txt_name()
                    converter.writing_txt_down_to(file_directory, file_name, sentences)
                    self.ask = input('계속 진행할까요? [Y/N]')
                    if(self.ask in ['N', 'n']):
                        print('시스템을 종료합니다.')
                        return False
                    elif(self.ask in ['Y', 'y']):
                        print('JSON 파일 변환을 계속 진행합니다.')
                        continue
                    else:
                        print('Y 또는 N으로만 응답해주세요.')
                        continue
            elif(self.ask in ['N', 'n']):
                print('시스템을 종료합니다.')
                break
            else:
                print('Y 또는 N으로만 응답해주세요.')
                continue

converter = Converter()
json_data, sentences = converter.open_json()
file_directory = converter.directory()
file_name = converter.txt_name()
converter.writing_txt_down_to(file_directory, file_name, sentences)
converter.continue_system()


