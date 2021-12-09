import http.server
import os
from prometheus_client import start_http_server, Counter , Gauge


REQUEST_COUNT = Counter('app_requests_count', 'total app http request count',['app_name', 'endpoint'])
RANDOM_COUNT = Counter('app_random_count','increment counter by random value')
ram_metric = Gauge("pod_memory_usage_bytes", "Memory usage in bytes.")
cpu_metric = Gauge("pod_cpu_usage_percent", "CPU usage percent.")
APP_PORT = 9011
METRICS_PORT = 8011

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        
        MEM=str(os.popen('cat /sys/fs/cgroup/memory/memory.usage_in_bytes').readlines())
        CPU=str(os.popen('cat /sys/fs/cgroup/cpuacct/cpuacct.usage').readlines())

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        REQUEST_COUNT.labels('prom_python_app', self.path).inc()
        RANDOM_COUNT.inc()
        ram_metric.set(int(MEM[2:-4])) 
        cpu_metric.set(int(CPU[2:-4]))

        

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('', APP_PORT), HandleRequests)
    server.serve_forever()
