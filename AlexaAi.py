# Â©  - MetaVoid (Moezilla) And Alexa Team For Modification
# Give Credit â£ï¸Day

from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from os import getenv
import re
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME", None)
MONGO_URL = getenv("MONGO_URL", None)

client = Client(SESSION_NAME, API_ID, API_HASH)

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in client.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

@client.on_message(
    filters.command("repo", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.delete()
    alexaai = await message.reply("ð")
    await asyncio.sleep(1)
    await alexaai.edit("**ð ððð©ð¨ ð¢ð¬ ðð«ðð¢ð¯ð­ð ð**")
    await asyncio.sleep(1)
    await alexaai.edit("**ð ðð¨ð¯ð ð²ð¨ð® ð**")
    await alexaai.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("CAACAgQAAxkBAAIBNGPBGEjm8t1RHGY0J_BheWhzKYZbAAIWEAACpvFxHvvJk-2D25XRLQQ")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/21941841a9fca15ea39e7.jpg",
        caption=f"""ââââââââââââââââââââââ
ð¥ ð ðð¨ð°ðð«ðð®ð¥ ðð¢ ðð¨ð­ ð¨ð ððð§ð ð«ðð¦.

âââââââââââââââââââ
ð¥ ððð­ðððð¬ð ðððð¤ðð§ð ðð¨ð­ ðð¨ð« ðð ..
âââââââââââââââââââ
â£â¤ ðð«ððð­ð¨ð« â [ððð§ð ð«ðð¦](https://t.me/The_Sangram)
â£â¤ ðð®ðð¬ðð«ð¢ðð ð¨ð§ â [ðð¨ð®ðð®ðð](https://youtube.com/@Official_Sangram)
â£â¤ ðð®ð©ð©ð¨ð«ð­ â [ðð®ð©ð©ð¨ð«ð­](https://t.me/WorldChattingFriendsWCF)
â£â¤ ðð©ððð­ðð¬ â [ðð©ððð­ðð¬](https://t.me/WCFnetwork)
â£â¤ ðð¨ð®ð«ðð ðð¨ðð â [ððð«ð](https://github.com/OpQueenbots/Shreya-Chatbot)
â£â¤ ðð°ð§ðð« â [ððð§ð ð«ðð¦ ð±ð](https://t.me/Sangram_XD)
âââââââââââââââââââ

ð¥ ðð ð²ð¨ð® ð¡ðð¯ð ðð§ð² ðªð®ðð¬ð­ð¢ð¨ð§ð¬ ð­ð¡ðð§ ðð¨ð§ð­ððð­ ðð² [ðð°ð§ðð«](https://t.me/The_Sangram)""",
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**ðð¡ð«ðð²ð ðð¬ðð«ðð¨ð­ ð¢ð¬ ðð¨ð«ð¤ð¢ð§ð  ðð¨ð« ðð¡ðð­ð­ð¢ð§ð **")

@client.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    alexadb = MongoClient(MONGO_URL)    
    alexa = alexadb["AlexaDb"]["Alexa"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                ""
            )
    is_alexa = alexa.find_one({"chat_id": message.chat.id})
    if not is_alexa:
        alexa.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"á´Êá´á´ÊÉªá´ Éªs á´Éªsá´ÊÊá´á´ ÊÊ {message.from_user.mention()} Òá´Ê á´sá´Ês ÉªÉ´ {message.chat.title}")
    if is_alexa:
        await message.reply_text(f"á´Êá´á´ÊÉªá´ Éªs á´ÊÊá´á´á´Ê á´Éªsá´ÊÊá´á´")
    

@client.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    alexadb = MongoClient(MONGO_URL)    
    alexa = alexadb["AlexaDb"]["Alexa"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "Êá´á´ á´Êá´ É´á´á´ á´á´á´ÉªÉ´"
            )
    is_alexa = alexa.find_one({"chat_id": message.chat.id})
    if not is_alexa:           
        await message.reply_text(f"á´Êá´á´ÊÉªá´ Éªs á´ÊÊá´á´á´Ê á´É´á´ÊÊá´á´")
    if is_alexa:
        alexa.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"á´Êá´á´ÊÉªá´ Éªs á´É´á´ÊÊá´á´ ÊÊ {message.from_user.mention()} Òá´Ê á´sá´Ês ÉªÉ´ {message.chat.title}")
    

@client.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**á´sá´á´É¢á´:**\n/chatbot [on|off] á´É´ÊÊ É¢Êá´á´á´")

    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       if not is_alexa:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_alexa:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexastickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       if not is_alexa:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_alexa:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
