import multiprocessing
from deploy_tools.workers import CustomUvicornWorker

name = "django_gunicorn"
bind = "unix:/project/django_gunicorn.sock"    # UNIX 소켓 사용 방식 -> 속도가 빠름
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
