
from django import forms
from .models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['C_Title', 'C_Artist', 'C_Album','C_lyrics']
        labels = {'C_Title': 'Song Title', 'C_Artist': 'Song Artist','C_Album': 'Song Album' ,'C_lyrics': 'Song Lyrics'}
