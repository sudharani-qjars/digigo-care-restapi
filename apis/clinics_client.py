from apis.base_client import BaseClient
from endpoints.api_endpoints import ClinicEndpoints

class ClinicsClient(BaseClient):

    def get_clinic_doctors(self):
        return self.get(ClinicEndpoints.GET_CLINIC_DOCTORS)