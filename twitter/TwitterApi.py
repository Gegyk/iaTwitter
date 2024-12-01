from Twitter import Authentication as autenticacion
    
cuenta = autenticacion.cuentaTwitter

def getUltimoTweet(username):
    
    try:
        user_response = cuenta.get_user(username=username)

        # Obtener tweets del usuario
        user_id = user_response.data.id  # ID del usuario
        tweets_response = cuenta.get_users_tweets(id=user_id, max_results=5)  # Mínimo permitido: 5

        # Verificar si hay tweets disponibles
        if tweets_response.data:
            # Obtener el último tweet de la lista
            return tweets_response.data
        else:
            return None
    except Exception as error:
        print("Hola soy twitter y e decidido que hasta dentro de nose cuanto tiempo no puedes volver a usar esto: \n")
        print(error) 
        return None