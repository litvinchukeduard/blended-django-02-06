from django.db import models
from django.contrib.auth.models import User

# Використовувати Postgres для зберігання користувачів (id, name, email, password, preferences), '
# подорожей (id, user_id, trip_name, start_date, end_date, destination), 
# друзів (user_id, friend_id) та відгуків (id, user_id, destination, rating)

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_name = models.CharField(max_length=100)
    start_date = models.DateField() 
    end_date = models.DateField()
    destination = models.CharField(max_length=50)
