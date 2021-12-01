from pykiwoom.kiwoom import *
import pandas as pd
from pykrx import stock

# 0. 로그인

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")

state = kiwoom.GetConnectState()
if state == 0:
    print("미연결")
elif state == 1:
    print("연결완료")

#--------------------------------------------------------------------------------
def get_krx_kospi(sdate, edate,종목개수):
    종목분류들 = stock.get_index_ticker_list()
    if 종목개수 == 200:
        종목개수 = '1028'
    elif 종목개수 == 100:
        종목개수 = '1034'
    elif 종목개수 == 50:
        종목개수 = '1035'
    list = []
    dfs= []
    for 종목분류코드 in 종목분류들:
        if 종목분류코드 == 종목개수:  #KOSPI50
            세부종목 = stock.get_index_portfolio_deposit_file(종목분류코드)
            print(f'코드리스트 : \n{세부종목}')
            for code in 세부종목:
                df = fdr.DataReader(code,sdate,edate)
                df.insert(0,'Stockcode',code)
                dfs.append(df)
            df = pd.concat(dfs)
    return df


#---------------------------------------------------------------------------------
# 1. OPT10001 : 주식기본정보요청


def opt10001(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10001",
                                  종목코드=code,
                                  output="주식기본정보",
                                  next=0)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df

# 2. OPT10002 : 주식거래원요청

def opt10002(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10002",
                                  종목코드=code,
                                  output="주식거래원요청",
                                  next=0)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df



# 3. OPT10003 : 체결정보요청

