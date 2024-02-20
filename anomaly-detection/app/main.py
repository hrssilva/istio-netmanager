from os import environ
from time import localtime, sleep
import anomaly_detection as ad
import data_query as dq
import sys
from prometheus_client import start_http_server, Gauge, Counter
import traceback


if __name__ == "__main__":
    try:
        prometheus = environ['PROMETHEUS_ADDRESS'].strip("'") + ':' + environ['PROMETHEUS_PORT'].strip("'")
        neighbors = int(environ['KNN_NEIGHBORS'])
        wait_time = int(environ['WAIT_SEC'])
        max_count = int(environ['MAX_ELEMENTS_COUNT'])
        try:
            sleep(wait_time)
            prev_outliers = set()
            data = []
            start_http_server(9090)
            g = Gauge('current_anomalies','Current anomalies on network')
            n = Gauge('new_anomalies', 'New detected anomalies on network')
            c = Counter('detected_anomalies','Anomalies detected since program started')
            _, prev_bytes = dq.getPrometheusData(prometheus)
            sleep(wait_time)
            while(True):
                x, total_bytes = dq.getPrometheusData(prometheus)
                y = (total_bytes - prev_bytes) / wait_time
                print("Data Queried " + str(x) + " " + str(y))
                data.append([x, y])
                outliers = ad.getOutliers(data, neighbors) # Index of outliers in 'data'
                new_outliers = outliers - prev_outliers
                prev_outliers = outliers
                if len(outliers) > 0:
                    print("Anomaly Ocurred ",[data[o] for o in outliers])
                    c.inc()
                    g.set(len(outliers))
                    n.set(len(new_outliers))
                if len(data) >= max_count:
                    data.pop(0)
                sleep(wait_time)
        except :
            print('Unknown Error')
            traceback.print_exc()
    except KeyError:
        print('Environment Error')
