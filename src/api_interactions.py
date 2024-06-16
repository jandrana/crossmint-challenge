from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

max_retries = 5

def get_env_variable(name):
	value = os.getenv(name)
	if value is None:
		raise ValueError('No value for {name} found in the .env file')
	return value

class ApiClient:
	def __init__(self, base_url, candidate_id):
		self.base_url = base_url
		self.candidate_id = candidate_id
	
	def __str__(self):
		return f"Base URL: {self.base_url}, CandidateID: {self.candidate_id}."

	def create_polyanet(self, row, column):
		url = f"{self.base_url}/polyanets"
		data = {"candidateId": self.candidate_id ,"row": row, "column": column}
		self._post(url, data)

	def create_soloon(self, row, column, color):
		url = f"{self.base_url}/soloons"
		data = {"candidateId": self.candidate_id ,"row": row, "column": column, "color":color}
		self._post(url, data)

	def create_cometh(self, row, column, direction):
		url = f"{self.base_url}/comeths"
		data = {"candidateId": self.candidate_id ,"row": row, "column": column, "direction":direction}
		self._post(url, data)

	def get_goal_map(self):
		url = f"{self.base_url}/map/{self.candidate_id}/goal"
		try:
			response = requests.get(url)
			response.raise_for_status()
			return response.json()
		except requests.exceptions.RequestException as err:
			self._handle_error(err)

	def _post(self, url, data):
		retry_delay = 1
		for attempt in range(max_retries):
			try:
				response = requests.post(url, json=data)
				response.raise_for_status()
				return response.json()
			except requests.exceptions.HTTPError as err:
				if response.status_code == 429:
					print(f"Too Many Requests for url. Waiting {retry_delay} seconds before retrying...")
					time.sleep(retry_delay)
					retry_delay *= 2
				else:
					self._handle_error(err)
					break
			except requests.exceptions.RequestException as err:
				self._handle_error(err)
				break
			
		raise Exception("Maximum retry attempts reached")

	def _handle_error(self, error):
		print(f"API request failed: {error}")
		raise