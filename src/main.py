import time
from api_interactions import get_env_variable, ApiClient
from astral_objects import Polyanet, Soloon, Cometh

def create_megaverse(api_client, goal_map):
	megaverse_objects = []
	for row_index, row in enumerate(goal_map['goal']):
		for col_index, value in enumerate(row):
			if value == 'POLYANET':
				megaverse_objects.append(Polyanet(row_index, col_index))
			elif value.endswith('SOLOON'):
				color = value.split('_')[0].lower()
				megaverse_objects.append(Soloon(row_index, col_index, color))
			elif value.endswith('COMETH'):
				direction = value.split('_')[0].lower()
				megaverse_objects.append(Cometh(row_index, col_index, direction))
	
	for object in megaverse_objects:
		object.create(api_client)
		time.sleep(0.5)

	return megaverse_objects

def print_megaverse(objects):
	for object in objects:
		print("MEGAVERSE:")
		print(f"{object.__class__.__name__}: row {object.row} | column {object.column}")

def main():
	candidate_id = get_env_variable('CANDIDATE_ID')
	base_url = get_env_variable('API_URL')
	api_client = ApiClient(base_url, candidate_id)

	goal_map = api_client.get_goal_map()
	if goal_map:
		print("Goal Map:", goal_map)
		objects = create_megaverse(api_client, goal_map)

if __name__ == "__main__":
	main()