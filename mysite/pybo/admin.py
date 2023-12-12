from django.contrib import admin

# Register your models here.
from .models import Question

# Django 관리자 페이지에서 Question 모델을 검색 설정을 위한 QuestionAdmin을 정의합니다.
class QuestionAdmin(admin.ModelAdmin):
    # search_fields는 관리자 페이지에서 특정 필드를 검색할 수 있게 해주는 옵션입니다.
    # 'subject' 필드를 기반으로 검색할 수 있도록 설정되어 있습니다.
    search_fields = ['subject']

# Question 모델과 위에서 정의한 QuestionAdmin 클래스를 함께 Django 관리자 페이지에 등록합니다.
admin.site.register(Question, QuestionAdmin)