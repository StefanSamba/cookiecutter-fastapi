import re
import sys

MODULE_REGEX = r"^[A-Za-z_]*$"

project_name = "{{cookiecutter.project_name}}"
endpoint_name = "{{cookiecutter.endpoint_name}}"


def validate_input(re_pattern, string_to_validate):
    if not re.match(re_pattern, string_to_validate):
        print(
            "ERROR: %s is not a valid Python name!\
            Only letters and underscores allowed"
            % string_to_validate
        )

        # exits with status 1 to indicate failure
        sys.exit(1)


validate_input(MODULE_REGEX, project_name)
validate_input(MODULE_REGEX, endpoint_name)
