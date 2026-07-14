DOCTOR_SCHEMA = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Get Clinic Doctors Response",
  "type": "object",
  "additionalProperties": False,
  "required": [
    "success",
    "doctors",
    "clinic_settings"
  ],
  "properties": {
    "success": {
      "type": "boolean"
    },
    "doctors": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": False,
        "required": [
          "id",
          "name",
          "photo_url",
          "gender",
          "qualification",
          "specialization",
          "designation",
          "experience",
          "bio",
          "availability_status",
          "upcoming_available_dates",
          "working_days",
          "clinic_schedule"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "photo_url": {
            "type": [
              "string",
              "null"
            ],
            "format": "uri"
          },
          "gender": {
            "type": "string",
            "enum": [
              "male",
              "female",
              "other"
            ]
          },
          "qualification": {
            "type": "string"
          },
          "specialization": {
            "type": "string"
          },
          "designation": {
            "type": "string"
          },
          "experience": {
            "type": "integer",
            "minimum": 0
          },
          "bio": {
            "type": [
              "string",
              "null"
            ]
          },
          "availability_status": {
            "type": "string",
            "enum": [
              "available",
              "unavailable",
              "busy"
            ]
          },
          "upcoming_available_dates": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "date"
            }
          },
          "working_days": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "mon",
                "tue",
                "wed",
                "thu",
                "fri",
                "sat",
                "sun"
              ]
            }
          },
          "clinic_schedule": {
            "type": "object",
            "additionalProperties": False,
            "required": [
              "start_time",
              "end_time",
              "working_days",
              "appointment_duration",
              "slot_interval"
            ],
            "properties": {
              "start_time": {
                "type": "string",
                "pattern": "^([01]\\d|2[0-3]):([0-5]\\d)$"
              },
              "end_time": {
                "type": "string",
                "pattern": "^([01]\\d|2[0-3]):([0-5]\\d)$"
              },
              "working_days": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": [
                    "mon",
                    "tue",
                    "wed",
                    "thu",
                    "fri",
                    "sat",
                    "sun"
                  ]
                }
              },
              "appointment_duration": {
                "type": "integer",
                "minimum": 1
              },
              "slot_interval": {
                "type": "integer",
                "minimum": 1
              }
            }
          }
        }
      }
    },
    "clinic_settings": {
      "type": "object",
      "additionalProperties": False,
      "required": [
        "working_days",
        "start_time",
        "end_time",
        "max_advance_booking_days",
        "appointment_duration",
        "slot_interval",
        "min_advance_booking_hours"
      ],
      "properties": {
        "working_days": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "mon",
              "tue",
              "wed",
              "thu",
              "fri",
              "sat",
              "sun"
            ]
          }
        },
        "start_time": {
          "type": "string",
          "pattern": "^([01]\\d|2[0-3]):([0-5]\\d)$"
        },
        "end_time": {
          "type": "string",
          "pattern": "^([01]\\d|2[0-3]):([0-5]\\d)$"
        },
        "max_advance_booking_days": {
          "type": "integer",
          "minimum": 0
        },
        "appointment_duration": {
          "type": "integer",
          "minimum": 1
        },
        "slot_interval": {
          "type": "integer",
          "minimum": 1
        },
        "min_advance_booking_hours": {
          "type": "integer",
          "minimum": 0
        }
      }
    }
  }
}