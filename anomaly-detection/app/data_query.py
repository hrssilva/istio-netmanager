import requests
import pandas as pd

def outgoingLatencyAvg(response_3):
    df = pd.read_json(response_3)
    print(df)
    # ret = df.sum(data.result.value) # descobrir qual a col 
    return df

def getPrometheusData(prometheus_addr):
    response_1 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_request_bytes_sum")  # istio_request_bytes_sum
    response_2 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_response_bytes_sum")  # istio_response_bytes_sum
    response_3 = requests.get("http://" + prometheus_addr + "/api/v1/query?query=istio_agent_outgoing_latency")  # istio_agent_outgoing_latency
    
    response = (outgoingLatencyAvg(response_3), response_1.data.result.value + response_2.data.result.value)

    return response
