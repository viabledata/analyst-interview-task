from google.cloud import bigquery

client = bigquery.Client()

# sample query
openaq_query = """
               SELECT location, city, country, value, timestamp
               FROM `bigquery-public-data.openaq.global_air_quality`
               WHERE pollutant = "pm10" AND timestamp > "2019-03-01"
               ORDER BY value DESC
               LIMIT 20
               """

query_job = client.query(openaq_query)

results = query_job.result()  # Waits for job to complete.

# As a very simple example, this prints out the information received
print("Location | City | Country | Value | Timestamp")
for row in results:
    print("{} | {} | {} | {} | {}".format(row.location, row.city, row.country, row.value, row.timestamp))
