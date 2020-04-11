import os
from fn import daily as daily

bancofalabella = daily.DailyReport()
bancofalabella.main(
    ['bancofalabella.pe'],
    [os.getenv('BIGQUERY_DATASET_BANCOFALABELLA')],
    [15],
    os.getenv('DISCORD_URL_BANCOFALABELLA'),
    'app+web'
)

incarail = daily.DailyReport()
incarail.main(
    ['incarail.com'],
    [os.getenv('BIGQUERY_DATASET_INCARAIL')],
    [15],
    os.getenv('DISCORD_URL_INCARAIL'),
    'app+web'
)

tiendaonline = daily.DailyReport()
tiendaonline.main(
    ['tiendaonline.movistar.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MOVISTAR')],
    [15],
    os.getenv('DISCORD_URL_MOVISTAR'),
    '360'
)

catalogo = daily.DailyReport()
catalogo.main(
    ['catalogo.movistar.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MOVISTAR')],
    [15],
    os.getenv('DISCORD_URL_MOVISTAR'),
    '360'
)

publica = daily.DailyReport()
publica.main(
    ['www.movistar.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MOVISTAR')],
    [15],
    os.getenv('DISCORD_URL_MOVISTAR'),
    '360'
)

empresas = daily.DailyReport()
empresas.main(
    ['empresas.movistar.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MOVISTAR')],
    [15],
    os.getenv('DISCORD_URL_MOVISTAR'),
    '360'
)

servicios = daily.DailyReport()
servicios.main(
    ['serviciosmovistar.com'],
    [os.getenv('BIGQUERY_DATASET_MOVISTAR')],
    [15],
    os.getenv('DISCORD_URL_MOVISTAR'),
    '360'
)

soporte = daily.DailyReport()
soporte.main(
    ['soporte.movistar.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MOVISTAR')],
    [15],
    os.getenv('DISCORD_URL_MOVISTAR'),
    '360'
)
