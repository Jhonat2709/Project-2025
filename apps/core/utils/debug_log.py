import os
from django.conf import settings

def log_message(message):
    log_file_path = os.path.join(settings.BASE_DIR, 'debug.log')
    with open(log_file_path, 'a') as f:
        f.write(message + '\n')