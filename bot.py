import discord
import openai
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_KEY
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

personality_prefix = "Bạn là một cô gái 16 tuổi, dễ thương, nhí nhảnh, tinh nghịch. Bạn luôn trả lời một cách vui vẻ, trẻ trung và hơi bướng."

@client.event
async def on_ready():
    print(f"Bot đã đăng nhập với tên {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mentioned_in(message) or message.content.startswith("!chat"):
        prompt = message.content.replace("!chat", "").replace(f"<@{client.user.id}>", "").strip()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": personality_prefix},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content
        await message.channel.send(reply)

client.run(TOKEN)
