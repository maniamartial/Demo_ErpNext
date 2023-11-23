from subprocess import check_output
import requests
def print_contents_of_cwd():
    return check_output(['ls']).split()


def fetch_data_from_api():
    response=requests.get('https://api.github.com')
    return response.json()

def process_api_data():
    data=fetch_data_from_api()
    return data['current_user_url']


class ExternalService:
    def get_status(self):
        return 'OK'
    
class ServiceChecker:
    def __init__(self):
        self.external_service=ExternalService()
        
    def check_service_status(self):
        status=self.external_service.get_status()
        if status=='OK':
            return True
        else:
            return False
        