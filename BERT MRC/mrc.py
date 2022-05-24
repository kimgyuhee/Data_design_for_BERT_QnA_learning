import os
import pandas as pd
import json
from collections import OrderedDict
import datetime
import requests
import openpyxl

class Combine_sentence :
    
    def input_xlsx_path(self) :
        print('='*70)
        current_path = os.getcwd()
        self.xlsx_path = current_path+'\\country_data\\xlsx'
        
        print('나라 데이터가 존재하는 경로는 '+self.xlsx_path+" 입니다.")
            
        self.country_menu()

    # 폴더에 존재하는 엑셀 파일 리스트 메뉴
    def country_menu(self) :
        print('='*70)
        path_list = os.listdir(self.xlsx_path)
        self.text = ''
        self.country_list = []
        for i in path_list :
            if '.xlsx' in i or '.xls' in i :
                self.country = i.split('.')[0]
                self.country_list.append(self.country)

        for i in range(len(self.country_list)) :
            if(i%4 == 0) :
                self.text = self.text+'\n'
            self.text = self.text+str(i)+'. '+self.country_list[i]+'  \t\t'
            
        print(self.text)
        
    def input_country(self) :
        print('='*70)
        while True :
            num = input('나라번호 입력 : ')
            
            if num == '-1' :
                self.country = ''
                break
            
            if num.isdecimal() :
                num = int(num)
                if num >=0 and num < len(self.country_list) :
                    print('*** {}번 {} 나라 선택 ***'.format(num, self.country_list[num]))
                    self.country = self.country_list[num]
                    break
                else :
                    print('-1을 입력하면 종료할 수 있습니다.\n')
            else :
                print('-1을 입력하면 종료할 수 있습니다.\n')
     
        return self.country
    
    
    def open_xlsx(self, country) :
        print('='*70)
        self.questions = []
        self.mystr = ''
        path = self.xlsx_path+'\\'+country+'.xlsx'
        print(path)

        
        try :
            df1 = pd.read_excel(path, sheet_name = '질문지')
            df2 = pd.read_excel(path, sheet_name = '질문지') # 20220523 코드 추가
            # sent_count = len(df.index) 코드 삭제
            w = df1['sentence']
            data_id = df2['id'] # 20220523 코드 추가

        except KeyError :
            print('xlsx 파일의 내용이 현 프로그램과 관련이 없습니다.')
            return False
        except ValueError:
            print('xlsx 파일의 내용이 현 프로그램과 관련이 없습니다.')
            return False
        else :
            for i in range(len(w)) :
                if '?' in str(w[i]) and ('질문' in str(data_id[i]) or 'Q' in str(data_id[i])):
                    self.questions.append(str(w[i]))
                # else : 20220523 코드 제거
                #     self.mystr += str(w[i]) + '\n'
                elif isinstance(data_id[i], float) :
                    if data_id[i]%1 == 0.0 :
                        self.mystr += str(w[i]) + '\n'
                        continue
                elif isinstance(data_id[i], int) :
                    if data_id[i]%1 == 0 :
                        self.mystr += str(w[i]) + '\n'
                        continue
    
        return True
    
    def write_json(self, file_data) :
        self.json_path = os.getcwd()+'\\xlsx\\'
        if not os.path.isdir(self.json_path) :
            print('{}경로가 존재하지 않아서 폴더를 생성합니다.\n'.format(self.json_path))
            os.makedirs(self.json_path)
            
        path =  self.json_path+self.country + '.json'
        if os.path.isfile(path) :
            date = datetime.datetime.now()
            now = datetime.datetime.strftime(date, '%Y년%m월%d일_%H시%M분')
            self.name = self.country+'_'+now
            print('동일한 파일이 존재하여 {} 이름으로 저장합니다.\n'.format(self.name))
            path =  self.json_path+self.name + '.json'
            
        with open(path, 'w', encoding='utf-8') as make_file :
            json.dump(file_data, make_file, ensure_ascii=False, indent='\t')
            
        print('{} 에 json 파일이 저장했습니다.\n'.format(path))
    
    def json_set(self) :
        file_data = OrderedDict()
        file_data['context'] = self.mystr
        file_data['question'] = self.questions
        
        return file_data
        
    
    def mrc_run(self, input_data) :
        print(self.mystr)
        print('='*70)
        self.positions = []
        self.answers = []
        for i in range(len(self.questions)) :
            print(self.questions[i])
            input_data = { 'context' : [self.mystr], 'question' : [self.questions[i]]}
            response = requests.post('http://192.168.0.132:8888/mrc', json = input_data)
            response_data = json.loads(response.text)
            # print(response)
            # print(response.text)
            print(response_data)
            print(response_data[0].get('position'))
            self.answers.append(response_data[0].get('answer'))
            self.positions.append(response_data[0].get('position'))
        
        self.write_xls()
        
            
    def write_xls(self) :
        x_path = os.getcwd()+'\\xlsx\\'
        if not os.path.isdir(x_path) :
            print('{}경로가 존재하지 않아서 폴더를 생성합니다.\n'.format(x_path))
            os.makedirs(x_path)
            
        path =  x_path+self.country + '.xlsx'
        if os.path.isfile(path) :
            date = datetime.datetime.now()
            now = datetime.datetime.strftime(date, '%Y년%m월%d일_%H시%M분')
            self.name = self.country+'_'+now
            print('동일한 파일이 존재하여 {} 이름으로 저장합니다.\n'.format(self.name))
            path =  self.json_path+self.name + '.xlsx'
            
        country = pd.DataFrame()
        country['질문']=pd.Series(self.questions)
        country['답']=pd.Series(self.answers)
        country['위치']=pd.Series(self.positions)

        # 엑셀 형태로 저장하기
        country.to_excel(path , index=False)
        
    def sys_run(self) :
        self.input_xlsx_path()
        country = self.input_country()
        if self.open_xlsx(country) :
        
            file_data = self.json_set()
            self.write_json(file_data)
            self.mrc_run(file_data)
            print('='*70)
        
instance = Combine_sentence()
instance.sys_run()
        