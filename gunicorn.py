# Definição do host e porta
bind = ":8080"
# Define 8 processes
workers = 4
# Define 4 threads
threads = 4
# Configura o timeout para 10s
timeout = 10
# Define a saida dos logs para o console
errorlog = '-'
accesslog = '-'
# define o formato dos  logs
access_log_format = '%(h)s %(l)s %(u)s' \
                    ' %(t)s "%(r)s" %(s)s' \
                    ' %(b)s "%(f)s" "%(a)s"'
