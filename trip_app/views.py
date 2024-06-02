from django.shortcuts import render
from trip_app.models_mongo import Message
from trip_app.models import User

# Create your views here.
def main(request):
    messages = []
    if request.user.is_authenticated:
        messages_from_user = list(Message.objects(sender_id=request.user.id))
        # messages_to_user = list(Message.objects(receiver_id=request.user.id))
        messages = messages_from_user #+ messages_to_user

        for message in messages:
            user_id = message.sender_id
            user = User.objects.get(id=user_id)
            message.user = user
        
    return render(request, 'index.html', context={'messages': messages})
