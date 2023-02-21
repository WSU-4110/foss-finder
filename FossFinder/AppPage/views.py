from django.shortcuts import render
from AppPage.models import Software

# Create your views here.
def software_index(request):
    software = Software.objects.all()
    context = {
        'Software': software
    }
    return render(request, 'software_index.html', context)

def software_detail(request, pk):
    software = Software.objects.get(pk=pk)
    context = {
        'Software': software
    }
    return render(request, 'software_detail.html', context)