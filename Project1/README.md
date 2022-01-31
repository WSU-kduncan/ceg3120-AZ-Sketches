# Guide to Discord Bot

## Setup
  - Obtain the bot's API token by going to Discord Developer Portal and navigate to Applications.
  - Select the bot under My Applications and go to Bot.
  - Select Copy under the text "Click to Reveal Token".
    - The token will be placed in a file called ".env", paste the token after the following:
      - DISCORD_TOKEN={TOKEN HERE}
    - Certain libraries will be needed to run the script as well. Enter the following commands to install them:
      - pip3 install -U discord.py
      - pip3 install -U python-dotenv

## Usage
  - The bot initially responds to the message "towel!" and delivers hitchhiker quotes randomly. It is also able to quote Brooklyn 99 if you comment out the commands responsible for providing this response.
  - Changes were made to the bot's code to being employed as a coffee brewer that responds to the message "Coffee!". Type the message and you will get a fresh cup of coffee as well as an entertaining one liner.

## Concluding Notes
  - The bot will stop running when the command finishes on the running instance. To make sure that the bot stays running even after the instance is closed, you must host the program on a server and not on a local machine.
  - A server essentially is a computer waiting for other computers to interact with it. Once contacted, the program will respond in some way. Servers also do not go down often, unlike other computers running locally, so it will be accessible at any time.
