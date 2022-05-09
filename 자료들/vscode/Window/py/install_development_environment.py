import sys         # 파이썬 인터프리터와 관련된 정보 기능을 제공하는 모듈
import subprocess  # 쉘 명령을 실행할수있게 해주는 라이브러리

print('\n')
print('='*60)
print('\t\t  필요 모듈 버전 업데이트')
print('='*60)

try:
    import wheel as wh
    print('wheel 버전: ' + wh.__version__)

    import pip as p
    print('pip 버전: ' + p.__version__)    

    # 시각화
    import wordcloud  as wc
    print('wordcloud 버전: ' + wc.__version__)

    import matplotlib as mt
    print('matplotlib 버전: ' + mt.__version__)

    # 형태소 분석기
    import konlpy as kn
    print('konlpy 버전: ' + kn.__version__)

    # 데이터분석
    import pandas as pd
    print('pandas 버전: ' + pd.__version__)

    import numpy as np
    print('numpy 버전: ' + np.__version__)

    # 작업 진행도
    import tqdm as tq
    print('tqdm 버전: ' + tq.__version__)


except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'wheel'])
    print('wheel 모듈을 설치하였습니다.\nwheel 버전: ' + wh.__version__)
  
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    print('pip 모듈을 설치하였습니다.\npip 버전: ' + p.__version__)

    # 시각화 
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'wordcloud'])
    print('wordcloud 모듈을 설치하였습니다.\nwordcloud 버전: ' + wc.__version__)

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'matplotlib'])
    print('matplotlib 모듈을 설치하였습니다.\nmatplotlib 버전: ' + mt.__version__)

    # 형태소 분석기
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'konlpy'])
    print('konlpy 모듈을 설치하였습니다.\nkonlpy 버전: ' + kn.__version__)

    # 데이터 분석
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pandas'])
    print('pandas 모듈을 설치하였습니다.\npandas 버전: ' + pd.__version__)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'numpy'])
    print('numpy 모듈을 설치하였습니다.\nnumpy 버전: ' + np.__version__)

    # 작업 진행도
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'tqdm'])
    print('tqdm 모듈을 설치하였습니다.\ntqdm 버전: ' + tq.__version__)



finally:
    print('\n')
    print('모듈 버전 검사를 마쳤습니다.')