from extract_template import extract_template
from final_render import final_render
from string import Template
import random
import json
import sys
import os

class renderer:
    def __init__(self, templatePath, valuesPath):
        """
        Checks if the provided paths are valid and proceeds to parse.
        """
        filesExist = os.path.isfile(templatePath) and os.path.isfile(valuesPath)
        if filesExist:
            self.fetchResources(templatePath, valuesPath)
            self.editTemplate()
            self.exportPDF(templatePath)
        else:
            raise FileNotFoundError('Invalid path provided for template or object file(s).')


    def fetchResources(self, templatePath, valuesPath):
        """
        Fetches the raw value object and template string.
        """
        with open(valuesPath) as f:
            self.values = json.load(f)

        self.template = extract_template(templatePath)
        
    def editTemplate(self):
        """
        Replaces all the template fields with their values from the value object.
        """
        template = Template(self.template)
        edited_template = template.safe_substitute(**self.values)
        self.edited_template = edited_template.split('\n')

    def exportPDF(self,templatePath):
        """
        Creates the output directory if it doesnt exist, makes a path
        and proceeds to render the final output.
        """
        if not os.path.isdir('output'):
            os.mkdir('output')

        output_dir = f'output/{templatePath}_{random.randint(0,10000)}.pdf'

        final_render(output_dir, self.edited_template)


# driver code
def fetch_inputs():
    if __name__ == "__main__":
        try: #if run by command-line
            templatePath, valuesPath = sys.argv[1], sys.argv[2]
        except IndexError: #if run manually
            templatePath = input("Template path: ")
            valuesPath = input("Values path: ")

        renderInstance = renderer(templatePath, valuesPath)

fetch_inputs()