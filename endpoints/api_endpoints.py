class ClinicEndpoints:
    GET_CLINIC_DOCTORS = "/api/clinics/public/{clinic_id}/doctors/"

class AppointmentsEndpoints:
    GET_CLINIC_DOCTOR_APPOINTMENTS = "/api/appointments/clinic/{clinic_id}/get-available-slots/{doctor_id}/{date}/"