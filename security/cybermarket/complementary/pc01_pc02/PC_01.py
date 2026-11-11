import json
import uuid
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# PC-01: Validacion de contrasenas
URL = "http://localhost:8000/graphql/"
CARPETA = Path("evidencias_PC_01")
CARPETA.mkdir(exist_ok=True)

MUTACION = """
mutation Registrar($email: String!, $password: String!) {
  accountRegister(
    input: {
      email: $email
      password: $password
      redirectUrl: "http://localhost:3000/"
    }
  ) {
    user {
      id
      email
    }
    errors {
      field
      message
      code
    }
  }
}
"""

CASOS = [
    ("PC-01.1", "Numerica debil", "12345678"),
    ("PC-01.2", "Contrasena comun", "password123"),
    ("PC-01.3", "Contrasena robusta", "Ab7!qR92#Lm5"),
]


def consultar_graphql(email, password):
    datos = {
        "query": MUTACION,
        "variables": {
            "email": email,
            "password": password
        }
    }

    solicitud = Request(
        URL,
        data=json.dumps(datos).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(solicitud, timeout=20) as respuesta:
            return json.loads(respuesta.read().decode("utf-8"))
    except HTTPError as error:
        return {
            "http_error": error.code,
            "detalle": error.read().decode("utf-8")
        }
    except (URLError, TimeoutError) as error:
        return {"conexion_error": str(error)}


resultados = []
identificador = uuid.uuid4().hex[:8]

for numero, (codigo, tipo, password) in enumerate(CASOS, 1):
    email = f"pc01-auto-{identificador}-{numero}@example.com"

    respuesta = consultar_graphql(email, password)

    registro = respuesta.get("data", {}).get("accountRegister")

    if registro is None:
        estado = "ERROR_DE_SOLICITUD"
    elif registro.get("errors"):
        estado = "RECHAZADA_POR_VALIDACION"
    elif respuesta.get("errors"):
        estado = "ERROR_GRAPHQL"
    else:
        estado = "SIN_ERRORES_REPORTADOS"

    resultados.append({
        "caso": codigo,
        "tipo": tipo,
        "email": email,
        "longitud_password": len(password),
        "estado": estado,
        "respuesta": respuesta
    })

    print(codigo, ":", estado)
    print("Correo:", email)
    print("-" * 45)

archivo = CARPETA / "resultados.json"

with open(archivo, "w", encoding="utf-8") as f:
    json.dump(resultados, f, indent=4, ensure_ascii=False)

print("\nPC-01 FINALIZADA")
print("Evidencia guardada en:", archivo.resolve())
