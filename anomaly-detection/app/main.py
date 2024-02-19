from os import environ
from time import localtime, sleep
import anomaly_detection as ad
import data_query as dq


if __name__ == "__main__":
    try:
        prometheus = environ['PROMETHEUS_ADDRESS'] + ':' + environ['PROMETHEUS_PORT']
        while(True):
            data = dq.getPrometheusData(environ[''])
            outliers = ad.getOutliers(data) # Index of outliers in 'data'
            if len(outliers) > 0:
                pass # Give warning to prometheus
            sleep(15)
    except KeyError:
        print('Prometheus address is not configured, please define the PROMETHEUS_ADDRESS and PROMETHEUS_PORT environment variables')
