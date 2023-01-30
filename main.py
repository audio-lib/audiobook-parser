import asyncio

import telethon
import db
import config

dat = db.Connection()


async def save(post_id: int, author: str, title: str):
    dat.save_record(link=f'https://t.me/aitu_lib/{post_id}', author=author, title=title)


async def send_post(client: telethon.TelegramClient, file_id, message: str) -> int:
    resp = await client.send_message(entity='aitu_lib', file=file_id, message=message)
    return resp.id


async def parse_messages():
    cfg = config.get_config()
    client = telethon.TelegramClient(cfg.username, cfg.api_id, cfg.api_hash)
    await client.connect()
    print('client created')
    channel = await client.get_entity('flibusta_anglysky')
    async for message in client.iter_messages(channel):
        if hasattr(message.media, 'document') and hasattr(message.media.document,
                                                          'mime_type') and 'audio' in message.media.document.mime_type:
            name = message.message.split("\n\n")
            title = name[0]
            author = name[1]
            print(title[2:], author[9:], sep='\t')
            print(message.media.document.id)
            print(telethon.utils.pack_bot_file_id(message.media.document))
            # print(vars(message))
            idx = await send_post(client, message.media.document, f'🔥{title[2:]}\n👤{author[9:]}')
            await save(post_id=idx, title=title[2:], author=author[9:])


def main():
    asyncio.run(parse_messages())


if __name__ == '__main__':
    main()
