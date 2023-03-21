from django.shortcuts import render
from .models import SubmittedSoftware
from .forms import SubmitSoftwareForm

# Create your views here.
def software_submit(request):
    form = SubmitSoftwareForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = SubmitSoftwareForm()

    return render(request, 'software_submit.html', {'form':form})

def software_submit_detail(request, pk):
    software = SubmittedSoftware.objects.get(pk=pk)
    context = {
        'SubmittedSoftware': software
    }
    return render(request, 'software_submit_detail.html', context)