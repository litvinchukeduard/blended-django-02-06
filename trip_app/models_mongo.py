# Використовувати Mongo для збереження профілю користувача (user_id, bio, interests, travel_history) 
# та повідомлень (sender_id, receiver_id, message_content, timestamp)

from mongoengine import Document, EmbeddedDocument, StringField, ListField, IntField, DateTimeField


class TravelHistory(EmbeddedDocument):
    trip_id = IntField(unique=True)
    description = StringField()


class UserProfile(Document):
    bio = StringField()
    interests = ListField(StringField()) # ['tennis', 'badminton', ...]
    travel_history = ListField(TravelHistory())


class Message(Document):
    sender_id = IntField()
    receiver_id = IntField()
    message_content = StringField(max_length=300)
    timestamp = DateTimeField()

# {
#     "bio": "...",
#     "interests": "...",
#     "travel_history": {
#         "trip_id": "1",
#         "description": "..."
#     }
# }