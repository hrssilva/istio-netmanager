#!/bin/bash
kubectl create namespace monitoring
kubectl label namespace default istio-injection=enabled
