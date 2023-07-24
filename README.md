## Practicum welcowe bot
Telegram bot with welocme info for Yandex Practicum.

The bot is available here - https://t.me/evgenii_welcome_bot

The bot deployed on the [Yandex Cloud service](https://cloud.yandex.ru/)
## Commands description
* /get_latest_photo - returns my most recent photo 
* /get_high_school_photo - returns my highschool photo 
* /hobby - short description of my favorite hobby 
* /repository - link to github repository 
* /listen_audio - returns 3 audio messages to choose from
* /send_message_to_evgenii - send me a message via the bot

## How to deploy the bot locally

1. Write an `.env` file with your `TELEGRAM_TOKEN` in it and other env vars.
2. Run `docker-compose up -d` and wait for the build to finish.

That's it. Enjoy your the bot. 🚀