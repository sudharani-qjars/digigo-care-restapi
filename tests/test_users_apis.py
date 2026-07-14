import pytest
from endpoints.api_endpoints import ClinicEndpoints
from schemas.clinics_schema import DOCTOR_SCHEMA

@pytest.mark.rest_api_sanity
def test_clinics_doctors_api_validation(clinics_client, test_data_reader, validator):
    clinic_id = test_data_reader["clinic_id"]
    get_doctors_url = ClinicEndpoints.GET_CLINIC_DOCTORS.format(clinic_id=clinic_id)
    response = clinics_client.get(get_doctors_url)
    assert response.status_code == 200
    assert (response.json()).get("doctors") is not None, "The doctors field should not be empty"
    print(response.text)
    validator.validate_schema(response.json(),DOCTOR_SCHEMA)


