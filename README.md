# Analyst Interview Task

We would like you to perform some analysis on one of the following open data sets:

*   the [OpenAQ data set](https://www.kaggle.com/open-aq/openaq) data set that tracks global air pollution measurements, and draw out some insights.

*   the [Hacker News](https://www.kaggle.com/hacker-news/hacker-news) data set that contains summary information of all stories and comments from Hacker News from its launch in 2006.

What analyses you perform and how you present the insights is up to you.

We look forward to seeing what you create!

## Getting started

First you will need to set up a service account in [GCP](https://console.cloud.google.com). NB. billing must be enabled on your account, but this exercise should be within the free usage limits.

*   In the GCP Console, go to the [create service account private key](https://console.cloud.google.com/apis/credentials/serviceaccountkey) page.
*   From the **Service account** list, select **New service account**.
*   In the **Service account name** field, enter a name.
*   From the **Role** list, select **Project > Owner**.
*   Click **Create**. A JSON file that contains your key downloads to your computer.

To use this, you will  need to set an environment variable in your terminal session that specifies where to find your token:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=<Path to the JSON file you just downloaded>

# check that it is set correctly before proceeding
echo $GOOGLE_APPLICATION_CREDENTIALS
```

> NB. If you close your terminal session, you will need to repeat the step setting this environment variable (or add it to your shell profile)

You may also need to enable the BigQuery API on your account. This can be done [here](https://console.cloud.google.com/flows/enableapi?apiid=bigquery). Select the project in which you created the account service and click **Continue**. This will enable the BigQuery API service.

Now prepare the Python environment (assumes that you already have [Python 3.7.14](https://docs.python.org/3.7/library/venv.html) or newer installed). From your working directory run:

```bash
python3 -m virtualenv env
source env/bin/activate
pip install --upgrade pandas google-cloud-bigquery
```

## Retrieving and analysing the datasets

You can now use Python to retrieve and analyse the data. The following can be placed in a file and run (or grab the file from [here](example.py)). This example uses the OpenAQ dataset.

```python
from google.cloud import bigquery

client = bigquery.Client()

# sample query from:
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
```

Please adjust the sample query to return different cuts of the data, possibly taking multiple snapshots over time or for different pollutants. You can [view some of the possible filters on their website](https://openaq.org/#/locations).

We expect that Pandas would probably be useful for the analysis, but don't feel restricted - we are interested to see how you approach this task.
