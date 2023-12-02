#!/bin/bash
kubectl apply -f services/
kubectl apply -f monitors/

kubectl -n istio-system get service istio-ingressgateway
