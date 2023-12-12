from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 질문의 제목은 최대 200자로 지정한다.
    content = models.TextField()                # 질문의 내용을 담는 텍스트 필드
    create_date = models.DateTimeField()        # 질문이 작성된 일시를 저장하는 필드
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 답변(Answer) 모델의 question 필드는 Question 모델과의 관계를 나타내는 외래키(ForeignKey)이다.
    # on_delete=models.CASCADE는 연결된 질문(Question)이 삭제될 때 해당 답변도 함께 삭제된다는 의미이다.
    content = models.TextField()                # 답변의 내용을 담는 텍스트 필드
    create_date = models.DateTimeField()        # 답변이 작성된 일시를 저장하는 필드