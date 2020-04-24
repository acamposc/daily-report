import os
import time
from fn import daily as daily

slp = time.sleep(1)


mapfre_www = daily.DailyReport()
mapfre_www.main(
    ['www.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)



mapfre_soat = daily.DailyReport()
mapfre_soat.main(
    ['soat.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)

 

mapfre_salud = daily.DailyReport()
mapfre_salud.main(
    ['salud.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)



mapfre_alarmas = daily.DailyReport()
mapfre_alarmas.main(
    ['alarmas.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)




mapfre_accidentes = daily.DailyReport()
mapfre_accidentes.main(
    ['seguro-accidentes.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)



mapfre_sctr = daily.DailyReport()
mapfre_sctr.main(
    ['sctr.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)



mapfre_app = daily.DailyReport()
mapfre_app.main(
    ['apps.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)



mapfre_vehicular = daily.DailyReport()
mapfre_vehicular.main(
    ['seguro-vehicular.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)

 

mapfre_landing = daily.DailyReport()
mapfre_landing.main(
    ['landing.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)




mapfre_viajes = daily.DailyReport()
mapfre_viajes.main(
    ['seguro-de-viaje.mapfre.com.pe'],
    [os.getenv('BIGQUERY_DATASET_MAPFRE')],
    [15],
    os.getenv('DISCORD_URL_MAPFRE'),
    '360'
)



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

