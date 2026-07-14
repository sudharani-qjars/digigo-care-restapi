import pytest
from endpoints.api_endpoints import AppointmentsEndpoints
from schemas.appointments_schema import APPOINTMENTS_SCHEMA

@pytest.mark.rest_api_sanity
def test_appointments_doctor_api_validation(appointments_client, test_data_reader, validator):
    clinic_id = test_data_reader["clinic_id"]
    doctor_id = test_data_reader["doctor_id"]
    date = test_data_reader["date"]

    get_appointments_doctor_url = AppointmentsEndpoints.GET_CLINIC_DOCTOR_APPOINTMENTS.format(clinic_id=clinic_id, doctor_id=doctor_id,date=date)
    response = appointments_client.get(get_appointments_doctor_url)
    assert response.status_code == 200
    assert (response.json()).get("available_slots") is not None, "The available_slots field is empty"
    print(response.text)

    validator.validate_schema(response.json(),APPOINTMENTS_SCHEMA)


