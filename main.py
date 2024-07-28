from typing import Any, Coroutine, Optional
from datetime import datetime
from discord.interactions import Interaction
import requests
import discord 
import json
from discord import utils, app_commands
from discord.ext import commands
from colorama import init, Fore
from configparser import ConfigParser


init(autoreset=True) 

config = ConfigParser() 
with open("config.json") as f: 
    config = json.load(f) 

token = config["discord_token"] 

intents = discord.Intents.all()

client = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True, self_client=True)


@client.tree.command(name="drop", description="Drops product(s) to user.")
@commands.has_permissions(administrator=True)
async def drop(interaction: discord.Interaction, user: discord.User, amount: int, type: int):
    if interaction.guild is None:
        return await interaction.response.send_message("You can't use this command in DMs.", ephemeral=True)
    
    if interaction.user.id != 747912150521086112 and interaction.user.id != 1017173526047899750:
        return await interaction.response.send_message("You can't use this command.", ephemeral=True)
    else:
            if type == 1:
                file = "nitro.txt"
            elif type == 2:
                file = "nitrobc.txt"
            elif type == 3:
                file = "spotify.txt"
            elif type == 4:
                file = "netflix.txt"    
            elif type == 5:
                file = "disney.txt"  
            elif type == 6:
                file = "crunchyroll.txt"        
            else:
                return await interaction.response.send_message("Invalid type.", ephemeral=True)
    
            try:
                with open(file, "r") as f:
                    nitros = f.readlines()

                if amount > len(nitros):
                    return await interaction.response.send_message("Not enough URLs available.", ephemeral=True)
        
                message = f"""
<:tw_money:1242493360800006226> **__THANK YOU FOR ORDERING!__** <:tw_money:1242493360800006226> 

**Here's your Product! <a:1_ngnitroboost:1242493372862562374> <a:2_Nitro_Basic54:1242493370186596472> <:Spotify:1249430062315606047> <:Netflix:1249430136336683108> <:Disney:1249430259041042566> <:crunchyroll:1249430327605203004>**

<a:CH_IconVoteYes:1166852061590200433> Don't forget to vouch for your warranty! <a:star:1189342370081292298>
<a:CH_IconVoteYes:1166852061590200433> Always recheck and save your links. <a:star:1189342370081292298>
<a:CH_IconVoteYes:1166852061590200433> Strictly No Claim warranty after receiving the Product. <a:star:1189342370081292298>

**Vouch Here for your warranty:** https://discord.com/channels/1242475283051708519/1242490189104812173 <a:heart:1189341588229460141>
"""
                sent_nitros = nitros[:amount] 

                for i, sent_nitro in enumerate(sent_nitros):
                    sent_nitros[i] = f"{i + 1}. || {sent_nitro.strip()} ||\n"

                for sent_nitro in sent_nitros:
                    message += sent_nitro
                    nitros = nitros[amount:]
        
                with open(file, "w") as f:
                    f.writelines(nitros)
        
                class View(discord.ui.View):
                    def __init__(self) -> None:
                        super().__init__(timeout=None)
                await user.send(message)
                banana = View()
                banana.add_item(discord.ui.Button(label=f"Sent Product(s) to {user.name}", style=discord.ButtonStyle.green, custom_id="vouch", disabled=True))
                banana.timeout = None
                await interaction.response.send_message(f"""
Sent {amount} Product(s) to {user.mention}.
- Thank you for buying from us <a:heart:1189341588229460141>
- Leave a vouch in https://discord.com/channels/1242475283051708519/1242490189104812173 <a:heart:1189341588229460141>
- This message may appear as **direct or request** message.
    """, view=banana)
    
            except Exception as e:
                print(e)

@client.tree.command(name="restock", description="Restocks.")
@commands.has_permissions(administrator=True)
async def restock(interaction: discord.Interaction, account_data: str, type: int):

    if interaction.guild is None:
        return await interaction.response.send_message("You can't use this command in DMs.", ephemeral=True)
    else:
        if interaction.user.id != 747912150521086112 and interaction.user.id != 1017173526047899750:
            return await interaction.response.send_message("You can't use this command.", ephemeral=True)
        if type == 1:
            file = "nitro.txt"
        elif type == 2:
            file = "nitrobc.txt"
        elif type == 3:
            file = "spotify.txt"
        elif type == 4:
            file = "netflix.txt"    
        elif type == 5:
            file = "disney.txt"
        elif type == 6:
            file = "crunchyroll.txt"   
        else:
            return await interaction.response.send_message("Invalid type.", ephemeral=True)
        try:
            temp_stock = account_data
    
            f = open(file, "a", encoding="utf-8")
            f.write(f"{temp_stock}\n")
            f.close()
            lst = temp_stock.split("\n")
            return await interaction.response.send_message(f"Restocked {len(lst)} accounts in {file}.", ephemeral=True)
        except Exception as e:
            print(e)
            return await interaction.response.send_message(f"Error: {e}", ephemeral=True)

@client.tree.command(name="stock", description="Shows the current stock.")
@commands.has_permissions(administrator=True)
async def stock1(interaction: discord.Interaction):
    try:
        class stock(discord.ui.View):
            def __init__(self) -> None:
                super().__init__(timeout=None)
        with open("nitro.txt", "r") as f:
            nitro_codes = f.readlines()
        with open("nitrobc.txt", "r") as f:
            nitro_codes2 = f.readlines()
        with open("spotify.txt", "r") as f:
            spotify_codes3 = f.readlines()
        with open("netflix.txt", "r") as f:
            netflix_codes4 = f.readlines()    
        with open("disney.txt", "r") as f:
           disney_codes5 = f.readlines()        
        with open("crunchyroll.txt", "r") as f:
           crunchyroll_codes6 = f.readlines()         
        banana = stock()
        banana.add_item(discord.ui.Button(label=f"Nitro Boost ({len(nitro_codes)})", style=discord.ButtonStyle.grey,emoji="<a:boost:1185006268025409536>" ,custom_id="stock1", disabled=True))
        banana.add_item(discord.ui.Button(label=f"Nitro Basic ({len(nitro_codes2)})", style=discord.ButtonStyle.grey, emoji="<a:basic:1185006501924966471>",custom_id="stock2", disabled=True))
        banana.add_item(discord.ui.Button(label=f"Spotify Premium ({len(spotify_codes3)})", style=discord.ButtonStyle.grey, emoji="<:Spotify:1185006884592300040>",custom_id="stock3", disabled=True)) 
        banana.add_item(discord.ui.Button(label=f"Netflix ({len(netflix_codes4)})", style=discord.ButtonStyle.grey, emoji="<:Netflix:1236106942510927933>",custom_id="stock4", disabled=True))
        banana.add_item(discord.ui.Button(label=f"Disney+ ({len(disney_codes5)})", style=discord.ButtonStyle.grey, emoji="<:Disney:1185043020639371357>",custom_id="stock5", disabled=True))
        banana.add_item(discord.ui.Button(label=f"Crunchyroll ({len(crunchyroll_codes6)})", style=discord.ButtonStyle.grey, emoji="<:crunchyroll:1185025083014647888>",custom_id="stock6", disabled=True))
        await interaction.response.send_message(view=banana)
    except Exception as e:
        await interaction.response.send_message(f"Error {e}")
        print(e)

@client.event
async def on_ready():
    activity = discord.Game(name=".gg/st0re", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(Fore.CYAN + "Bot is currently running.")
    await client.tree.sync()

client.run(token)