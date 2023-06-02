from ._func import random_string, random_number, get_time
import re


class Template:

    def __init__(self):
        pass

    def replace_random(self, match: re.Match, func: callable) -> str:
        """Replace the random string or number"""
        group = match.group(1)
        if group:
            return func(int(group))
        return func()

    def build(self, template: str, email: str = '') -> str:
        """Build the template"""
        template = re.sub(r'\$random_string\((\d*)\)', lambda match: self.replace_random(match, random_string), template)
        template = re.sub(r'\$random_number\((\d*)\)', lambda match: self.replace_random(match, random_number), template)
        template = re.sub(r'\$time\((\w*)\)', lambda match: get_time(match.group(1)), template)
        template = re.sub(r'\$to_email\(\)', email, template)
        return template
