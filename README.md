# Nimble_Gravity_postgREST
Instructions for Challenge

Brief description of your project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How to Run](#how-to-run)
- [Views](#views)
- [License](#license)

## Installation
You need to have postgres and python

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
## Views (results)
