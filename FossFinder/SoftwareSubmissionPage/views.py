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

def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().prefetch_related('rating_set')
    for post in posts:
        rating = post.rating_set.filter(user=request.user).first()
        post.user_rating = rating.rating if rating else 0
    return render(request, "index.html", {"posts": posts})

def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return index(request)