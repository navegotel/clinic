import jinja2
import os

class PageGenerator(object):
    def __init__(self, templateDir, templates, outputDir):
        self.templateLoader = jinja2.FileSystemLoader(searchpath=templateDir)
        self.templateEnv = jinja2.Environment(loader=self.templateLoader)
        self.outputDir = outputDir
        self.templates = templates
 
    def generate_page(self, filename, context):
        template = self.templateEnv.get_template(filename)
        outfilename = os.path.join(self.outputDir, filename)
        outputText = template.render(context)
        with open(outfilename, 'w') as f:
            f.write(outputText)
        
    def generate(self):
        for item in self.templates:
            self.generate_page(item['filename'], item['context'])


if __name__ == "__main__":
    templates = [{
            'filename': 'ictus_es.html',
            'context': {'title':'Apoyo con ictus',
                        'lang': 'es',
            },
        },
        {
            'filename': 'ictus_en.html',
            'context': {'title':'Help with ictus',
                        'lang': 'en',
            },
        },
        {
            'filename': 'ictus_de.html',
            'context': {'title':'Hilfe bei Ictus',
                        'lang': 'de',
            },
        },
    ]
    pg = PageGenerator("./tmpl/", templates, "..")
    pg.generate()
