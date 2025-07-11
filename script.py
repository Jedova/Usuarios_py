from usuario import Usuario
import datetime
import json
import pytz

tz_CL = pytz.timezone("America/Santiago")

instancias =[]
with open("usuarios.txt") as u:
    linea=u.readline()
    while linea:
        if not linea.strip():
            linea = u.readline()
            continue
        try:
            usuario = json.loads(linea)
            instancias.append(Usuario(
                usuario.get("nombre"),
                usuario.get("apellido"),
                usuario.get("email"),
                usuario.get("genero")
            ))
        except Exception as e:
            datetime_CL = datetime.datetime.now(tz_CL)
            with open("error-log", "a+") as log:
                log.write(f"el error es: {datetime_CL.strftime('%d/%m/%Y %H:%M:%S')}, {e} \n")
        finally:
            linea = u.readline()
for u in instancias:
    print(u)