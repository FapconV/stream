import os




#dotenv_path = join(dirname(__file__), '.env')
#load_dotenv(dotenv_path)

DELAY = 0.01
NUM_PARTITIONS = 3
OUTLIERS_GENERATION_PROBABILITY = 0.2
KAFKA_BROKER = "http://103.249.77.22:9092/"
TRANSACTIONS_TOPIC = "random_cpu_usage"
TRANSACTIONS_CONSUMER_GROUP = "Random_CPU_Usage"
PREDICTION_TOPIC = "Random_CPU_Usage_Predictions"
PREDICTION_CONSUMER_GROUP = "Random_CPU_Usage_Predictions"

SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN")
SLACK_CHANNEL = "anomalies-alerts"