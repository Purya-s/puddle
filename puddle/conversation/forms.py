from django import forms
from .models import Conversationmessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = Conversationmessage
        fields = ('content',)
        widjets = {
                'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            })
        }