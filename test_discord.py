import discord
import local_config

client = discord.Client()
 
@client.event
async def on_ready():
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global voich

    # bot return
    if message.author.bot:
        return
    
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    def check_error(er):
        print('Error check: '+ er)
    
    # 接続
    if message.content.startswith('/connect'):
        voich = await discord.VoiceChannel.connect(message.author.voice.channel)
    # 切断
    if message.content.startswith('/discon'):
        await voich.disconnect()

    if message.content.startswith('/play'):
        if message.author.voice is None:
            await message.channel.send('ボイスチャンネルに参加してからコマンドを打ってください。')
            return
        audio = discord.FFmpegPCMAudio('test.mp3')
        audio_out = discord.PCMVolumeTransformer(audio, volume=0.025)
        #audio = discord.FFmpegOpusAudio('test.mp3', bitrate=192)
        
        voich.play(audio_out, after=check_error)

TOKEN = local_config.token
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

# すごい
