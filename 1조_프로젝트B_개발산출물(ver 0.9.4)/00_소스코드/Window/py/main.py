from importlib import reload # 모듈을 재호출하기위해 쓰임
import ascii_art as asc
import time

class Main():
    def __init__(self): # main 프로그램 시작시 호출되는 welcoming 함수 
        print('\n\n')
        print('='*60)
        print('='*60)
        print('\t\t\t\t\t\tfor Windows')
        print('\tBERT 질의응답 학습을 위한 데이터 설계 프로그램')
        print('\t\t\t  START')
        print('='*60)
        print('='*60)
        print('\n\n')
    '''
    함수명: check_libraries
    설 명: 각 모듈 실행을 위해 필요한 라이브러리를 설치하는 함수
    매개변수: self(Converter)
    반환값: 없음  
    '''
    def check_libraries(self):
        print('\t필요 모듈을 설치하거나 버전을 업데이트합니다.')
        print('\n')
        import install_development_environment
    '''
    함수명: menu
    설 명: 각 모듈을 실행시켜줄 메뉴를 보여주고 선택된 모듈을 실행시키는 함수
    매개변수: self(Converter)
    반환값: 없음  
    '''
    def menu(self):
        json = 0 # json_to_txt 모듈이 실행되는 횟수에 따라 import 또는 reload로 조건문이 나뉨 
        txt = 0  # txt_in_nouns 모듈이 실행되는 횟수에 따라 import 또는 reload로 조건문이 나뉨 
        vis = 0  # visualiser 모듈이 실행되는 횟수에 따라 import 또는 reload로 조건문이 나뉨 
        com = 0  # combine_sentences 모듈이 실행되는 횟수에 따라 import 또는 reload로 조건문이 나뉨 
        while(True):
            print('\n')
            print('='*60)
            asc.img.book()
            print('\t1. TXT 문장 추출 모듈\t2. 명사 추출 모듈\n\t3. 시각화 모듈\t\t4. 문장 통합 모듈\n   입력없이 엔터를 눌러서 프로그램을 종료 할 수 있습니다.')
            print('='*60)
            print('\n')
            menu_input = input('메뉴 입력: ')
            menu_input = menu_input.strip() # 사용자가 공백을 입력하는 경우 방지 
            if menu_input == '':            # 값 없이 엔터하여 프로그램 종료 가능 
                print('종료를 선택하였습니다.')
                break
            if menu_input in ['1', '2', '3', '4']:
                # ================== json_to_txt ==================
                if menu_input == '1':
                    if json == 0: # 모듈 첫 실행일경우 
                        json += 1
                        asc.img.open()
                        import json_to_txt
                        if self.menu_2() == True:
                            continue
                        else :
                            print('종료를 선택하였습니다.')
                            break

                    if json > 0: # 모듈이 n회차 실행되는 경우
                        json += 1
                        asc.img.open()
                        reload(json_to_txt)
                        if self.menu_2() == True:
                            continue
                        else :
                            print('종료를 선택하였습니다.')
                            break
                # ================== txt_in_nouns ==================
                if menu_input == '2':
                    if txt == 0: # 모듈 첫 실행일경우 
                        txt += 1
                        asc.img.open()
                        import txt_in_nouns
                        if self.menu_2() == True:
                            continue
                        else :
                            print('종료를 선택하였습니다.')
                            break

                    if txt > 0: # 모듈이 n회차 실행되는 경우
                        txt += 1
                        asc.img.open()
                        reload(txt_in_nouns)
                        if self.menu_2() == True:
                            continue
                        else :
                            print('종료를 선택하였습니다.')
                            break
                # ================== visualiser ==================
                if menu_input == '3':
                    if vis == 0: # 모듈 첫 실행일경우 
                        vis += 1
                        asc.img.open()
                        import visualiser_modified
                        if self.menu_2() == True:
                            continue
                        else :
                            print('종료를 선택하였습니다.')
                            break

                    if vis > 0: # 모듈이 n회차 실행되는 경우
                        vis += 1
                        asc.img.open()
                        reload(visualiser_modified)
                        if self.menu_2() == True:
                            continue
                        else :
                            print('종료를 선택하였습니다.')
                            break
                # ================== combine_sentences ==================
                if menu_input == '4':
                    if com == 0: # 모듈 첫 실행일경우 
                        com += 1
                        asc.img.open()
                        import combine_sentences
                        if self.menu_2() == True:
                            continue
                        else :
                            print('종료를 선택하였습니다.')
                            break

                    if com > 0: # 모듈이 n회차 실행되는 경우
                        com += 1
                        asc.img.open()
                        reload(combine_sentences)
                        if self.menu_2() == True:
                            continue
                        else :
                            print('종료를 선택하였습니다.')
                            break
            else:
                asc.img.error4()
                print('메뉴는 1번부터 4번까지입니다. 종료를 원하는 경우 입력값없이 엔터를 눌러주세요.')
                time.sleep(1)
                print('\n')
                continue
    '''
    함수명: menu_2
    설 명: 추가 진행 여부를 묻는 함수
    매개변수: self(Converter)
    반환값: 없음  
    '''
    def menu_2(self):
        while True :
            print('\n')
            print('='*60)
            option = input('최상위 메뉴로 돌아가거나 프로그램을 완전히 종료합니다.\n상위 메뉴 [1], 종료 [0]\n입력: ')
            print('='*60)
            option = option.strip()
            if option.upper() == '1':
                print('최상위 메뉴를 선택하였습니다.')
                return True
            elif option.upper() == '0':
                print('종료를 선택하였습니다.')
                return False
            else:
                asc.img.error4()
                print('1 또는 0으로만 입력해주세요.')
                time.sleep(1)

    def exit(self):
        print('='*60)
        print('='*60)
        print('\t\t\t\t\t\tfor Windows')
        print('\tBERT 질의응답 학습을 위한 데이터 설계 프로그램')
        print('\t\t\t   END')
        print('='*60)
        print('='*60)
        print('\n\n')

main = Main() # Main 클래스의 인스턴스 
main.check_libraries() # 라이브러리 자동 설치
main.menu() # 메뉴 인터페이스 출력 
asc.img.exit()
main.exit()


