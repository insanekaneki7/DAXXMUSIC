from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ 🥀 ᴀʟʟ sᴇʀᴠɪᴄᴇ ᴘʀᴏᴠɪᴅᴇᴅ ʙʏ ~ ɪɴsᴀɴᴇᴛᴇᴀᴍ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("🥂𝘼𝘿𝘿 𝙈𝙀 𝘽𝘼𝘽𝙔😎", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("⚡𝙃𝙀𝙇𝙋⚡", url="https://t.me/insaneupdate"),
          InlineKeyboardButton("⚡𝙊𝙒𝙉𝙀𝙍⚡", url="https://t.me/abtkaneki"),
          ],
               [
                InlineKeyboardButton("⚡𝘿𝙀𝙑⚡", url="https://t.me/Oghoneyy"),

],
[
              InlineKeyboardButton("⚡𝘽𝘼𝙉𝘼𝙇𝙇⚡", url=f"https://t.me/insanebanall_bot?startgroup=true"),
              InlineKeyboardButton("︎⚡𝙈𝙐𝙎𝙄𝘾⚡", url=f"https://t.me/Kavyaa_music_bot?startgroup=true"),
              ],
              [
              InlineKeyboardButton("⚡𝙈𝘼𝙉𝘼𝙂𝙀𝙈𝙀𝙉𝙏⚡", url=f"https://t.me/insanemanager_bot?startgroup=true"),
InlineKeyboardButton("⚡𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏⚡", url=f"https://t.me/insanecopyright_bot?startgroup=true"),
],
[
InlineKeyboardButton("⚡𝘾𝙊 𝙊𝙒𝙉 𝘽𝙊𝙏⚡", url=f"https://t.me/insanerepo"),
InlineKeyboardButton("⚡𝙉𝙀𝙏𝙒𝙊𝙍𝙆⚡", url=f"https://t.me/INSANE_NETWORK"),
],
[
              InlineKeyboardButton("⚡𝙑𝙎𝘾⚡", url=f"https://t.me/insanerepo"),
              InlineKeyboardButton("⚡𝙈𝘼𝙄𝙉 𝘾𝙃𝘼𝙏⚡", url=f"https://t.me/insanesociety"),
              ],
              [
              InlineKeyboardButton("⚡𝙎𝙏𝙍𝙄𝙉𝙂⚡", url=f"https://t.me/Honey_stringgenbot?startgroup=true"),
InlineKeyboardButton("⚡𝙒𝘼𝙄𝙁𝙐𝙎", url=f"https://t.me/insanegrabber_bot?startgroup=true"),
],
[
InlineKeyboardButton("⚡𝙏𝙀𝙍𝙈𝙄𝙉𝘼𝙏𝙀𝙍𝙎⚡", url=f"https://t.me/insanedestroyer"),
InlineKeyboardButton("⚡𝙋𝙍𝙀𝘿𝘼𝙏𝙊𝙍⚡", url=f"https://t.me/Predatorcopyright"),
],
[
InlineKeyboardButton("⚡𝘾HAT⚡", url=f"https://t.me/insanesociety"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/9bd66462402feb557a928.png",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://t.me/insanerepo/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/insanerepo) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/abtkaneki)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
