from django.shortcuts import render
from .forms import SubmitSoftwareForm
#from SoftwareSubmissionPage import SubmittedSoftware
from django.http import HttpResponse

# Create your views here.
def software_submit(request):
    form = SubmitSoftwareForm
    return render(request, 'software_submit.html', {'form':form})
