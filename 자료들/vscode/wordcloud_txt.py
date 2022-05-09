# 기존 txt 파일에서 명사만 추출
from konlpy.tag import Okt
import sys
from wordcloud import WordCloud

class TextToWordCloud:
    def txt_dir(self):
        self.txt_file = input('txt 파일 경로: ')
        return self.txt_file

    def read_txt(self, txt_file):                         # read_txt(self, txt 파일 경로 문서)
        self.text = open(txt_file, 'r', encoding='utf-8')
        self.lines = self.text.read()                
        self.text.close()
        return self.lines 

    def visualise_text(self, lines): # 워드클라우드 해주는 함수 visualise_text(self, txt 문서)
        self.wordcloud = WordCloud(font_path = 'C:\\Data_design_for_BERT_QnA_learning\\font\\font1.otf',
                              background_color='white',
                               width=1000,
                               height=1000,
                               max_words=100,
                               max_font_size=200)

        self.wordcloud = self.wordcloud.generate(lines)
        return self.wordcloud

    def save_to_png(self, wordcloud):
        self.wordcloud.to_file('C:\\Data_design_for_BERT_QnA_learning\\check\\wc_check\\test.png')
        print('파일 저장이 정상적으로 완료됐습니다.')

class NounFilter:
    def __init__(self):
        print('='*60)
        print('\t\t  명사 추출 프로그램을 시작합니다.')
        print('='*60)
        
    def file_dir(self):
        print('txt 파일을 저장합니다. 저장 경로를 지정해주세요.')
        print('C:\\Data_design_for_BERT_QnA_learning\\check\wc_check\\')
        self.file_directory = input('저장 파일 경로: ')
        print('='*60)
        return self.file_directory
    
    def file_n(self):
        print('txt 파일의 이름을 지정해주세요.\n예) test')
        self.file_name = input('txt 파일명 지정: ')
        print('='*60)
        return self.file_name
    
    def confirming_file_name(self, file_directory, file_name):
        print('txt 파일을 아래와 같이 저장합니다.')
        print(f'경로: {file_directory}\n이름: {file_name}')
        print('='*60)
        self.txt_file = file_directory + file_name + '.txt'
        return self.txt_file
    
    def open_raw_data(self):
        print('명사를 추출할 데이터 파일의 경로를 입력해주세요.')
        print('C:\\Data_design_for_BERT_QnA_learning\\country\\')
        self.raw_data = input('데이터 파일 경로: ')
        print('='*60)
        return self.raw_data 
    
    def read_file(self, raw_data):        
        with open(self.raw_data, 'r', encoding='utf-8') as self.f:
            self.text = self.f.read()
        return self.text
        
    def write_file(self, text, txt_file):
        self.okt = Okt()
        self.noun = self.okt.nouns(text)
        
        self.orig_stdout = sys.stdout
        with open(txt_file, 'w', encoding='utf-8') as self.file:
            sys.stdout = self.file
            
            for i in self.noun:
                if len(i) > 1 and i != '문장':
                    print(i)

            sys.stdout = self.orig_stdout
            
        print('명사 추출이 완료되었으며 파일이 정상적으로 저장되었습니다.')


noun_f = NounFilter()
file_directory = noun_f.file_dir()
file_name = noun_f.file_n()
txt_file = noun_f.confirming_file_name(file_directory, file_name)
raw_data = noun_f.open_raw_data()
text = noun_f.read_file(raw_data)
noun_f.write_file(text, txt_file)
    

visualise = TextToWordCloud()
txt_file = visualise.txt_dir()
lines = visualise.read_txt(txt_file)
wordcloud = visualise.visualise_text(lines)
visualise.save_to_png(wordcloud)

