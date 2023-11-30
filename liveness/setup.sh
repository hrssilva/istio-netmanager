#!/bin/bash

# Create namespace and label it for istio
kubectl create namespace istio-io-health-rewrite
kubectl label namespace istio-io-health-rewrite istio-injection=enabled
