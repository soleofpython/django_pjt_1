import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_django.settings")
    # django settings 메모리 로딩 적용
django.setup()

from dashboard.models import DashData

CSV_PATH='./dashboard/datas/songpa.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
  data_rows = csv.reader(file, skipinitialspace=True)
  # header(첫번째 줄) 제외
  # next(data_rows, None) 

  # 공백라인을 제거하기 위해서
#   data_rows = list(data_rows)
  print("전 ", data_rows)
  data_rows = list(filter(None, data_rows))
  print("후 ", data_rows)

  # DB 테이블에 한 레코드씩 입력하기
  for dbData in data_rows:
    # print(row[0])
    # 
    # if dbData[2].isinstance(int, ):
    # 식당 매출중에 ,(콤마)를 없애고 숫자로 형 변환
    dbData[3] = dbData[3].replace(',', '') 
    dbData[3] = int(dbData[3])
    # dbData[2] = dbData[2]



    # 식당명은 primary key로 할 수 없기에, DB에서 ID를 PK로 처리한다. 
    if dbData[0] != None or dbData[0] != '' or dbData[2] != "-":
        # dbData[2] = int(dbData[2])
      # 예외 처리 : 만약에 첫번째 행에 날짜가 있다면, 업데이터
        DashData.objects.update_or_create(
            # filter : 중복을 체크할 값


            restaurant = dbData[1], 
            regDate = dbData[0],

            # menu_name이 cook_name 컬럼에 값이 없으면 테이블에 저장하도록함
            #new value :
            defaults = {
                
                "restaurant": dbData[1],
                "personnel": dbData[2],
                "revenue": dbData[3],            
                "regDate": dbData[0],
                "district": "송파구",

            }
        )
    else:
      # 메뉴가 없을 경우는 pass
      continue