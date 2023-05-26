"""Class to send Discord webhooks"""

import discord
from datetime import datetime


class Embed:
	def __init__(self, webhook_url):
		self.webhook_url = webhook_url
		self.connector()

	def connector(self):
		"""Creates partial webhook from webhook url"""
		webhook = self.webhook_url.split("/")
		self.webhook = discord.SyncWebhook.partial(webhook[-2], webhook[-1])

	def send_embed(self, location):
		"""Creates discord embed and sends it to webhook url"""
		embed = discord.Embed(title=f"Treatment Start Time for {location['name']} (UTC)")

		for farm in location['locations']: # Add each farm field to the embed object
			embed.add_field(name=farm['name'], value=f"Start: {farm['times']['twilight_start']}\nEnd: {farm['times']['twilight_end']}", inline=False)

		embed.set_footer(text=f"Date: {datetime.today().date()}")
		self.webhook.send(embed=embed, avatar_url="")
		