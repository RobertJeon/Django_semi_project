from django.urls import path

from . import views

# pybo 앱 이외의 다른 앱이 프로젝트에 추가 될 수도 있으므로 네임스페이스를 의미하는 app_name 변수를 지정해줍니다.
app_name = 'pybo'

urlpatterns = [
    # config/urls.py에서 이미 pybo/로 시작하는 url이 pybo/urls.py로 매핑되었기 때문에
    # '' 으로 작성되었다. 별칭은 index로 정했습니다.
    path('',views.index, name='index'),

    # '<int:question_id>/'는 정수형(question_id) 파라미터를 가지는 URL을 나타냅니다.
    # 이 URL 패턴에 대한 처리는 views.detail 함수를 호출하여 진행됩니다. 별칭은 detail로 정했습니다.
    path('<int:question_id>/', views.detail, name='detail'),

    # 'answer_create'는 질문에 대한 답변을 등록하는 URL 패턴입니다.
    # views.answer_create 함수를 호출하여 진행됩니다.
    # 'name' 매개변수를 통해 URL 패턴에 대한 별칭(alias)을 'answer_create'로 지정하였습니다.
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

]