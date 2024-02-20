import requests
import pandas as pd
import sys

def requestLatencyAvg(response_3):
    df = pd.DataFrame.from_dict(response_3.json())
    values = [float(a['value'][1]) for a in df['data']['result']]
    ret = 0 if len(values) == 0 else sum(values)/len(values)
    return ret

def totalBytesExchanged(response_1, response_2):
    df1 = pd.DataFrame.from_dict(response_1.json())
    df2 = pd.DataFrame.from_dict(response_2.json())
    values1 = [int(round(float(a['value'][1]))) for a in df1['data']['result']]
    values2 = [int(round(float(a['value'][1]))) for a in df2['data']['result']]
    return 0 if (not values1) and (not values2) else (sum(values1) + sum(values2))

def getPrometheusData(prometheus_addr):
    response_1 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_request_bytes_sum")  # istio_request_bytes_sum
    response_2 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_response_bytes_sum")  # istio_response_bytes_sum
    response_3 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_request_duration_milliseconds_sum")  # istio_agent_outgoing_latency
    #print(response_3.json(), file=sys.stderr)

    response = (requestLatencyAvg(response_3), totalBytesExchanged(response_1, response_2))

    return response 
