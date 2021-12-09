# Assignment on prometheus


    • Export the metrics (like request per second, memory usage, cpu usage etc) in the existing mini project given to Interns
    • Install Prometheus and Grafana using Docker (with docker-compose)
    • Configure prometheus (scrape configs) such way that it can scrape the metrics from default metric path of the application job
    • Validate the entire configuration to check if the data is coming or not in Prometheus UI
    • Create the Dashboards in Grafana on top of the metrics exported by adding the Prometheus as a Datasource.
    
  # Solution
 
Build docker image
   # Path "prometheus/build"
   
   -> docker-compose build
     tag the image and push to your docker repo or you can use my image in the rpshreedhar/prom-assigment:f1
     if you build your own image then you have to change docker image K8 deployment.yml file 
   
Run deplyment.yml and service.yml file 
   # path "prometheus/k8"
  -> kubectl create -f deployment -f service.yml 
  
     run minikube tunnnel(keep it run) if are you using minikube then get external IP to access the app
  -> minikube tunnel
  -> kubectl get svc
  
      access the  application at External_IP:9011
      access the  application at External_IP:8011

Run the Prometheus and grafana

     replace the target of web-app ip address with external IP and port  in prometheus.yml file
   # path "prometheus/config"
   
     run docker-compose file 
   # path "prometheus"
      -> docker-compose up 
      
      access the  prometheus at localhost:9090
      access the  prometheus at localhost:3000
      
   
   
 
