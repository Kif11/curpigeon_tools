from lib.shotgun_api3 import Shotgun

base_url = 'https://aau.shotgunstudio.com'
script_name = 'util'
app_key = 'cf1e303b918f7cab09c73ae4a100d89f596410f25690a41ba21d6211797d1daf'

sg = Shotgun(base_url, script_name, app_key)

# List all shots in the project
def list_shots(project_id):
	
	filters = [['project','is',{'type':'Project','id':project_id}]]
	shots = sg.find("Shot", filters, ["code"])
	
	return shots