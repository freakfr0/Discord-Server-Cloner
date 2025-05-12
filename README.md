<p align="left"> <img src="https://komarev.com/ghpvc/?username=freakfrv4&label=Profile%20views&color=0e75b6&style=flat" alt="freakfr0" /> </p>

<p align="left"> <a href="https://twitter.com/freakfrv4" target="blank"><img src="https://img.shields.io/twitter/follow/Freak.fr?logo=twitter&style=for-the-badge" alt="freakfr0" /></a> </p>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/freakfrv4" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="freakfr0" height="30" width="40" /></a>
<a href="https://instagram.com/usrfreak.exe" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="usrfreak.exe" height="30" width="40" /></a>
<a href="https://discord.gg/freak.fr" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="freak.fr" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=freakfr0&show_icons=true&locale=en" alt="freakfr0" /></p>
<p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=freakfr0&" alt="freak.fr" /></p>

## Discord Server Cloner
[![version](https://img.shields.io/badge/version-1.0-red)](https://github.com/your-username/your-repo/releases/tag/v1.0.0)
![license](https://img.shields.io/badge/license-MIT-red)

This is a Discord bot that allows you to clone an entire Discord server, including channels, roles, emojis, and server settings, to another server.

## Features
- Clone server settings (name, icon, region, etc.)
- Clone channels (categories, voice channels, text channels)
- Clone roles and role permissions
- Clone emojis
- Asynchronous processing for faster cloning
- User-friendly prompts and error handling

## Requirements
- Python 3.6 or higher
- Discord.py library
- Pypresence library (for Rich Presence)
- Colorama library (for colored console output)
- Inquirer library (for interactive prompts)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/freakfr0/Discord-Server-Cloner.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Discord bot token and server IDs:
   - Create a new Discord application and bot account.
   - Copy the bot token and place it in the `token` variable in the `main.py` file.
   - Copy the IDs of the source and destination servers and place them in the `input_guild_id` and `output_guild_id` variables, respectively.

## Usage
1. Run the bot:
   ```
   python main.py
   ```

2. The bot will prompt you for the authentication token, source server ID, and destination server ID.

3. The bot will then clone the selected server, including channels, roles, emojis, and server settings.

4. After cloning, the bot will display the duration of the cloning process and end the session.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
