
import os
from logging import debug
from logging.config import dictConfig
import ezgmail

vasometrics_path = "v:\\Vasometrics"
clinic_list = os.listdir(vasometrics_path)

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)s] [%(filename)s(%(lineno)d)] [PID:%(process)d]: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'maxBytes': 100000000,
            'backupCount': 5,
            'filename': '0.cronos.log',
            'mode': 'w',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})

debug('first debug: {}'.format(5))

for clinic in clinic_list:
    #### Skip these files/directories
    if clinic == "Vasometrics Archive":
        continue  # skips



    clinic_object_list = os.listdir(os.path.join(vasometrics_path,clinic))
    clinic_path = os.path.join(vasometrics_path, clinic)
    print("Clinic '{}':".format(clinic))
    for object in  clinic_object_list:
        if object.lower() == "Processed Studies".lower():
            continue

        object_path = os.path.join(clinic_path,object)
        print("\t{}".format(object_path))