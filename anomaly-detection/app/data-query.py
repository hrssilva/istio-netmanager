import requests
import prometheus-client
import pandas as pd

def outgoing_latency_avg(response_3):
    df = pd.readjson(response_3)
    ret = df.sum(data.result.value) # descobrir qual a col 
    return ret

def get_prometheus_data(prometheus_addr):
    response_1 = requests.get("http://" + prometheus_addr + ":3000/api/v1/query?query=istio_request_bytes_sum")  # istio_request_bytes_sum
    response_2 = requests.get("http://" + prometheus_addr + ":3000/api/v1/query?query=istio_response_bytes_sum")  # istio_response_bytes_sum
    response_3 = requests.get("http://" + prometheus_addr + ":3000/api/v1/query?query=istio_agent_outgoing_latency")  # istio_agent_outgoing_latency
    
    response = (outgoing_latency_avg(response_3), response_1 +response_2)

    return response