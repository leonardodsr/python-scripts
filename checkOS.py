import platform as plat

user = [
	'architecture',
	'linux_distribution',
	'machine',
	'processor',
	'python_version',
	'release',
	'system',
	'uname',
	'version',
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
UNDERLINE = '\033[4m'


for key in user:
	if hasattr(plat, key):
		print(key + bcolors.BOLD + ": " + str(getattr(plat, key)()) + bcolors.ENDC)