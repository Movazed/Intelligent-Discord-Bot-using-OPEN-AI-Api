import discord
import os
from openai import OpenAI


os.environ['DISCORD_TOKEN'] = 'MTE4MzI2MDc1NTcwMTc5Mjc3OA.GJLuu2.mTGeXtoukxDRwU2sqjMfwEcp8ueCF5zb41QvN4'
DISCORD_TOKEN = 'MTE4MzI2MDc1NTcwMTc5Mjc3OA.GJLuu2.mTGeXtoukxDRwU2sqjMfwEcp8ueCF5zb41QvN4'
api_key = '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'
client = OpenAI(api_key=api_key)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message.mentions)
        if self.user != message.author:
            if self.user in message.mentions:               
                channel = message.channel
                response = client.completions.create(
                    model="gpt-3.5-turbo-instruct-0914",
                    prompt=message.content,
                    temperature=1.28,
                    max_tokens=200,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                message_to_send = response.choices[0].text
                await channel.send(message_to_send)

# Use environment variable for Discord token
discord_token = os.getenv('DISCORD_TOKEN')

if discord_token is None:
    print("DISCORD_TOKEN environment variable is not set.")
else:
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(discord_token)
