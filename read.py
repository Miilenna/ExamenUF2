from connection import connexio

def read_user():
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM Registre;")
    text = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return text