from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
# def index(request):
# 	latest_question_list=Question.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template('polls/index.html')
# 	context={'latest_question_list' : latest_question_list,}
# 	# output=','.join([p.question_text for p in latest_Questions_list])
# 	# return HttpResponse(output)
# 	return render(request,'polls/index.html',context)

# def detail(request, question_id):
# 	# try:
# 	question=get_object_or_404(Question, pk=question_id)
	
# 	# except Questions.DoesNotExist:
# 	# 	raise Http404("Question does not exist")
    
# 	return render(request, 'polls/deatil.html', {'question':question})

# def results(request, question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html',{'question':question})

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# def vote(request, question_id):
# 	p=get_object_or_404(Question, pk=question_id)
# 	try:
# 		selected_choice=p.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):
# 			return render (request, 'polls/deatil.html',{'question':p, 'error_message':"You didn't select a choice",})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model=Question
	template_name = 'polls/deatil.html'


class ResultsView(generic.DetailView):
	model=Question
	template_name = 'polls/results.html'



def vote(request, question_id):
	p=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
			return render (request, 'polls/deatil.html',{'question':p, 'error_message':"You didn't select a choice",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
