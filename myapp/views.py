from django.shortcuts import render
from django.http import JsonResponse
from .forms import FeedbackForm
# Create your views here.
def index(request):
    return render(request, 'index.html')


def your_view_name(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # ডেটা ডাটাবেসে সেভ
            return JsonResponse({'message': 'success'})
        else:
            return JsonResponse({'message': 'fail', 'errors': form.errors}, status=400)
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form})