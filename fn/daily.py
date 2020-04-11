import matplotlib.pyplot as plt
import numpy as np
import os
import time

from datetime import datetime
from google.cloud import bigquery
from discord_webhook import DiscordWebhook, DiscordEmbed
from fn import query as qr

class DailyReport:
    def __init__(self):
        self.today = datetime.today().strftime('%Y-%m-%d')
        self.ts = time.time()
    
    def query_to_bigquery(self, query):
        self.client = bigquery.Client()
        self.query_job = self.client.query(query)
        self.result = self.query_job.result()
        self.dataframe = self.result.to_dataframe()
        return self.dataframe

    def visualize_bar_chart(self,x,x_label, y, y_label, title):
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        self.index = np.arange(len(x))
        plt.xticks(self.index, x, fontsize = 7, rotation=30)
        plt.bar(self.index, y, color=np.random.rand(3,))
        return plt

    def get_and_save_image(self, hostname, dataset, days, ga):
        self.query = qr.query(hostname, dataset, days, ga)
        dataframe = self.query_to_bigquery(self.query)
        x = dataframe['date'].tolist()
        y = dataframe['users'].tolist()
        plt = self.visualize_bar_chart(
            x = x, 
            x_label = 'date', 
            y = y, 
            y_label = 'users', 
            title = f'Daily user count for {hostname}'
            )
        #plt.savefig(f'{ts}.png')
        plt.savefig(f'{hostname}-{self.ts}.png')
        plt.close(fig='all')

    def send_to_discord(self, hostname, discord_url):
        self.url = discord_url
        webhook = DiscordWebhook(url = self.url, username = 'daily')
        with open(f'{hostname}-{self.ts}.png', 'rb') as f:
            webhook.add_file(
                file= f.read(), 
                filename = f'{hostname}-{self.ts}.png'
                )
        response = webhook.execute()

    def main(self, hostname, dataset, days, discord_url, ga):
        self.get_and_save_image(hostname, dataset, days, ga)
        self.send_to_discord(hostname, discord_url)
