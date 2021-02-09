from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.urls import reverse
from django.views import generic
from .models import Question, Choice, Voter
from .forms import QuesForm, ChoiceForm

# Create your views here.
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = { 'latest_question_list': latest_question_list }
# 	return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/details.html', {'question': question})

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/details.html'

class QuesView(generic.CreateView):
	model = Question
	form_class = QuesForm
	template_name = 'polls/createques.html'

class ChoiceView(generic.TemplateView):
	template_name = 'polls/options.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

class VotedView(generic.DetailView):
	model = Question
	template_name = 'polls/voted.html'


def choice(request, pk):
	question = get_object_or_404(Question, pk=pk)
	if request.POST:
		question.choice_set.create(choice_text=request.POST['op1'], votes=0)
		question.choice_set.create(choice_text=request.POST.get('op2'), votes=0)
		question.choice_set.create(choice_text=request.POST['op3'], votes=0)
		question.choice_set.create(choice_text=request.POST['op4'], votes=0)
		return HttpResponseRedirect(reverse('polls:index'))

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	if Voter.objects.filter(question=question, user=request.user.id).exists():
		return HttpResponseRedirect(reverse('polls:voted', args=(question_id,)))
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/details.html', {'question':question, 'error_message': "You didn't select a choice"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		v=Voter(user=request.user, question=question)
		v.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})

def search(request):
	query=request.GET.get('query')
	search1 = Question.objects.filter(question_text__icontains=query)
	search2 = Question.objects.filter(pub_date__icontains=query)
	search = search1.union(search2)
	params = {'search': search, 'query':query}
	return render(request, 'polls/search.html', params)


def resultData(request, obj):
	votedata=[]
	question=Question.objects.get(id=obj)
	votes=question.choice_set.all()
	for i in votes:
		votedata.append({i.choice_text:i.votes})
	return JsonResponse(votedata, safe=False)


