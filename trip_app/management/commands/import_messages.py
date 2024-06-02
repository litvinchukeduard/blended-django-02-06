import json
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from trip_app.models_mongo import Message


class Command(BaseCommand):
    help = "Import messages from json file"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **options):
        json_file_name = options['json_file']
        with open(json_file_name, 'r') as json_file:
            messages = json.load(json_file)
            for message in messages:
                sender_id = message['sender_id']
                receiver_id = message['receiver_id']
                message_content = message['message_content']
                timestamp = datetime.strptime(message['timestamp'], '%Y-%m-%dT%H:%M:%S')

                mongo_message = Message(
                    sender_id=sender_id,
                    receiver_id=receiver_id,
                    message_content=message_content,
                    timestamp=timestamp
                )
                mongo_message.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully loaded messages')
            )
