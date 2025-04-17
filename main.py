from os import system
import psutil
import os
from pypresence import Presence
import time
import sys
import discord
import subprocess
import json
from rich.table import Table
from rich.console import Console
from rich.style import Style
from rich.panel import Panel as RichPanel
from rich.text import Text
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
import inquirer
from cloner import Clone

version = '0.3'
clones = {'Clones_teste_feitos': 0}
versao_python = sys.version.split()[0]

console = Console()


from os import system
from colorama import Style, Fore

def clearall():
    system('cls')  # Use 'clear' for Unix-like systems

# Print the ASCII art
from os import system
from colorama import Style, Fore

def clearall():
    system('cls')  # Use 'clear' for Unix-like systems

# Print the ASCII art along with the final message
print(f"""{Style.BRIGHT}{Fore.RED}
    .....             .         s                                                ...                ..                                                   
 .H8888888h.  ~-.    @88>      :8                                             xH88"`~ .x8X    x .d88"                                                    
 888888888888x  `>   %8P      .88                   u.    u.                :8888   .f"8888Hf  5888R          u.      u.    u.                 .u    .   
X~     `?888888hx~    .      :888ooo       u      x@88k u@88c.             :8888>  X8L  ^""`   '888R    ...ue888b   x@88k u@88c.      .u     .d88B :@8c  
'      x8.^"*88*"   .@88u  -*8888888    us888u.  ^"8888""8888"             X8888  X888h         888R    888R Y888r ^"8888""8888"   ud8888.  ="8888f8888r 
 `-:- X8888x       ''888E`   8888    .@88 "8888"   8888  888R              88888  !88888.       888R    888R I888>   8888  888R  :888'8888.   4888>'88"  
      488888>        888E    8888    9888  9888    8888  888R              88888   %88888       888R    888R I888>   8888  888R  d888 '88%"   4888> '    
    .. `"88*         888E    8888    9888  9888    8888  888R              88888 '> `8888>      888R    888R I888>   8888  888R  8888.+"      4888>      
  x88888nX"      .   888E   .8888Lu= 9888  9888    8888  888R              `8888L %  ?888   !   888R   u8888cJ888    8888  888R  8888L       .d888L .+   
 !"*8888888n..  :    888&   ^%888*   9888  9888   "*88*" 8888"              `8888  `-*""   /   .888B .  "*888*P"    "*88*" 8888" '8888c. .+  ^"8888*"    
'    "*88888888*     R888"    'Y"    "888*""888"    ""   'Y"                  "888.      :"    ^*888%     'Y"         ""   'Y"    "88888%       "Y"      
        ^"***"`       ""              ^Y"   ^Y'                                 `""***~"`        "%                                 "YP'                 
                                                                                                                                                                                                                                                                                                                 {Style.RESET_ALL}{Fore.WHITE}{Fore.RESET} bot by naitik.exe_""")

# Wait for user input to continue
input(f'{Style.BRIGHT}{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}{Fore.RESET}')

# Clear the screen afterwards
clearall()




client = discord.Client()
if os == "Windows":
    system("cls")
else:
    print(chr(27) + "[2J")
    clearall()
while True:
    token = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Please enter your authentication token to continue:{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    guild_s = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Enter the ID of the server you wish to replicate (Source Server):{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    guild = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Enter the ID of the target server where the copied content will be pasted (Destination Server):{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    clearall()
    print(f'{Style.BRIGHT}{Fore.GREEN}You have entered the following details:')
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Authentication Token: {Fore.YELLOW}{token}{Style.RESET_ALL}{Fore.RESET}'
    )
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Source Server ID: {Fore.YELLOW}{guild_s}{Style.RESET_ALL}{Fore.RESET}'
    )
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Destination Server ID: {Fore.YELLOW}{guild}{Style.RESET_ALL}{Fore.RESET}'
    )
    confirm = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Are all details correct? {Fore.YELLOW}(Y/N){Style.RESET_ALL}{Fore.RESET}\n >'
    )
    if confirm.upper() == 'Y':
        if not guild_s.isnumeric():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}The server ID to replicate should only contain numbers.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if not guild.isnumeric():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}The destination server ID should only contain numbers.{Style.RESET_ALL}{Fore.RESET}'
            )
            print(
                f'{Style.BRIGHT}{Fore.RED}One or more fields are blank.{Style.RESET_ALL}{Fore.RESET}'
            )
            
            print(
                f'{Style.BRIGHT}{Fore.RED}One or more fields have less than 3 characters.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        break

    elif confirm.upper() == 'N':
        clearall()
else:
    clearall()
    print(
        f'{Style.BRIGHT}{Fore.RED}Invalid option. Please enter Y or N.{Style.RESET_ALL}{Fore.RESET}'
    )
input_guild_id = guild_s
output_guild_id = guild
token = token
clearall()


@client.event
async def on_ready():
    try:
        start_time = time.time()
        global clones
        table = Table(title="Versions", style="bold magenta")
        table.add_column("Component")
        table.add_column("Version")
        table.add_row("Cloner", str(version), style="cyan")
        table.add_row("Discord.py", str(discord.__version__), style="cyan")
        table.add_row("Python", str(versao_python), style="cyan")
        console.print(RichPanel(table, width=47))
        console.print(
            RichPanel(f" Successful authentication",
                      style="bold green",
                      width=47))
        console.print(
            RichPanel(
                f" Hello, {client.user.name}! Starting Cloner...",
                style="bold blue",
                width=47))
        print(f"\n")
        questions = [
            inquirer.List(
                'clone_emojis',
                message="\033[35mDo you want to clone emojis?\033[0m",
                choices=['\033[32mYes\033[0m', '\033[31mNo\033[0m'],
            ),
        ]
        answers = inquirer.prompt(questions)
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.guild_edit(guild_to, guild_from)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        end_time = time.time()
        duration = end_time - start_time
        duration_str = time.strftime("%M:%S", time.gmtime(duration))
        if answers['clone_emojis'] == '\033[32mYes\033[0m':
            print(
                f"{Style.BRIGHT}{Fore.YELLOW}Cloning emojis in progress. This may take a few moments."
            )
            await asyncio.sleep(20)
            await Clone.emojis_create(guild_to, guild_from)
            print(
                f"{Style.BRIGHT}{Fore.BLUE}The server was successfully cloned in {Fore.YELLOW}{duration_str}{Style.RESET_ALL}"
            )
            clones['Clones_teste_feitos'] += 1
            with open('saves.json', 'w') as f:
                json.dump(clones, f)
            print(
                f"{Style.BRIGHT}{Fore.BLUE}Finalizing process and ending session on account {Fore.YELLOW}{client.user}"
            )
            await client.close()  
    except discord.LoginFailure:
        print(
            "Could not authenticate to the account. Check if the token is correct."
        )
    except discord.Forbidden:
        print("Could not clone due to insufficient permissions.")
    except discord.HTTPException:
        print("An error occurred communicating with the Discord API.")
    except discord.NotFound:
        print(
            "Could not find one of the copy elements (channels, categories, etc.)."
        )
    except Exception as e:
        print(Fore.RED + "An error occurred:", e)


try:
    client.run(token, bot=False)
except discord.LoginFailure:
    print(Fore.RED + "The inserted token is invalid")
    print(
        Fore.YELLOW +
        "\n\nThe code will be restarted in 10 seconds. If you don't want to wait, refresh the page and start again."
    )
    print(Style.RESET_ALL)
    time.sleep(10)
    print(Fore.RED + "Restarting...")
