import os, sys, re

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def to_numeric(string):
    return re.sub(r'[^0-9]', '', string)

def to_string_removed_square_brackets(string):
    return re.sub(r'\[(.*?)\]', '', string)

def to_string_removed_parentheses(string):
    return re.sub(r'\((.*?)\)', '', string)