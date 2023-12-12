from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed

def index(request):
	# 질문 목록 데이터 얻기: Question 모델에서 모든 질문을 작성일시(create_date)의 역순으로 정렬하여 가져옵니다.
    question_list = Question.objects.order_by('-create_date')

	# 템플릿으로 전달할 데이터를 담은 context 딕셔너리를 생성합니다.
    # 'question_list' 키에 위에서 얻은 질문 목록을 할당합니다.
    context = {'question_list': question_list}

	# render 함수를 사용하여 'pybo/question_list.html' 템플릿을 렌더링합니다.
    # 이때, 템플릿에 context의 내용을 전달하여 동적인 데이터를 템플릿에서 사용할 수 있도록 합니다.
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # question_id에 해당하는 Question 모델의 객체를 가져옵니다.
    # 여기서 사용한 pk는 Question 모델의 기본키(Primary Key)에 해당하는 값을 의미합니다.
    question = get_object_or_404(Question, pk=question_id)
    # 가져온 질문 객체를 'question'이라는 이름의 변수로 context에 담습니다.
    context = {'question': question}
    # render 함수를 사용하여 'pybo/question_detail.html' 템플릿에 context를 전달하여 렌더링합니다.
    # 이때, 템플릿에 context의 내용을 전달하여 동적인 데이터를 템플릿에서 사용할 수 있도록 합니다.
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    # question_id에 해당하는 Question 모델의 객체를 가져옵니다.
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

