# istio-netmanager
Network management configuration for service mesh using kubernetes with istio

The services folder contains the bookinfo example as well as prometheus and kiali.

The routing folder has a match based trafic shifting example

The fault folder contains the fault injection of a 30 seconds delay in the ratings virtual service

The fix_timeout folder contains the proposed fix for an unresponsive service through the use of a timeout configuration. Please note that the timeout value is extremely short only for demonstration.

The fix_load folder contains the httpbin and fortio applications, with httpbin configured with a circuit break. There are also two scripts for ease of use during testing.


To verify the fault tolerance configurations mentioned first enable istio injection on the default namespace and initialize the bookinfo application. This can be done with the setup.sh and init.sh, respectively.
If you are using minikube, make shure to run 
> minikube tunnel

before the above scripts.

The init.sh script will display the ingress ip of the cluster. By connecting to http://<INGRESS_IP>:80/productpage you can see the bookinfo application.

After running
> kubectl apply -f fault/

and reloading the bookinfo app a couple times, you will be able to see that reviews-v3 is no longer showing ratings and reviews-v2 is no longer able to load. This happens because ratings now takes 30 seconds more to reply, reviews-v3 has an implemented timeout and reviews-v2 has no timeout implemented, thus being timed out by productpage.

Running 
> kubectl apply -f fix_timeout/ 

will implement a control plane level timeout on ratings, recovering reviews-v2 functionality.


To test circuit braking simply run
> kubectl apply -f fix_load/

you can then test the communication between httpbin and fortio by running
> sh fix_load/test.sh

and trip the circuit break with
> sh fix_load/break.sh

notice in the output that some requests were refused, this means that there were more requests than the maximum pending requests.

