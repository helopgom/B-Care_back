from django.http import JsonResponse, HttpResponse
import openai
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def conversacion_ia(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('user_text')

        # Generar la respuesta usando GPT-4
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=f"El usuario dice: {user_input}, responde acorde a sus intereses.",
            max_tokens=150
        )

        return JsonResponse({'response': response.choices[0].text.strip()})

    # Si es una solicitud GET, devolver un mensaje indicando que solo POST está permitido
    return HttpResponse("Método no permitido. Usa POST para enviar datos.", status=405)
