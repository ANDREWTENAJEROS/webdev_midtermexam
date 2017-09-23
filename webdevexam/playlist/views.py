from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import SongForm

# Create your views here.
def IndexView(request):
    if request.method == 'POST':
        form = SongForm(data=request.POST)
        if form.is_valid():
            Song = form.save(commit=False)
            Song.save()
            return HttpResponseRedirect(reverse('playlist:index'))
    else:
        form = SongForm()

    context = {'form': form}
    return render(request, 'playlist/index.html', context)
