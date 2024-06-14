import re

def sanitize_output(output, target_type):
    sanitized_output = output
    if target_type == 'url':
        sanitized_output = re.sub(r"(https?://[^\s]+)", r"\1", sanitized_output)
    elif target_type == 'ip':
        sanitized_output = re.sub(r"(\d{1,3}\.){3}\d{1,3}", r"\1", sanitized_output)
    return sanitized_output
