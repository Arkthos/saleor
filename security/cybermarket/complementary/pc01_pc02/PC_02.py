import json
import uuid
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# PC-02: Proteccion contra enumeracion de usuarios
URL = "http://localhost:8000/graphql/"
CARPETA = Path("evidencias_PC_02")
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


def normalizar(respuesta):
    # Comparamos los campos relevantes de GraphQL.
    # No comparamos el email, porque cambia por escenario.
    registro = respuesta.get("data", {}).get("accountRegister")

    if registro is None:
        return {
            "errores_generales": respuesta.get("errors"),
            "http_error": respuesta.get("http_error"),
            "conexion_error": respuesta.get("conexion_error"),
            "detalle": respuesta.get("detalle")
        }

    usuario = registro.get("user")

    return {
        "user_presente": usuario is not None,
        "user_id": usuario.get("id") if usuario else None,
        "errores_registro": registro.get("errors"),
        "errores_generales": respuesta.get("errors", [])
    }


correo_existente = "pc01-prueba01@example.com"
correo_nuevo = f"pc02-auto-{uuid.uuid4().hex[:10]}@example.com"
password = "NuevaClave9!X"

print("Ejecutando PC-02.1: correo existente...")
respuesta_existente = consultar_graphql(correo_existente, password)

print("Ejecutando PC-02.2: correo nuevo...")
respuesta_nueva = consultar_graphql(correo_nuevo, password)

normalizada_existente = normalizar(respuesta_existente)
normalizada_nueva = normalizar(respuesta_nueva)

comparacion_valida = (
    "data" in respuesta_existente
    and "data" in respuesta_nueva
    and respuesta_existente.get("data", {}).get("accountRegister") is not None
    and respuesta_nueva.get("data", {}).get("accountRegister") is not None
)

if not comparacion_valida:
    conclusion = "NO_CONCLUYENTE_ERROR_DE_SOLICITUD"
elif normalizada_existente == normalizada_nueva:
    conclusion = "RESPUESTAS_EQUIVALENTES"
else:
    conclusion = "RESPUESTAS_DIFERENTES"

resultado = {
    "prueba": "PC-02",
    "correo_existente": correo_existente,
    "correo_nuevo": correo_nuevo,
    "respuesta_existente": respuesta_existente,
    "respuesta_nueva": respuesta_nueva,
    "comparacion_existente": normalizada_existente,
    "comparacion_nueva": normalizada_nueva,
    "conclusion": conclusion
}

archivo = CARPETA / "resultados.json"

with open(archivo, "w", encoding="utf-8") as f:
    json.dump(resultado, f, indent=4, ensure_ascii=False)

print("\nRESULTADOS PC-02")
print("PC-02.1:", normalizada_existente)
print("PC-02.2:", normalizada_nueva)
print("CONCLUSION:", conclusion)
print("Evidencia guardada en:", archivo.resolve())
