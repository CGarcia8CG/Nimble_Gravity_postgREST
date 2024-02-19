import psycopg2
import pandas as pd

# Database connection details
dbname = "ces_data"
user = "your_user"
password = "your_password"
host = "your_host"
port = "your_port"

# Connect to PostgreSQL
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

# Mapping for file
month_mapping = {
    'M01': 'January',
    'M02': 'February',
    'M03': 'March',
    'M04': 'April',
    'M05': 'May',
    'M06': 'June',
    'M07': 'July',
    'M08': 'August',
    'M09': 'September',
    'M10': 'October',
    'M11': 'November',
    'M12': 'December'
}

# Read data, transform and insert in tables
chunk_size = 1000  # Adjust the chunk size as needed
for chunk in pd.read_csv('AllSeries.txt', delimiter='\t', chunksize=chunk_size):
    # Skip the header row
    chunk = chunk.iloc[1:]

    # Check if the series_id is "CES9000000010"
    filtered_chunk = chunk[chunk.iloc[:, 0].str.strip() == "CES9000000010"]

    if filtered_chunk.shape[0] > 0:
        print("Found women")

    for index, row in filtered_chunk.iterrows():
        full_month = month_mapping.get(row[2], row[2])
        series = f"{row[0]}_{row[1]}_{row[2]}"
        period = f"{row[1]}_{full_month}"
        # year = int(row[1])  # Uncomment if needed
        sector = "government"
        women = int(row[3])

        # Use psycopg2 to insert data into the table
        cursor.execute("INSERT INTO ces_woman (series, period, sector, women) VALUES (%s, %s, %s, %s)",
                       (series, period, sector, women))

    # Nonsupervisory
    # Check if the series_id is "CES9000000010"
    filtered_chunk2 = chunk[chunk.iloc[:, 0].str.strip() == "CES0500000006"]

    if filtered_chunk2.shape[0] > 0:
        print("Found nonsupervisory")

    for index, row in filtered_chunk2.iterrows():
        full_month = month_mapping.get(row[2], row[2])
        series = f"{row[0]}_{row[1]}_{row[2]}"
        period = f"{row[1]}_{full_month}"
        # year = int(row[1])  # Uncomment if needed
        sector = "private"
        employ = int(row[3])

        # Use psycopg2 to insert data into the table
        cursor.execute("INSERT INTO ces_data_nonsupervisory (series, period, sector, employ) VALUES (%s, %s, %s, %s)",
                       (series, period, sector, employ))

    # Total
    # Check if the series_id is "CES9000000010"
    filtered_chunk3 = chunk[chunk.iloc[:, 0].str.strip() == "CES0500000001"]

    if filtered_chunk3.shape[0] > 0:
        print("Found total")

    for index, row in filtered_chunk3.iterrows():
        full_month = month_mapping.get(row[2], row[2])
        series = f"{row[0]}_{row[1]}_{row[2]}"
        period = f"{row[1]}_{full_month}"
        # year = int(row[1])  # Uncomment if needed
        sector = "private"
        employ = int(row[3])

        # Use psycopg2 to insert data into the table
        cursor.execute("INSERT INTO ces_data_total_private (series, period, sector, employ) VALUES (%s, %s, %s, %s)",
                       (series, period, sector, employ))

# Create views
create_view_query_supervisory = """
    CREATE VIEW supervisory_employment_view AS
    SELECT
        p1.period,
        p1.employ AS "total employ",
        p2.employ AS "nonsupervisory employ",
        (p1.employ - p2.employ) AS "supervisory employment"
    FROM
        ces_data_total_private p1
    INNER JOIN
        ces_data_nonsupervisory p2 ON p1.period = p2.period;
"""

create_view_query_women = ('''CREATE VIEW women_view AS
SELECT
    period,
    women
FROM
    ces_woman;''')

cursor.execute(create_view_query_supervisory)
cursor.execute(create_view_query_women)

#Create Role and grant permisions for postgREST
cursor.execute('''
CREATE ROLE anonymous;
GRANT SELECT ON TABLE supervisory_employment_view TO anonymous;
GRANT SELECT ON TABLE women_view TO anonymous;
''')

# Commit and close the connection
print("Finished")
conn.commit()
conn.close()