import discord
import openai
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# Cài đặt API key OpenAI
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
    
    print(f"Nhận được tin nhắn từ {message.author}: {message.content}")

    # Nếu bạn muốn bot phản hồi mọi tin nhắn
    if True:  # Điều kiện này có thể thay đổi tùy thuộc vào nhu cầu
        prompt = message.content.strip()

        # Sử dụng API OpenAI với cú pháp mới
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # hoặc model phù hợp khác
            messages=[
                {"role": "system", "content": personality_prefix},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response['choices'][0]['message']['content'].strip()
        await message.channel.send(reply)

client.run(TOKEN)
