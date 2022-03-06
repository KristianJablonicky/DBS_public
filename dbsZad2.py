import json
import http.client, urllib.parse
import psycopg2
import os

print(os.getenv('DB_Meno'), os.getenv('DB_Heslo'))
print(os.environ.get('DB_Meno'))


databaza = psycopg2.connect(dbname='dota2', user='USER', password='HESLO', host='147.175.150.216', port='5432', sslmode='require')

kurzor = databaza.cursor()
kurzor.execute("SELECT VERSION()")
fetch = kurzor.fetchall()

#vysledok = '{"version":"PostgreSQL 12.3 on amd64-portbld-freebsd12.1, compiled by FreeBSD clang version 8.0.1 (tags/RELEASE_801/final 366581) (based on LLVM 8.0.1), 64-bit","dota2_db_size": "4347"}'
pgsql = '{"pgsql":{'
vysledok = '"version": "'
for x in fetch:
    vysledok = vysledok + "". join(x)

vysledok += '",'

kurzor = databaza.cursor()
kurzor.execute("SELECT pg_database_size('dota2')/1024/1024 as dota2_db_size")
fetch = kurzor.fetchall()

vysledok += '"dota2_db_size": '
for x in fetch:
    x = str(x)
    x = x[1:-2]
    print(x)
    vysledok += x
    

vysledok = pgsql + vysledok + '}}'

print(vysledok)

jsonVysledok = json.dumps(json.loads(vysledok), indent = 4)

print(jsonVysledok)