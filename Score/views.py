from django.shortcuts import render
from .forms import ScoreForm

# Create your views here.
def score_view(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            score = form.cleaned_data['score']
            form.save()
            form = ScoreForm() 
    else:
        form = ScoreForm()
    return render(request, 'Score/Score.html', {'form': form})
