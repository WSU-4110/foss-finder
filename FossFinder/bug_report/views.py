from django.shortcuts import render
from .models import SubmittedBugs
from .forms import SubmitBugsForm

# Create your views here.
def bug_submit(request): 
    form = SubmitBugsForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = SubmitBugsForm()
    return render(request, 'bug_submit.html', {'form':form})

def bug_submit_detail(request, pk):
    bugs = SubmittedBugs.objects.get(pk=pk)
    context = {
        'SubmittedBugs': bugs
    }
    return render(request, 'bug_submit_detail.html', context)