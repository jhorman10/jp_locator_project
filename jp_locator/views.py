from django.shortcuts import render
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Coordenadas de las antenas
wonderfulAntena1 = [-25, -10]
wonderfulAntena2 = [5, -5]
wonderfulAntena3 = [25, 5]


def get_location(*distances):
    # Implementar la lógica para calcular la ubicación basada en las distancias
    x = (wonderfulAntena1[0] + wonderfulAntena2[0] + wonderfulAntena3[0]) / 3
    y = (wonderfulAntena1[1] + wonderfulAntena2[1] + wonderfulAntena3[1]) / 3
    return x, y


def get_message(*messages):
    # Implementar la lógica para combinar los mensajes
    message = " ".join([m for m in messages if m])
    return message


@csrf_exempt
def obtener_ubicacion_y_mensaje(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            antenas = data.get("antenas", [])
            distances = [antena.get("distance", 0) for antena in antenas]
            messages = [antena.get("message", []) for antena in antenas]

            x, y = get_location(*distances)
            message = get_message(*messages)

            response_data = {
                "position": {"x": x, "y": y},
                "message": message,
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Carga JSON inválida"}, status=400)

    return JsonResponse({"error": "Método de solicitud inválido"}, status=405)
