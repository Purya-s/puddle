from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
                'content': forms.Textarea(attrs={
                'class': 'w-2/3 py-4 px-6 rounded-xl border'
            })
        }