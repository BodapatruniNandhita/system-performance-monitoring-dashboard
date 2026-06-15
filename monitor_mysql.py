import psutil
import mysql.connector
from datetime import datetime
import time
import os

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    database=os.getenv("MYSQL_DATABASE", "system_monitoring")
)

cursor = conn.cursor()

while True:

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    net = psutil.net_io_counters()
    bytes_received = net.bytes_recv
    bytes_sent = net.bytes_sent

    query = """
    INSERT INTO system_metrics
    (timestamp, cpu_usage, memory_usage, disk_usage,
     bytes_received, bytes_sent)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        datetime.now(),
        cpu,
        memory,
        disk,
        bytes_received,
        bytes_sent
    )

    cursor.execute(query, values)
    conn.commit()

    print("Data inserted successfully!")

    time.sleep(10)   # collect data every 10 seconds
