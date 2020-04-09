from google.cloud import bigquery
from fn import query as qr
from discord_webhook import DiscordWebhook, DiscordEmbed

import matplotlib.pyplot as plt
import numpy as np
import datetime

def query_to_bigquery(query):
    client = bigquery.Client()
    query_job = client.query(query)
    result = query_job.result()
    dataframe = result.to_dataframe()
    return dataframe

def visualize_bar_chart(x,x_label, y, y_label, title):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    index = np.arange(len(x))
    plt.xticks(index, x, fontsize = 7, rotation=30)
    plt.bar(index, y)
    return plt

def get_and_save_image():
    query = qr.query
    dataframe = query_to_bigquery(query)
    x = dataframe['date'].tolist()
    y = dataframe['users'].tolist()
    plt = visualize_bar_chart(x = x, x_label = 'date', y = y, y_label = 'users', title = 'Daily users')
    plt.savefig('daily.png')

def send_to_discord():
    url = 'https://discordapp.com/api/webhooks/697903828103725128/ovmQsqjoK0R3m6ygO773evESO8gMDkVTFFHeO49XdDNUFIfAXxsC1OrhiJWjDsQH9wDx'
    webhook = DiscordWebhook(url = url, username = 'daily')
    with open('../daily-report/daily.png', 'rb') as f:
        webhook.add_file(file= f.read(), filename = 'daily.png')
    response = webhook.execute()

def main():
    get_and_save_image()
    send_to_discord()

if __name__ == '__main__':
    main()
