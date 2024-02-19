# Nimble_Gravity_postgREST
Instructions for Challenge

Usage of postgREST to expose data (Views in this case) in JSON format.
There are 3 files
- CreateDB_and_tables.sql
- populate_tables.py
- postgrest.conf

It's very impportant to put postgrest.conf in the right folder, this is the one that has the postgrest.exe file

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How to Run](#how-to-run)
- [Views](#views)

## Installation
You need to have postgres and python
Also you need a web browser, Chrome is prefered.

### PostgREST
```bash
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
scoop install postgrest
```

### Python Packages

```bash
pip install psycopg2 pandas
```

## Usage
### For Database, tables, views, role creation and table population
```powershell
$psqlPath = "path\to\PostgreSQL\version\bin\psql.exe"
$databaseUser = "your_user"
$databaseHost = "your_host"
$databasePort = "your_port"
$scriptPath = "path\to\folder\with\CreateDB_and_tables.sql"
& "$psqlPath" -U $databaseUser -h $databaseHost -p $databasePort -f $scriptPath

cd path\to\folder\with\populate_tables.py
python populate_tables.py

```

## How to Run
```bash
cd path\to\postgrest\folder
postgrest postgrest.conf
```
Open in browser

http://localhost:3000/supervisory_employment_view
or
http://localhost:3000/women_view

## Views (results)
Women view result example
![Women View](https://github.com/CGarcia8CG/Nimble_Gravity_postgREST/blob/main/women_view.png)

Supervisory view result example
![Supervisory view](https://github.com/CGarcia8CG/Nimble_Gravity_postgREST/blob/main/supervisory_view.png)

