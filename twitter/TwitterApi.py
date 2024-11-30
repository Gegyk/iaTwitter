from twitter import Authentication as autenticacion

class TwitterApi:
    
    cuenta = autenticacion.cuentaTwitter

    #def obtenerTweet():clea
    
    def obtenerSeguidos(username="IasPaco36305"):
        
         # Obtener el usuario usando el nombre de usuario (username) en API V2
        user = autenticacion.cuentaTwitter.get_user(username=username)

        # Mostrar el nombre de usuario consultado
        print(f"Usuarios seguidos por {user.data['username']}:")

        # Usamos el método get_users_following() para obtener los usuarios seguidos
        # Este método es el adecuado para la API V2 y no debería causar el error 403
        following = autenticacion.cuentaTwitter.get_users_following(id=user.data['id'])

        # Mostrar los resultados
        if following.data:
            for friend in following.data:
                print(f"- {friend.username}")
        else:
            print("No se encontraron usuarios seguidos.")
