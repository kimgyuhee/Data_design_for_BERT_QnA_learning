# 마스킹 이미지로 워드클라우드
'''
=========================================== path note ===========================================
9th Apr - Dean 
1. 0번 입력시 종료되는 구간에는 첫 출력문에 모두 '\n0을 입력하여 종료할수있습니다.'를 추가 하였음 
2. 149번줄에 폴더 경로에 '/' 누락시 예외처리 - 맥 사용자용 버전 추가 

=========================================== path note ===========================================
'''



from wordcloud import WordCloud  # 워드 클라우드로 이미지 표현을 위함 
import matplotlib.pyplot as plt  # 시각화 기능 사용을 위함 
import numpy as np               # 이미지 데이터를 다루기 위함 
from PIL import Image            # 이미지를 위한 라이브러리
import os
import datetime                  # 동일한 파일명일 경우 날짜 데이터 추가하기 위한 모듈

# 워드 클라우드 시켜주는 클래스
class Wordclold() :
    def __init__(self): # Wordcloud 프로그램 시작시 호출되는 welcoming 함수 
        print('\n')
        print('='*60)
        print('\t\t시각화 프로그램을 시작합니다.')
        print('='*60)
    '''
    함수명 : open_txt_file
    설명 : 명사가 담긴 txt 파일을 읽어오는 함수
    매개변수 : self(Wordclold)
    반환값 : words(str) -> txt 파일의 내용의 내용을 담고있는 데이터(str)
    '''
    def open_txt_file(self):
        print('\n')
        print('='*60)
        # dean_path = '/Users/deankim/Desktop/Developer/Project/wordcloud/noun_text/W_Korea.txt'
        gyu_path = 'C:\\Users\\user\\Desktop\\projrct\\country\\txt\\터키.txt'   
        while(True):
            txt_file = input(f'불러올 txt 파일의 위치를 입력하세요.\n0을 입력하여 종료할수있습니다.\n기본 경로: {gyu_path}\n경로 입력: ')
            print('='*60)
            txt_file = txt_file.strip()
            
            if txt_file == '0' :
                return '종료'

            if os.path.isfile(txt_file):
                break
            else:
                print('불러올 txt 파일이 경로에 없습니다.')
                print('0을 입력하여 종료할수있습니다.\n')
                continue

        txt = open(txt_file, 'r', encoding='utf-8') 
        lines = txt.read()   # lines 변수를 호출하면 txt 파일을 전체 읽습니다. 
        words = str(lines)   # 워드클라우드에서 읽을수있도록 lines 변수를 string으로 변환해줍니다. 
        txt.close()
        
        return words         # txt 파일의 내용을 담고있는 words 변수를 내보냅니다.

    '''
    함수명 : open_img_file
    설명 : 마스킹 이미지로 사용될 img 파일의 경로를 입력받는 함수
    매개변수 : self(Wordclold)
    반환값 : desg_mask(<class 'numpy.ndarray'>) -> 사용자가 입력한 img 파일 데이터(<class 'numpy.ndarray'>)
    '''
    def open_img_file(self):
        print('\n')
        print('='*60)
        # dean_path = '/Users/deankim/Desktop/Developer/Project/wordcloud/img/korea.png'
        gyu_path = 'C:\\Users\\user\\Desktop\\projrct\\mask_img\\turkey.jpg'
        while(True):
            img_file = input(f'마스킹 이미지로 사용할 파일의 경로를 입력하세요.\n0을 입력하여 종료할수있습니다.\n기본 경로: {gyu_path}\n경로 입력: ')
            print('='*60)
            img_file = img_file.strip()

            if img_file == '0':
                return '종료'

            if os.path.isfile(img_file):
                break
            else:
                print('불러올 이미지 파일이 경로에 없습니다.')
                print('0을 입력하여 종료할수있습니다.\n')
                continue
    
        desg_mask = np.array(Image.open(img_file)) # 사용자가 입력한 img 파일을 desg_mask 변수에 담습니다. 
        # print(type(desg_mask))
        return desg_mask

    '''
    함수명 : set_font_path
    설명 : 폰트 경로를 입력 받는 함수
    매개변수 : self(Wordclold)
    반환값 : path(str) -> 폰트 경로가 담겨 있는 데이터(str)
    '''
    def set_font_path(self):
        print('\n')
        print('='*60)
        # dean_path = '/Users/deankim/Desktop/Developer/Project/wordcloud/font/SB.otf'
        gyu_path = 'C:\\Users\\user\\Desktop\\projrct\\font\\카페24.ttf'
        while(True):
            
            path = input(f'워드클라우드에서 사용할 폰트의 경로를 입력하세요.\n0을 입력하여 종료할수있습니다.\n기본 경로: {gyu_path}\n경로 입력: ')
            print('='*60)
            path = path.strip()

            if path == '0':
                return '종료'

            if os.path.isfile(path):
                break
            else:
                print('폰트가 경로에 존재하지 않습니다.')
                print('0을 입력하여 종료할수있습니다.\n')
                continue

        return path
    

    '''
    함수명 : wordclouder
    설명 : txt 문서를 워드클라우드화 해주는 함수
    매개변수 : self(Wordclold), path(str), desg_mask(str), words(str) 
    -> 폰트 경로 데이터(str), 마스킹 이미지 경로 데이터(str), txt 내용 데이터(str) 
    반환값 : wordcloud(<class 'wordcloud.wordcloud.WordCloud'>) -> words에 담고있던 명사들을 워드클라우드화한 데이터(<class 'wordcloud.wordcloud.WordCloud'>)
    '''
    def wordclouder(self, path, desg_mask, words): # path: 폰트 경로, desg_mask: 마스킹 이미지 경로, words: txt 내용(명사)
        print('\n')
        print('='*60)
        wordcloud = WordCloud(font_path=path, background_color="white", max_font_size=100, mask=desg_mask).generate(words)
        print('성공적으로 워드클라우드 변환을 완료하였습니다.')
        print('='*60)
        return wordcloud  
    

    '''
    함수명 : file_path_for_png
    설명 : 워드클라우드화 이후 이미지 파일의 저장 경로를 지정 받는 함수 
    매개변수 : self(Wordclold)
    반환값 : path(str) -> png 저장 경로 데이터
    '''
    def file_path_for_png(self):
        # dean_path = '/Users/deankim/Desktop/Developer/Project/wordcloud/'
        gyu_path = 'C:\\Users\\user\\Desktop\\projrct\\wordcloud\\'
        print('\n')
        print('='*60)
        while(True):
            path = input(f'png 파일로 저장할 파일 경로를 입력하세요.\n0을 입력하여 종료할수있습니다.\n기본 경로: {gyu_path}\n경로 입력: ') 
            print('='*60)      
            path = path.strip()
            if path == '0' :
                return '종료'

            if path[len(path)-1] != '/':
                path = path + '/'
                
            if os.path.isdir(path):        # 폴더 경로가 존재하는 경우
                break
            else:
                print('경로가 존재하지 않습니다.')
                print('0을 입력하여 종료할수있습니다.\n')
                continue


        return path

    '''
    함수명 : file_name_for_png
    설명 : 워드클라우드화 이후 이미지 파일의 저장할 이름을 입력받는 함수 
    매개변수 : self(Wordclold)
    반환값 : name(str) -> png 저장 이름 데이터
    '''
    def file_name_for_png(self, path) :
        print('\n')
        print('='*60)
        while(True):                
            name = input('png 파일로 저장할 이름을 입력하세요.\n0을 입력하여 종료할수있습니다.\n예) indonesia\n파일명: ')
            print('='*60)
            name = name.strip()

            if name == '0' :
                return '종료'

            if name == '':                 # 파일명을 입력하지 않은 경우 
                print('파일명을 입력해주세요.')
                print('0을 입력하여 종료할수있습니다.\n')
                continue
            if '.' in name:                # 파일명에 확장자명을 같이 적은 경우
                print('확장자명은 입력할 수 없습니다. 파일명만 입력해주세요.')
                print('0을 입력하여 종료할수있습니다.\n')
                continue
            else:                          # 파일명이 정상 입력된 경우
            # ========== 22.04.11 수정 사항 - 동일 파일명 존재시 파일명 변경    
                if os.path.isfile(path+name+'.png') :
                    date = datetime.datetime.now()
                    now = datetime.datetime.strftime(date, '%Y년%m월%d일_%H시%M분')
                    name = name+'_'+now
                    print('동일한 파일이 존재하여 {} 이름으로 저장합니다.\n'.format(name))
                break

        return name
                
    '''
    함수명 : save_as_png
    설명 : 워드클라우드 이후 이미지 파일로 저징해주는 함수
    매개변수 : self(Wordclold), wordcloud(<class 'wordcloud.wordcloud.WordCloud'>), png_path(str) 
    -> txt 파일을 워드클라우드로 변환한 데이터(<class 'wordcloud.wordcloud.WordCloud'>), 이미지 파일로 저장될 경로 데이터(str)
    반환값 : 없음
    '''                                    
    def save_as_png(self, wordcloud, png_path):  # wordcloud: txt 파일을 워드클라우드로 변환한 변수, png_path: 이미지 파일로 저장될 경로를 담고있는 변수
        print('\n')
        print('='*60)
        wordcloud.to_file(png_path)        # 워드클라우드된 내용을 png_path 변수의 경로로 저장합니다. 
        print(f'파일이 {png_path} 경로로 저장되었습니다.')
        print('='*60)
    '''
    함수명 : quick_view
    설명 : 저장 단계를 거치지 않고 미리보기를 보여주는 함수
    매개변수 : self(Wordclold), wordcloud(<class 'wordcloud.wordcloud.WordCloud'>)
    -> txt 파일을 워드클라우드로 변환한 데이터(<class 'wordcloud.wordcloud.WordCloud'>)
    반환값 : 없음
    '''   
    def quick_view(self, wordcloud):             # 저장 단계를 거치지 않고 미리보기를 보여주는 함수 
        plt.figure(figsize = (20,20), dpi=300)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')                    # 의미 없는 그래프 축 제거 
        plt.show()
        
    '''
    함수명 : store_png
    설명 : png를 저장할 경로와 이름을 입력받는 함수, 그리고 그 경로에 저장해주는 함수
    매개변수 : self(Wordclold), wordcloud(<class 'wordcloud.wordcloud.WordCloud'>)
    -> txt 파일을 워드클라우드로 변환한 데이터(<class 'wordcloud.wordcloud.WordCloud'>)
    반환값 : 성공여부(str)
    '''  
    def store_png(self, wordcloud) :
        png_path = self.file_path_for_png()
        if png_path == '종료' :
           return '종료'
                
        png_name = self.file_name_for_png(png_path)
        if png_name == '종료' :
            return '종료'
                
        path = png_path + png_name+'.png'
        self.save_as_png(wordcloud, path)
        return '성공'

    '''
    함수명 : menu
    설명 : 사용자에게 바로 볼건지 저장할건지 묻는 주 메뉴 함수
    매개변수 : self(Wordclold), wordcloud(<class 'wordcloud.wordcloud.WordCloud'>)
    -> txt 파일을 워드클라우드로 변환한 데이터(<class 'wordcloud.wordcloud.WordCloud'>)
    반환값 : 성공여부(bool)
    '''
    def menu(self, wordcloud):
        print('\n')
        print('='*60)
        while(True):
            print('파일을 저장하거나 이미지 파일을 바로 확인합니다. 메뉴를 선택해주세요.')
            try:
                menu = int(input('1. 파일 저장 2. 바로 보기 -> '))
                print('='*60)
            except ValueError:   # 1, 2 메뉴 이외의 선택 
                print('존재하지 않는 메뉴입니다.\n')
                continue
            else :
                if menu == 1:    # 1. 파일 저장
                    result = self.store_png(wordcloud) # 파일 저장하기
                    if result == '종료' :
                        return False
                    break
                elif menu == 2:    # 2. 바로 보기 
                    self.quick_view(wordcloud)
                    if self.menu_1() == True: # 파일저장 묻기
                        result = self.store_png(wordcloud) # 파일 저장하기
                        if result == '종료' :
                            return False
                        break
                    else :
                        return False
                else :
                    print('존재하지 않는 메뉴입니다.\n')
                    continue
        
        return self.menu_2()


    '''
    함수명 : menu_1
    설명 : 파일 저장 여부를 묻는 함수
    매개변수 : self(Wordclold)
    반환값 : 성공여부(bool)
    '''    
    def menu_1(self):  
        print('\n')                          
        print('='*60)
        while(True):
            save_menu = input('파일을 저장할까요? (Y/N) -> ') 
            print('='*60)
            if save_menu in ['Y', 'y']:      # 파일 저장
                print('파일을 저장하겠습니다.')
                return True
            elif save_menu in ['N', 'n']:    # 파일 저장 하지 않음 
                print('파일을 저장하지 않습니다.')
                return False 
            else:                            # 오입력
                print('Y 또는 N으로만 입력해주세요.')
                continue
    '''
    함수명 : menu_2
    설명 : 상위 메뉴로 올라가 계속 진행할지 종료할지 묻는 함수
    매개변수 : self(Wordclold)
    반환값 : 성공여부(bool)
    '''      
    def menu_2(self):   
        print('\n')    
        print('='*60)
        while(True):
            print('계속 진행하거나 시스템을 종료합니다. 메뉴를 선택해주세요.')
            where_to = input('1. 상위 메뉴 2. 종료 -> ')
            print('='*60)
            if where_to == '1':   # 상위 메뉴로 이동합니다.
                print('상위메뉴를 선택하였습니다.')
                return True 
            elif where_to == '2': # 프로그램을 종료시킵니다.
                print('종료를 선택하였습니다.')
                return False
            else : 
                print('존재하지 않는 메뉴입니다.')
                continue
            
    def sys_run(self) :
        while True :
            words = self.open_txt_file() # # txt 파일의 내용을 담고있는 words 변수
            if words == '종료' :
                print('프로그램을 종료합니다.\n')
                break

            desg_mask = self.open_img_file()
            if desg_mask == '종료' :
                print('프로그램을 종료합니다.\n')
                break

            font_path = self.set_font_path()
            if font_path == '종료' :
                print('프로그램을 종료합니다.\n')
                break

            wordcloud = self.wordclouder(font_path, desg_mask, words)

            result = self.menu(wordcloud)

            if result == False :
                print('프로그램을 종료합니다.')
                break




# 인스턴스 실행
wordcloud = Wordclold()
wordcloud.sys_run()