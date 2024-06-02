from django.db import models
from django.contrib.auth.models import User

# Використовувати Postgres для зберігання користувачів (id, name, email, password, preferences), '
# подорожей (id, user_id, trip_name, start_date, end_date, destination), 
# друзів (user_id, friend_id) та 
# відгуків (id, user_id, destination, rating)


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_name = models.CharField(max_length=100)
    start_date = models.DateField() 
    end_date = models.DateField()
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Trip({self.trip_name}, {self.start_date}, {self.end_date})"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)
    rating = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"Review({self.user}, {self.destination}, {self.rating})"


class Destination(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Destination({self.name})"
    

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')

    def __str__(self) -> str:
        return f"The {self.user} is friend of {self.friend}"
