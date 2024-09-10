from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from openai import OpenAI
from users.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def conversacion_ia(request):
    if request.method == 'POST':
        try:
            # Obtener el perfil del usuario autenticado
            user = request.user
            user_profile = UserProfile.objects.get(user=user)

            data = json.loads(request.body)
            user_input = data.get('user_text')
            prompt = f"Eres un motor conversacional llamado B-Care para {user_profile.name}, una persona mayor que está sola y le apetece hablar. Al acabar de hablar de forma coherente , pregunta sobre alguno de sus temas de interés como {user_profile.preferences or ''}.Si no tiene preferencias, o si estas son nulas, o none sigue la conversación con lo que la persona te pregunta. Responde con un lenguaje sencillo y con respuestas que no superen las 200 palabras.Su fecha de cumpleaños es {user_profile.birth_date}, lo puedes felicitar cuando sea ese día. El usuario ha dicho lo siguiente: {user_input}"
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
                        "content": prompt,
                    }
                ],
                model="gpt-4",
            )

            return JsonResponse({'response': chat_completion.choices[0].message.content})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

