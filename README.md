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
```powershell
$psqlPath = "C:\Program Files\PostgreSQL\14\bin\psql.exe"
$databaseUser = "postgres"
$databaseHost = "localhost"
$databasePort = "5432"
$scriptPath = "C:\Users\Xande\OneDrive\Escritorio\NimbleGravity\CreateDB_and_tables.sql"
& "$psqlPath" -U $databaseUser -h $databaseHost -p $databasePort -f $scriptPath

cd C:\Users\Xande\OneDrive\Escritorio\NimbleGravity
python populate_tables.py

cd path\to\postgrest\folder
postgrest postgrest.conf
```
## How to Run

## Views (results)
