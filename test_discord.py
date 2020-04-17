import discord
import local_config

TOKEN = local_config.token

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

print("aa")
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

# 音がなる

# すごい
