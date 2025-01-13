from connection import connexio

def add_user(nombre, apellido, correo, descripción, curso, año, dirección, codigo_postal, contraseña):
    conn = connexio()
    cur = conn.cursor()
    try: 
        query = "insert into registre (nombre, apellido, correo, descripción, curso, año, dirección, codigo_postal, contraseña) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (nombre, apellido, correo, descripción, curso, año, dirección, codigo_postal, contraseña)
        cur.execute(query, values)
        conn.commit()
        return {
            "status": 1,
            "message": "S'ha insertat"
        }
    except Exception as e:
        return {
            "status": -1,
            "message": "error"
        }
    finally:
        cur.close()
        conn.close()