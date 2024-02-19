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
        try:
            prev_outliers = set()
            data = []
            start_http_server(9090)
            g = Gauge('Current_Anomalies','Current anomalies on network')
            n = Gauge('New_Anomalies', 'New detected anomalies on network')
            c = Counter('Detected_Anomalies','Anomalies detected since program started')
            while(True):
                x, y = dq.getPrometheusData(prometheus)
                print("Data Queried " + str(x) + " " + str(y))
                data.append([x, y])
                outliers = ad.getOutliers(data, neighbors) # Index of outliers in 'data'
                print("Data Queried " + str(x) + " " + str(y))
                new_outliers = outliers - prev_outliers
                if len(outliers) > 0:
                    print("Anomaly Ocurred ",[data[o] for o in outliers])
                    c.inc()
                    g.set(len(outliers))
                    n.set(new_outliers)

                sleep(wait_time)
        except :
            print('Unknown Error')
            traceback.print_exc()
    except KeyError:
        print('Environment Error')
