Додаток для планування подорожів

Написати додаток, який дозволить користувачам планувати подорожі в популярні міста та залишати про них відгуки.

Який також дозволить додавати інформацію про користувача, додавати друзів та надсилати їм повідомлення.

Використовувати Postgres для зберігання користувачів (id, name, email, password, preferences), подорожей (id, user_id, trip_name, start_date, end_date, destination), друзів (user_id, friend_id) та відгуків (id, user_id, destination, rating)

Використовувати Mongo для збереження профілю користувача (user_id, bio, interests, travel_history) та повідомлень (sender_id, receiver_id, message_content, timestamp)