def opt10003(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10003",
                                  종목코드=code,
                                  output="체결정보요청",
                                  next=0)
        df.insert(0,'종목코드',code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df


# 4. OPT10004 : 주식호가요청

def opt10004(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10004",
                                  종목코드=code,
                                  output="주식호가요청",
                                  next=0)
        df.insert(0,'종목코드',code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df


# 5. OPT10005 : 주식일주월시분요청

def opt10005(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10005",
                                  종목코드=code,
                                  output="주식일주월시분요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df



# 6. OPT10006 : 주식시분요청

def opt10006(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10006",
                                  종목코드=code,
                                  output="주식시분요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df


# 7. OPT10007 : 시세표성정보요청

def opt10007(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10007",
                                  종목코드=code,
                                  output="시세표성정보요청",
                                  next=0)
        # df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df


# 8. OPT10008 : 주식외국인요청

def opt10008(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10008",
                                  종목코드=code,
                                  output="주식외국인요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df



# 9. OPT10009 : 주식기관요청

def opt10009(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10009",
                                  종목코드=code,
                                  output="주식기관요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df



# 10. OPT10010 : 업종프로그램요청

def opt10010(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10010",
                                  종목코드=code,
                                  output="업종프로그램요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df



# 11. OPT10011 : 투자자정보요청

def opt10011(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10011",
                                  종목코드=code,
                                  output="투자자정보요청",
                                  next=0)
        # df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df


# 12. OPT10012 : 주문체결요청

def opt10012(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10012",
                                  종목코드=code,
                                  output="주문체결요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df


# 13. OPT10013 : 신용매매동향요청

def opt10013(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10013",
                                  종목코드=code,
                                  output="신용매매동향요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df


# 14. OPT10014 : 공매도추이요청

def opt10014(sdate,edate,codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10014",
                                  종목코드=code,
                                  시간구분=0, # 시간구분 = 0:시작일, 1:기간
                                  시작일자=sdate,
                                  종료일자=edate,
                                  output="공매도추이요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df


# 15. OPT10015 : 일별거래상세요청

def opt10015(sdate,codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10015",
                                  종목코드=code,
                                  시작일자=sdate,
                                  output="일별거래상세요청",
                                  next=0)
        df.insert(0, '종목코드', code)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df



# # 16. OPT10016 : 신고저가요청    ----- X
#
# def opt10016 ():
#     dfs = []
#
#     for code in codelist:
#         df = kiwoom.block_request("opt10016",
#                                   시장구분=1, # 시장구분 = 000:전체, 001: 코스피, 101: 코스닥
#                                   신고저구분=1, # 신고저구분 = 1:신고가, 2: 신저가
#                                   종목조건=0, # 종목조건 = 0:전체조회, 1: 관리종목제외, 3: 우선주제외, 5: 증100제외, 6: 증100만보기, 7: 증40만보기, 8: 증30만보기
#                                   거래량구분=0,
#                                   고저종구분=2, # 고저종구분 = 1:고저기준, 2: 종가기준
#                                   output="일별거래상세요청",
#                                   next=0)
#         '''
#         거래량구분 = 00000:전체조회, 00010: 만주이상, 00050: 5
#         만주이상, 00100: 10
#         만주이상, 00150: 15
#         만주이상, 00200: 20
#         만주이상, 00300: 30
#         만주이상, 00500: 50
#         만주이상, 01000: 백만주이상
#         '''
#
#
#
#
#
#         dfs.append(df)
#         time.sleep(1)
#
#     df = pd.concat(dfs)
#     return df



# 42. OPT10042 : 순매수거래원순위요청

def opt10042(sdate,edate,codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10042",
                                  종목코드=code,
                                  시작일자=sdate,
                                  종료일자=edate,
                                  조회기간구분=1, # 조회기간구분 = 0:기간으로 조회, 1: 시작일자, 종료일자로
                                  시점구분=0, # 시점구분 = 0:당일, 1: 전일
                                  기간=120, # 기간 = 5:5일, 10:10일, 20:20일, 40:40일, 60:60일, 120:120일
                                  정렬기준=1, # 정렬기준 = 1:종가순, 2:날짜순
                                  output="순매수거래원순위요청",
                                  next=0)
        dfs.append(df)
        time.sleep(1)


    df = pd.concat(dfs)
    return df



# 43. OPT10043 : 거래원매물대분석요청 ----------------------- 42번에서 회원사코드 구한 후 사용해야 함

def opt10043(sdate,edate,codelist,branchcode):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10043",
                                  종목코드=code,
                                  시작일자=sdate,
                                  종료일자=edate,
                                  조회기간구분=1, # 조회기간구분 = 0:기간으로 조회, 1: 시작일자, 종료일자로
                                  시점구분=0, # 시점구분 = 0:당일, 1: 전일
                                  기간=120, # 기간 = 5:5일, 10:10일, 20:20일, 40:40일, 60:60일, 120:120일
                                  정렬기준=1, # 정렬기준 = 1:종가순, 2:날짜순
                                  회원사코드=branchcode, # 회원사 코드는 OPT10042 조회 또는 GetBranchCodeName()함수사용
                                  output="거래원매물대분석요청",
                                  next=0)
        dfs.append(df)
        time.sleep(1)


    df = pd.concat(dfs)
    return df

# 44. OPT10044 : 일별기관매매종목요청

def opt10044(sdate,edate):

    df = kiwoom.block_request("opt10044",
                                  시작일자=sdate,
                                  종료일자=edate,
                                  매매구분=1, # 매매구분 = 0:전체, 1:순매도, 2:순매수
                                  시장구분=1, # 시장구분 = 001:코스피, 101:코스닥
                                  output="일별기관매매종목요청",
                                  next=0)
    return df


# 45. OPT10045 : 종목별기관매매추이요청   -------------------------------------- 2번뽑기

def opt10045(sdate,edate):

    df = kiwoom.block_request("opt10045",
                                  시작일자=sdate,
                                  종료일자=edate,
                                  기관추정단가구분=2, # 기관추정단가구분 = 1:매수단가, 2:매도단가
                                  외인추정단가구분=2, # 외인추정단가구분 = 1:매수단가, 2:매도단가
                                  output="종목별기관매매추이요청",
                                  next=0)
    return df



# 63. OPT10063 : 장중투자자별매매요청

def opt10063(codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10063",
                                  시장구분='001',  # 시장구분 = 000:전체, 001:코스피, 101:코스닥
                                  금액수량구분=1,  # 금액수량구분 = 1:금액, 2:수량
                                  투자자별= 6,    # 투자자별 = 6:외국인, 7:기관계, 1:투신, 0:보험, 2:은행, 3:연기금, 4:국가, 5:기타법인
                                  외국계전체= 0,   # 외국계전체 = 1:체크, 0:언체크
                                  동시순매수구분= 0, # 동시순매수구분 = 1:체크, 0:언체크
                                  output="장중투자자별매매요청",
                                  next=0)
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df

# 81. OPT10081 : 주식일봉차트조회요청

def opt10081(date, codelist):
    dfs = []

    for code in codelist:
        df = kiwoom.block_request("opt10081",
                                  종목코드=code,
                                  기준일자=date,
                                  수정주가구분=1, # 수정주가구분 = 0 or 1, 수신데이터 1:유상증자, 2:무상증자, 4:배당락, 8:액면분할, 16:액면병합, 32:기업합병, 64:감자, 256:권리락
                                  output="주식일봉차트조회요청",
                                  next=0)
        df['종목코드'] = code
        dfs.append(df)
        time.sleep(1)

    df = pd.concat(dfs)
    return df



# 전년대비

#------------------------------------------------------------------------------
# 데이터 조회 및 출력

# codelist = ['000270', '068270', '011170', '028260', '000660',
#         '090430', '018260', '018880', '003670', '361610']
#
# df_opt10014 = opt10014('20210101','20210705',codelist)
# print(df_opt10014)

# df_opt10081.to_csv('주식일봉차트조회요청_코스피10개.csv',index=False,encoding='euc-kr')


#-------------------------------------------------------------------------------
# 07-08 api 데이터 수집 셋팅

# kospi100 = pd.read_csv('kospi100종목.csv') # 실제 102종목
# kospi100['종목코드'] = kospi100['종목코드'].apply(lambda x: str(x).zfill(6))
# codelist = kospi100['종목코드'].to_list()
# # print(codelist)
#
# sdate='20210101'
# edate='20210705'

#------------------------
# 07-09 api 데이터 수집 셋팅
kospi200 = pd.read_csv('kospi200_0709.csv') # 200종목, 0709 조회 기준
kospi200['Stockcode'] = kospi200['Stockcode'].apply(lambda x: str(x).zfill(6))
codelist = kospi200['Stockcode'].unique()
print(len(codelist))
print(codelist)
# print(kospi200['Stockcode'].nunique()) # 200개
sdate='20210101'
edate='20210708'


#-----------------------------------------------------------------------------
# 이전 test용


# codelist = ['000270', '068270', '011170', '028260', '000660',
#         '090430', '018260', '018880', '003670', '361610']
#
# df_opt10001 = opt10001(codelist)
# print(df_opt10001)
# df.to_csv('키움_opt10001_주식기본정보.csv',index=False,encoding='euc-kr')

#----------------------------------------------------------------------------
# 데이터 조회


# df_opt10001 = opt10001(codelist)
# df_opt10002 = opt10002(codelist)
# df_opt10003 = opt10003(codelist)
# df_opt10004 = opt10004(codelist)
# df_opt10005 = opt10005(codelist)
# df_opt10006 = opt10006(codelist)
# df_opt10007 = opt10007(codelist)
# #
# df_opt10008 = opt10008(codelist)
# df_opt10009 = opt10009(codelist)
# df_opt10010 = opt10010(codelist)
# df_opt10011 = opt10011(codelist)
# df_opt10012 = opt10012(codelist)
# df_opt10013 = opt10013(codelist)

# 날짜데이터필요------------------------------------------
# df_opt10014 = opt10014(sdate,edate,codelist)
# df_opt10015 = opt10015(sdate,codelist)

# df_opt10042 = opt10042(sdate,edate,codelist)
# df_opt10043 = opt10043(sdate,edate,codelist,branch) #----------------------------branchcode필요 (opt10042)
df_opt10044 = opt10044(sdate,edate)
# df_opt10045 = opt10045(sdate,edate)


#-----------------------csv로 출력---------------------------------------------

# df_opt10001.to_csv('kospi200_opt10001_주식기본정보요청.csv',index=False,encoding='euc-kr')
#
# df_opt10002.to_csv('kospi200_opt10002_주식거래원요청.csv',index=False,encoding='euc-kr')
#
# df_opt10003.to_csv('kospi200_opt10003_체결정보요청.csv',index=False,encoding='euc-kr')
# # #
# df_opt10004.to_csv('kospi200_opt10004_주식호가요청.csv',index=False,encoding='euc-kr')

# df_opt10005.to_csv('kospi200_opt10005_주식일주월시분요청.csv',index=False,encoding='euc-kr')

# df_opt10006.to_csv('kospi200_opt10006_주식시분요청.csv',index=False,encoding='euc-kr')
#
# df_opt10007.to_csv('kospi200_opt10007_시세표성정보요청.csv',index=False,encoding='euc-kr')
# df_opt10008.to_csv('kospi200_opt10008_주식외국인요청.csv',index=False,encoding='euc-kr')
# df_opt10009.to_csv('키움_opt10009_주식기관요청.csv',index=False,encoding='euc-kr')
# df_opt10010.to_csv('키움_opt10010_업종프로그램요청.csv',index=False,encoding='euc-kr')
# df_opt10011.to_csv('키움_opt10011_투자자정보요청.csv',index=False,encoding='euc-kr')
# df_opt10012.to_csv('키움_opt10012_주문체결요청.csv',index=False,encoding='euc-kr')
# #
# df_opt10013.to_csv('키움_opt10013_신용매매동향요청.csv',index=False,encoding='euc-kr')
# df_opt10014.to_csv('키움_opt10014_공매도추이요청.csv',index=False,encoding='euc-kr')
# df_opt10015.to_csv('키움_opt10015_일별거래상세요청.csv',index=False,encoding='euc-kr')


# df_opt10042.to_csv('키움_opt10042_순매수거래원순위요청.csv',index=False,encoding='euc-kr') #--------------우선 보류
# df_opt10043.to_csv('키움_opt10043_거래원매물대분석요청.csv',index=False,encoding='euc-kr') #--------------opt10042 작업 후
df_opt10044.to_csv('키움_opt10044_일별기관매매종목요청.csv',index=False,encoding='euc-kr')
# df_opt10045.to_csv('키움_opt10045_종목별기관매매추이요청.csv',index=False,encoding='euc-kr')


#-----------------------------------결과물 확인------------------------------------------

# print(f'opt10002: 주식거래원요청\n')
# print(df_opt10002.head())

# print(f'opt10003: 체결정보요청\n')
# print(df_opt10003.head())
# print(f'opt10004: 주식호가요청\n')
# print(df_opt10004.head())
# print(f'opt10005: 주식일주월시분요청\n')
# print(df_opt10005.head())

# print(f'opt10006: 주식시분요청\n')
# print(df_opt10006.head())

# print(f'opt10007: 시세표성정보요청\n')
# print(df_opt10007.head())

# print(f'opt10008: 주식외국인요청\n')
# print(df_opt10008.head())



# print(f'opt10009: 주식기관요청\n')
# print(df_opt10009.head())

# print(f'opt10010: 업종프로그램요청\n')
# print(df_opt10010.head())

