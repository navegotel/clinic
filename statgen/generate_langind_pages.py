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
    templates = [
        {
            'filename': 'index.html',
            'context': {},
        },
        {
            'filename': 'ictus_es.html',
            'context': {'title':'Fisioterapia para Ictus en Clínica y a Domicilio',
                        'lang': 'es',
                        'description': 'Rehabilitación neurológica avanzada tras un ictus. Fisioterapeutas cualificados en clínica y en la comodidad de su domicilio. Recupere su autonomía.',
                        'hreflang': {
                            'en': 'https://clinica.markusbarth.net/ictus_en.html',
                            'de': 'https://clinica.markusbarth.net/ictus_de.html',
                        }
            },
        },
        {
            'filename': 'ictus_en.html',
            'context': {'title':'Stroke Physiotherapy | In-Clinic & Home Rehab Services',
                        'lang': 'en',
                        'description': 'Neurological stroke rehabilitation. Qualified physiotherapists providing expert care in-clinic and at home. Regain your mobility.',
                        'hreflang': {
                            'es': 'https://clinica.markusbarth.net/ictus_es.html',
                            'de': 'https://clinica.markusbarth.net/ictus_de.html',
                        }
            },
        },
        {
            'filename': 'ictus_de.html',
            'context': {'title':'Physiotherapie nach Schlaganfall | Praxis & Hausbesuche',
                        'lang': 'de',
                        'description': 'Neurologische Rehabilitation nach einem Schlaganfall. Erfahrene Physiotherapeuten in der Praxis & bei Ihnen zu Hause. Mobilität zurückgewinnen.',
                        'hreflang': {
                            'en': 'https://clinica.markusbarth.net/ictus_en.html',
                            'es': 'https://clinica.markusbarth.net/ictus_es.html',
                        }
            },
        },
        {
            'filename': 'onto_es.html',
            'context': {'title':'Rehabilitación oncológica',
                        'lang': 'es',
            },
        },
        {
            'filename': 'onto_en.html',
            'context': {'title':'Physiotherapy After Cancer Treatment | InBalance Guardamar',
                        'lang': 'en',
                        'description': 'Individualised physiotherapy after cancer treatment in Guardamar del Segura. Improve strength, mobility and physical function. Lymphoedema treatment available.',
                        'hreflang': {
                            'de': 'https://clinica.markusbarth.net/onto_de.html',
                            'es': 'https://clinica.markusbarth.net/onto_es.html',
                        }
                        
            },
        },
        {
            'filename': 'onto_de.html',
            'context': {'title':'Reha nach Krebs',
                        'lang': 'de',
            },
        },
    ]
    pg = PageGenerator("./tmpl/", templates, "..")
    pg.generate()

