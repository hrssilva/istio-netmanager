import requests
import pandas as pd
import sys

def outgoingLatencyAvg(response_3):
    df = pd.DataFrame.from_dict(response_3.json())
    values = [float(a['value'][1]) for a in df['data']['result']]
    print(values,file=sys.stderr)
    ret = sum(values)/len(values)
    return ret

def getPrometheusData(prometheus_addr):
    response_1 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_request_bytes_sum")  # istio_request_bytes_sum
    response_2 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_response_bytes_sum")  # istio_response_bytes_sum
    response_3 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_agent_outgoing_latency")  # istio_agent_outgoing_latency
    #print(response_3.json(), file=sys.stderr)

    response = (outgoingLatencyAvg(response_3))

    return response
