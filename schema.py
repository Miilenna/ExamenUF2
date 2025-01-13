# els altres camps que no estàn afegits es perquè son dades personals, 
# per tant son dades sensibles.

def user_registre(users) -> dict:
    return {"nombre": users[0],
            "apellido": users[1],
            "correo": users[2],
            "descripción": users[3],
            "curso": users[4],
            "año": users[5]
            }

def users_registre(users) -> dict:
    return [user_registre(user) for user in users]