from pdftemplate import CoverLetterPDF
import argparse
import os
import sys
import yaml

def inputs_sorter(config):
    if config['contact_name'] == "" or config['contact_name'] == None:
        if config['to_recruiter']:
            config['contact_name'] = "Recruiter"
        else:
            config['contact_name'] = "Hiring Committee"
    if config['company_add_2'] == "":
        del config['company_add_2']
    return(config)

def address_parser(inputs_hash):
    if "company_add_2" in inputs_hash.keys():
        address_block = "\n".join([inputs_hash['company_name'],
                                 inputs_hash['company_add_1'],
                                 inputs_hash['company_add_2'],
                                 inputs_hash['company_csz']])
    else:
        address_block = "\n".join([inputs_hash['company_name'],
                                 inputs_hash['company_add_1'],
                                 inputs_hash['company_csz']])
    return address_block

def read_text_file(path):
    with open(path, 'r') as file:
        output = file.read()
    return(output)

def content_builder(inputs_hash):
    text_body = read_text_file("./cover_letter_copy/stock.txt")
    body_text = text_body.format(
            inputs_hash['contact_name'],
            inputs_hash['position_name'],
            inputs_hash['job_listing_source'],
            )
    if inputs_hash['to_recruiter'] == 'True':
        conc_text = read_text_file("./cover_letter_copy/conclusion_recruiter.txt").format(
                inputs_hash['position_name']
                )
        output_text = "\n".join([body_text, conc_text])
    else:
        conc_text = read_text_file("./cover_letter_copy/conclusion_company.txt").format(
                inputs_hash['company_name'],
                inputs_hash['position_name']
                )
        address_block = address_parser(inputs_hash)
        full_letter = "\n".join([body_text, conc_text])
        output_text = "\n\n".join([address_block, full_letter])

    return(output_text)

def build_letter(config):
    inputs = inputs_sorter(config)
    body = content_builder(inputs)
    
    ## PDF setup
    pdf = CoverLetterPDF(orientation='P', unit='in',format='letter')
    pdf.add_font(family='Garamond', fname=r"fonts/gara.ttf", uni=True)

    pdf.set_font('Garamond', size=12)
    pdf.set_margins(1, .5, 1)
    pdf.add_page()

    ## Whole Text Body From Inputs
    pdf.multi_cell(w=6.5,h=.2,txt=body,align="L")

    ## EXIT SALUTATION ##
    pdf.cell(w=6.5, h=.25, txt='', ln=1, align="L")
    pdf.cell(w=6.5, h=.25, txt='Sincerely,', ln=1, align="L")
    pdf.cell(w=6.5, h=.25, txt='James Huessy', ln=1, align="L")

    ## Check if the output folder exists, create it if it doesn't
    if not os.path.isdir("generated_cover_letters"):
        os.mkdir("generated_cover_letters")

    out_name = "generated_cover_letters/{}_{}_James_Huessy_Cover_Letter.pdf".format(
            inputs['company_name'].replace(" ", "_"),
            inputs['position_name'].replace(" ", "_")
            )
    try:
        pdf.output(out_name)
    except Exception as err:
        print("Could not build cover letter!\nError: {}".format(err))
    else:
        print("Cover letter written!")

def args_wrangle(parser):
    input_args = vars(parser.parse_args())
    if input_args['config']:
        with open(input_args['config'], "r") as config_file:
            output_args = yaml.load(config_file.read(), Loader=yaml.BaseLoader)

    else:
        output_args = input_args

    return(output_args)



parser = argparse.ArgumentParser(description='Either provide the path to a yaml config file based on the neighboring config_template.yaml file or enter the neccessary info via command line args. You will find your finished cover letter in the generated_cover_letters folder in this repo.')

parser.add_argument('--config', type=str, nargs='?', default=False,
                    help='The relative path to the config file. If config is used, other arguments are ignored.')

parser.add_argument('--contact_name', type=str, nargs='?',
                    help='The contact name. If not known, enter a blank string like ""')

parser.add_argument('--position_name', type=str, nargs='?',
                    help='The position title')

parser.add_argument('--job_listing_source', type=str, nargs='?',
                    help='Where you found out about the job posting')

parser.add_argument('--company_name', type=str, nargs='?',
                    help='The name of the company')

parser.add_argument('--company_add_1', type=str, nargs='?',
                    help='The address of the company, line 1')

parser.add_argument('--company_add_2', type=str, default="", nargs='?',
                    help='The address of the company, line 2.\rIf not needed, you can exclude it')

parser.add_argument('--company_csz', type=str, nargs='?',
                    help='Company City, State Zipcode \rJust like that, with the comma')

parser.add_argument('--to_recruiter', type=str, default=False, nargs='?',
                    help='Whether or not this letter is intended for a recruiter. Defaults to False, change to True otherwise')



args = args_wrangle(parser)
build_letter(args)

