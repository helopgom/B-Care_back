from django.http import JsonResponse, HttpResponse
import openai
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

# Asegurarte de que estás utilizando la API Key correcta
@csrf_exempt
def conversacion_ia(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('user_text')

            # Usar el nuevo método openai.ChatCompletion.create
            response = openai.ChatCompletion.create(
                model="gpt-4",  # O el modelo que tengas acceso, como gpt-3.5-turbo
                messages=[
                    {"role": "system", "content": "Tú eres un asistente útil."},
                    {"role": "user", "content": user_input},
                ]
            )

            return JsonResponse({'response': response['choices'][0]['message']['content']})
        except Exception as e:
            # Devuelve más información sobre el error para depuración
            return JsonResponse({'error': str(e)}, status=500)

    return HttpResponse("Método no permitido. Usa POST para enviar datos.", status=405)
