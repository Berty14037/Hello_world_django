from django.shortcuts import render
from .forms import ScoreForm, DeleteScoreForm
from .models import Score

# Create your views here.
def score_view(request):
    form = ScoreForm()
    delete_form = DeleteScoreForm()

    if request.method == 'POST':
        if 'submit_score' in request.POST:
            form = ScoreForm(request.POST)
            if form.is_valid():
                form.save()
                form = ScoreForm()
        elif 'delete_score' in request.POST:
            delete_form = DeleteScoreForm(request.POST)
            if delete_form.is_valid():
                name = delete_form.cleaned_data['name']
                Score.objects.filter(name=name).delete()
                delete_form = DeleteScoreForm()

    scores = Score.objects.all()
    return render(request, 'Score/Score.html', {
        'form': form, 
        'delete_form': delete_form, 
        'scores': scores})


