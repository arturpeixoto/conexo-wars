from django import forms
from .models import DailyLeaderboard, Player
from datetime import date


class GameForm(forms.ModelForm):
    class Meta:
        model = DailyLeaderboard
        fields = "__all__"
        labels = {
            "name": "Nome da música",
            "date": "Data do jogo",
            "score": "Pontuação do dia",
        }
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "value": date.today().strftime('%Y-%m-%d')
                    }
            )
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'email']  # Campos a serem exibidos no formulário
