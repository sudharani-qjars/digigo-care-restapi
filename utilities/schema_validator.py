from jsonschema import validate
from jsonschema.exceptions import ValidationError


class SchemaValidator:

    @staticmethod
    def validate_schema(response_json, schema):
        try:
            validate(
                instance=response_json,
                schema=schema
            )
            return True

        except ValidationError as e:
            raise AssertionError(
                f"Schema Validation Failed\n\n{e.message}"
            )