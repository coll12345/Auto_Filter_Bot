# Don't Remove Credit @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import openai

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

async def ai(query):
    if not OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY is not configured')
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=query,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.9,
        timeout=5,
    )
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        question = message.text.split(' ', 1)[1]
        response = await ai(question)
        await m.edit(f'{response}')
    except Exception as e:
        await m.edit(f'An error occurred: {e}')
