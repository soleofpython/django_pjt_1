from django.shortcuts import render

# Create your views here.
def dashboard(request):
    # 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
    # django 환경설정 파일 지정
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")
    # # django settings 메모리 로딩 적용
    # django.setup()

    # # Foods 클래스와 연결된 테이블에 data를 ORM으로 업로딩하기 위해 impost함
    # from .models import DashData

    # CSV_PATH='.dashboard/datas/seocho.csv'
    # # CSV_PATH='.'


    # with open(CSV_PATH, 'r',  encoding='utf-8') as seocho:
    # # csv.reader(파일 식별자)
    #     dataRows = csv.reader(seocho, skipinitialspace=True)
    #     # print(list(dataRows))

    #     dataRows = filter(None, list(dataRows))
    #     # print(dataRows)

        # for dbData in dataRows:
        # # print(dbData[0])
            dbData[0] = dbData[0].replace("-","")
            dbData[0] = int(dbData[0])

            if dbData[3].isinstance(int, ):

                dbData[3] = dbData[3].replace("-","") 
                dbData[3] = int(dbData[3])

        #         if dbData[1] != None or dbData[1] != '':
        #             DashData.objects.update_or_create(
        #                 restaurant = dbData[1],
        #                 defaults={
        #                     "regDate": dbData[0],
        #                     "restaurant": dbData[1],
        #                     "personnel": dbData[2],
        #                     "revenue": dbData[3],
        #                     "district": dbData[4],
        #                 }
        # #             )

        # dbDatas = DashData.objects.all(/)

        # chartDash = {
        #     "dbDatas" : dbDatas
        # }

        # return render(request, "dashboard/dashboard.html", chartDash)
            # dbData[3].replace("-","")
            # 무조건 Upload, 중복 데이터 발생 가능
            # Foods.objects.create(    
            #     cook_name = dbData[0],
            #     count = dbData[1],
            #     unit_price = dbData[2],
            # )

        # 이건 무조건 uploading
        # filter로 중복을 체크하고, 있으면 update. 없다면 create하는 메서드
        # Foods.objects.update_or_create(
        #     # filter : 중복을 체크할 값
        #     cook_name = dbData[0],
            
            # 새롭게 create할 value : filtering한 결과에 의해 중복값이 없을 때
            # defaults={
            #     "regDate": regDate,
            #     "restaurant": restaurant,
            #     "personnel": int(personnel),
            #     "revenue": int(revenue),
            #     "district": district,
            # }
            # cook_name = menu_name, count=count, unit_price=unit_price
        # )

    # if request.method == "POST":
    #     form = DashDataForm(request.POST)
    #     # print(form)
    #     if form.is_valid():
    
    #         # 폼에 입력 값을 개별로 변수 대입
    #         input_restaurant = form.data.get('restaurant', None)
    #         input_num = form.data.get('revenue', None)
            
    #         # DashData에 연결된 db에 입력데이터가 있으면 update,
    #         # 없으면 create하는 로직
    #         DashData.objects.update_or_create(
    #             # filter : 중복을 체크할 값
    #             # rest : DashData 클래스의 속성 => 연결된 테이블의 rest 속성
    #             # rest의 값과 입력을 비교함, 값이 있는지 없는지 체크하는 역할
    #             restaurant = input_restaurant,
                
    #             # form에서 입력한 rest의 값이 없으면 테이블에 저장하도록 함.
    #             # new value : 
    #             defaults= {
    #                 'restaurant': input_restaurant,
    #                 'revenue' : input_num
    #             }
    #         )
            # form 객체의 데이터 db 저장
            # form 객체의 데이터 테이블에 무조건 저장
            # form.save() 
    
    # revenue 필드의 최대값 찾아서
    # from django.db.models import Max, Sum
    # # revenue 필드의 가장 큰 값 추출
    # max_pop = DashData.objects.aggregate(Max('revenue'))
    # # print(max_pop) # dict 타입 확인
    # # revenue의 최대값인 레코드 추출
    # revenue__max = DashData.objects.get(revenue = max_pop['revenue__max'])
    # print(revenue__max)
    
    # # 인구 통계 나라수    
    # district = DashData.objects.count()
    # print(district)
    
    # 입력한 인구 총 합계
    # 테이블 revenue 컬럼의 전체의 인구 총합, 참여한 나라수
    # total_pop = DashData.objects.aggregate(Sum('revenue'))
    # print(total_pop['revenue__sum'])
    # total_pop = total_pop['revenue__sum']
    
    # db DashData 클래스를 통해 DB 데이터 가져오기
    # 쿼리 데이터 변수에 대입
    # restaurant = DashData.objects.all()
    # # print(rest_datas)
    
    # # form 객체 생성
    # form=DashDataForm()
    
    # 가장 인구 많은 나라와 그 나라의 인구
    # from django.db.models import Max
    # pop_max=DashData.objects.aggregate(Max('revenue'))
    # print(pop_max)
    
    # db 전체의 인구 총합, 참여한 나라수
    # 
    
    
    # html 템플릿 작성
    # 쿼리 데이터 식별자를 html 템플릿에 랜더링
    # response 해 주기
    
    # context = {
    #     "regDate": regDate,
    #     "restaurant": restaurant,
    #     "personnel": int(personnel),
    #     "revenue": int(revenue),
    #     "district": district,
    # }
    
    # return render(request, "dashboard/dashboard.html", context)

        # form 객체의 데이터 테이블에 무조건 저장
        # form.save()  