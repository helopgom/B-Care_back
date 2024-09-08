from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from openai import OpenAI

# Asegurarte de que estás utilizando la API Key correcta
@csrf_exempt
def conversacion_ia(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('user_text')
            print(user_input)
            # Usar el nuevo método openai.ChatCompletion.create
            client = OpenAI(
                # This is the default and can be omitted
                api_key=os.environ.get("OPENAI_API_KEY"),

            )

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="gpt-4",
            )

            return JsonResponse({'response': chat_completion.choices[0].message.content})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
