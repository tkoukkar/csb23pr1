# from django.contrib.auth.decorators import login_required    # Required for the fix to broken access control (lines 52, 78, 94)
# import html    # Required for the fix to security against injection (lines 82, 100)

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice
from .forms import AddPollForm, AddChoiceForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get(self, request, pk):
        """Redirect to results if user has already voted on this question."""
        # (And yes, this should be refactored.)
        
        user = request.user
        question = get_object_or_404(Question, pk=pk)
        
        if user in question.alrvoted.all():
            return HttpResponseRedirect(reverse('polls:results', args=(pk,)))
        else:
            return render(request, 'polls/detail.html', {'question': question})
        
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# @login_required    # Extra security against unauthenticated voting (FLAW 1); see also fixes in urls.py.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # user = request.user    # Security against voting multiple times as the same authenticated user
    # if user in question.alrvoted.all():
    #    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
	
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        question.alrvoted.add(request.user)
        question.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# @login_required    # Fix against force browsing by unauthorized users (FLAW 1)
def add_poll(request):
    if request.method == 'POST':
        qtxt = request.POST['question_text']    # Allows injection (FLAW 2)
        # qtxt = html.escape(request.POST['question_text'])    # Fix to the above
        pubd = request.POST['pub_date']
        
        q = Question.objects.create(question_text = qtxt, pub_date = pubd)
        q.save()
        
        return HttpResponseRedirect(reverse('polls:add_choices', args=(q.id,)))
    else:
        form = AddPollForm()
    
    return render(request, 'polls/add_poll.html', {'form': form})

# @login_required    # Fix against force browsing by unauthorized users (FLAW 1)
def add_choices(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        ctxt = request.POST['choice_text']    # Allows injection (FLAW 2)
        # ctxt = html.escape(request.POST['choice_text'])    # Fix to the above
        
        c = Choice.objects.create(question=question, choice_text = ctxt)
        c.save()
        
        return HttpResponseRedirect(reverse('polls:add_choices', args=(question.id,)))    # Return to this same view so another choice may be added
    else:
        form = AddChoiceForm()
    
    return render(request, 'polls/add_choice.html', {'form': form, 'question' : question})