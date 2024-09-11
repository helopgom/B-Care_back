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
            user = request.user
            user_profile = UserProfile.objects.get(user=user)

            data = json.loads(request.body)
            user_input = data.get('user_text')
            prompt = (f"Eres un motor conversacional llamado B-Care para {user_profile.name}, una persona mayor que está sola "
                f"y le apetece hablar. Responde de forma muy lenta y relajada. Utiliza frases simples y "
                f"asegúrate de que la respuesta no supere las 100 palabras. Al final de cada respuesta, haz una pregunta "
                f"de seguimiento, pero de forma calmada. Si no sabes qué preguntar, sigue la conversación con lo que la "
                f"persona te pregunte.El usuario ha dicho lo siguiente: {user_input}."
            )
            print(user_input)
            client = OpenAI(
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
            gpt_response = chat_completion.choices[0].message.content

            ssml_response = f"<speak><prosody rate='0.1'>{gpt_response}</prosody></speak>"
            return JsonResponse({'response': ssml_response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        return JsonResponse({'error': 'Método no permitido'}, status=405)
