import multiprocessing
from deploy_tools.workers import CustomUvicornWorker

name = "django_gunicorn"
bind = "127.0.0.1:8000"    # 네트워크 소켓 사용 (분산환경을 위해)
workers = multiprocessing.cpu_count() * 2 + 1  
keepalive = 62
worker_connections = 1000 * workers
#worker_class = "deploy_tools.workers.CustomUvicornWorker"  # 이부분 custom 해야함
reload = True
loglevel = "INFO"
logfile = "-"
spew = False
lifespan = "off"

capture_output = True

max_requests = 1000
max_requests_jitter = 50
graceful_timeout = 15
timeout = 15

BASE_DIR = "/project/django_gunicorn"
pythonpath = BASE_DIR
chdir = BASE_DIR

preload_app = False
