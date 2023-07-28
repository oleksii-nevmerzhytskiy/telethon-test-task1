import json
import os
from dotenv import load_dotenv
from telethon import TelegramClient, sync

load_dotenv()
api_id = os.getenv('TELETHON_API_ID')
api_hash = os.getenv('TELETHON_API_HASH')

# Отримання id групи
# with TelegramClient('anon', api_id, api_hash) as client:
#     dialog_list = []
#     for dialog in client.get_dialogs():
#         dialog_list.append([dialog.title, dialog.id])
#     for dialog in dialog_list:
#         print(dialog)

session_id = os.getenv('TELETHON_API_SESSION')
group_id = -1001414591747

with TelegramClient(session_id, api_id, api_hash) as client:
    group = client.get_entity(group_id)
    participants = client.get_participants(group)

    participant_list = {}
    for participant in participants:
        participant_list[participant.username] = {
            'first_name': participant.first_name,
            'last_name': participant.last_name
        }

json = json.dumps(participant_list, indent=4, ensure_ascii=False)
print(json)

with open('json_file.json', 'w') as file:
    file.write(json)
    file.close()
