import discord
import local_config
import logging
import threading
import time
import random
import glob

#logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

WAIT = 0
PLAYING = 1

player_state = WAIT


def music_player(voich):
    player_state = PLAYING
    cnt = 0
    while True:
        logging.debug('start')
        if player_state == WAIT:
            print('wait')
            break
        
        time.sleep(1)
        cnt += 1
        #print('loop %s' % cnt)
        def after_event(er):
            print("test")
            print('Error check: '+ er)

        if voich.is_playing():
            continue

        print("audio start")
        lst_sound = glob.glob('sound_dir/*.mp3')
        path = random.choice(lst_sound)
        audio = discord.FFmpegPCMAudio(path)
        audio_out = discord.PCMVolumeTransformer(audio, volume=0.06)
        voich.play(audio_out, after=after_event)


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

        def check_error(er):
            print('Error check: '+ er)

        audio = discord.FFmpegPCMAudio('test.mp3')
        audio_out = discord.PCMVolumeTransformer(audio, volume=0.04)
        #audio = discord.FFmpegOpusAudio('test.mp3', bitrate=192)

        voich.play(audio_out, after=check_error)


    if message.content.startswith('/random_play'):
        if message.author.voice is None:
            await message.channel.send('ボイスチャンネルに参加してからコマンドを打ってください。')
            return

        player = threading.Thread(target=music_player, args=(voich,))
        player.start()


TOKEN = local_config.token
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

# すごい
