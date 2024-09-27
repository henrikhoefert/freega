import requests
import json
from lxml import html
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from os.path import isfile
import config

class logs:
    def __init__(self, filename):
        self.filename = filename

        try: # try to read logfile content
            with open(self.filename, "r+") as f:
                self.content = f.read()
            self.lines    = self.content.split("\n")
            self.lines    = list(filter(("").__ne__, self.lines))
        except OSError as e: # logfile doesn't exist
            with open(self.filename, "a") as f: 
                f.write("") # create logfile
            self.lines    = []

    def is_new(self, string: str): # check if string not in logfile
        for l in self.lines:
            if l == string:
                return False
        return True

    def clear_old(self, dict_list): # remove logfile lines that are not active posts anymore
        title_list = []
        for g in dict_list:
            title_list.append(g["title"]) 

        for l in self.lines:
            if l not in title_list: # if log entry not in title list
                with open(self.filename, "w+") as f:
                    clear_content = self.content.replace(l + "\n", "")
                    f.write(clear_content)

    def add(self, string: str): # add line to logfile
        with open(self.filename, "a") as f:
            f.write(string + "\n")

class platform:
    def list_to_string(platforms: list): # format platform names for api url
        out_str = ""
        for p in platforms:
            if p != platforms[-1]:
                out_str += p + "."
            else:
                out_str += p
        return out_str

    def get_meta(platforms: str): # identify game platform from post and get metadata of said platform
        for p in config.platform_meta:
            if config.platform_meta[p]["alias"] in platforms:
                return config.platform_meta[p]

def find(platforms: str, type: str): # get posts from gamerpower.com api
    if type not in ('game', 'loot', 'beta'):
        raise ValueError("type can only be 'game', 'loot' or 'beta'. Not: '" + type + "'")
    else:
        response = requests.get('https://www.gamerpower.com/api/filter?platform=' + platforms + '&type=' + type)
        
        if response.status_code == 200:
            data = response.json()

            return data

class discord:
    def translate(url, platform_dict, dict): # turn post and platform information into webhook
        webhook = DiscordWebhook(url=url)
        embed   = DiscordEmbed(title=dict["title"], url=dict["gamerpower_url"], color=platform_dict["color"])
        embed.set_author(name=platform_dict["author"], url=platform_dict["url"])
        embed.add_embed_field(name="platform:", value=":video_game: " + dict["platforms"], inline=False)
        embed.add_embed_field(name="description:", value=dict["description"], inline=False)
        embed.add_embed_field(name="instructions:", value=dict["instructions"], inline=False)
        embed.add_embed_field(name="free until:", value=":calendar: " + dict["end_date"], inline=False)
        embed.add_embed_field(name="users:", value=":busts_in_silhouette: " + str(dict["users"]), inline=False)
        embed.add_embed_field(name="price:", value=":dollar: " + dict["worth"], inline=False)
        embed.add_embed_field(name="links:", value=f":gift: [Get Giveaway]({dict['gamerpower_url']})\n:octopus: [GitHub](https://github.com/henrikhoefert/freega)\n:information_source: [Source](https://www.gamerpower.com/)", inline=False)
        embed.set_thumbnail(url=platform_dict["icon"])
        embed.set_image(url=dict["image"])
        embed.set_footer(text="Freega • Free Game Notifier, Discord-Webhook", 
                         icon_url="https://avatars.githubusercontent.com/u/83596694?v=4")
        webhook.add_embed(embed)
        return webhook

    def send(webhook): # send webhook
        return webhook.execute()

    def send_success(execute): # check if sending webhook was a success
        execute_status = execute.status_code
        if execute_status == 200:
            return True
        else:
            return False


if __name__ == "__main__":
    p = platform.list_to_string(config.platforms)
    games = find(platforms=p, type="game")
    for w in config.webhooks:
        logs(w["logfile"]).clear_old(games)
        for g in games:
            if logs(w["logfile"]).is_new(g["title"]):
                p_meta  = platform.get_meta(g["platforms"])
                webhook = discord.translate(w["url"], p_meta, g)
                sending = discord.send(webhook)
                send_success = discord.send_success(sending)
                print("NEW POST: " + g["title"])
                if send_success:
                    logs(w["logfile"]).add(string=g["title"])
                else:
                    print(sending)
            else:
                print("OLD POST: " + g["title"])
