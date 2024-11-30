import tweepy

# Bearer token de tu aplicación de Twitter
bearer_token = "AAAAAAAAAAAAAAAAAAAAALgQxQEAAAAA%2F2VwrHmkKJ6G0nv8hpdCNErEitg%3DvAdpySRfoo69f90BWtjrB38taP5Lh0c1GZv44ml5xy44Wa4cz6"

# Crear un cliente de la API con el bearer token
client = tweepy.Client(bearer_token=bearer_token)

# Nombre de usuario de Twitter
username = "EvilAFM"

# Obtener el usuario con el nombre de usuario
user = client.get_user(username=username)

# Obtener los últimos tweets de la cuenta (max 1 tweet)
tweets = client.get_users_tweets(user.id, max_results=1)

# Verificar si hay tweets
if tweets.data:
    print(f"Último tweet de {username}:")
    print(f"- {tweets.data[0].text}")
else:
    print(f"{username} no tiene tweets.")
