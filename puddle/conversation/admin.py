from django.contrib import admin
from .models import Conversation, Conversationmessage
# Register your models here.


admin.site.register(Conversation)
admin.site.register(Conversationmessage)