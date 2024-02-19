from os import environ
from time import localtime, sleep
import anomaly_detection as ad
import data_query as dq
from prometheus_client import start_http_server, Summary, gauge, counter


if __name__ == "__main__":
    try:
        prometheus = environ['PROMETHEUS_ADDRESS'] + ':' + environ['PROMETHEUS_PORT']
        prev_outliers = set()
        while(True):
            start_http_server(8080)
            g = gauge('Current Anomalies','Current anomalies on network')
            n = gauge('New Anomalies', 'New detected anomalies on network')
            c = counter('Detected Anomalies','Anomalies detected since program started')  
            data = dq.getPrometheusData(prometheus)
            outliers = ad.getOutliers(data) # Index of outliers in 'data'
            new_outliers = outliers - prev_outliers
            if len(outliers) > 0:
                c.inc()
                g.set(len(outliers))
                n.set(new_outliers)

            sleep(15)
    except KeyError:
        print('Prometheus address is not configured, please define the PROMETHEUS_ADDRESS and PROMETHEUS_PORT environment variables')
