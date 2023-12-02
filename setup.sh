#!/bin/bash
kubectl create namespace bookinfo
kubectl create namespace monitoring
kubectl label namespace bookinfo istio-injection=enabled
