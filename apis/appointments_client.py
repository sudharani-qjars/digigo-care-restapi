from apis.base_client import BaseClient
from endpoints.api_endpoints import AppointmentsEndpoints

class AppointmentsClient(BaseClient):

    def get_clinic_doctors_appointments(self):
        return self.get(AppointmentsEndpoints.GET_CLINIC_DOCTOR_APPOINTMENTS)