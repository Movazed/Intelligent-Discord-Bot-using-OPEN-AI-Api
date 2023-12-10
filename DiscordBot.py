#APPLICATION ID: 1183260755701792778
#PUBLC KEY: 80738a0d19130590c077a57e9f6dce3446ffe6a75581e210a170a354565ea225
#TOKEN = MTE4MzI2MDc1NTcwMTc5Mjc3OA.GJLuu2.mTGeXtoukxDRwU2sqjMfwEcp8ueCF5zb41QvN4
#OPENAI API= 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
#OPENAI API2= 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

import discord
import os
from openai import OpenAI

discord_token='MTE4MzI2MDc1NTcwMTc5Mjc3OA.GJLuu2.mTGeXtoukxDRwU2sqjMfwEcp8ueCF5zb41QvN4'
api_key='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'
client = OpenAI(api_key=api_key)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message.mentions)
        if self.user!=message.author:
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
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)
                

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE4MzI2MDc1NTcwMTc5Mjc3OA.GJLuu2.mTGeXtoukxDRwU2sqjMfwEcp8ueCF5zb41QvN4')
