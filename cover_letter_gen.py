from pdftemplate import CoverLetterPDF
import argparse
import os
import sys

def inputs_sorter(contact_name, position_name, job_listing_source, company_name, company_add_1, company_add_2, company_csz, company_name_informal=None):
    #Not adding company_name_informal because it's only used once and we could just sub in the contact name and not go through the headache of coding the ifs
    if contact_name == "" or contact_name == None:
        contact_name = "Hiring Committee"
        
    if company_add_2 == "":
        inputs_hash = {"contact_name": contact_name,
                       "position_name": position_name,
                       "job_listing_source": job_listing_source,
                       "company_name": company_name,
                       "company_add_1": company_add_1,                   
                       "company_csz": company_csz
                      }
    else:
        inputs_hash = {"contact_name": contact_name,
                       "position_name": position_name,
                       "job_listing_source": job_listing_source,
                       "company_name": company_name,
                       "company_add_1": company_add_1,
                       "company_add_2": company_add_2,
                       "company_csz": company_csz
                      }
    return inputs_hash

def address_parser(inputs_hash):
    if "company_add_2" in inputs_hash:
        address_block = "\n".join([inputs_hash['company_name'],
                                 inputs_hash['company_add_1'],
                                 inputs_hash['company_add_2'],
                                 inputs_hash['company_csz']])
    else:
        address_block = "\n".join([inputs_hash['company_name'],
                                 inputs_hash['company_add_1'],
                                 inputs_hash['company_csz']])
    return address_block

def content_builder(inputs_hash, algorithm_placeholder_variable=None):
    if algorithm_placeholder_variable:
        print("Carry out harder bit")
    else:
        with open("./Cover Letter Copy/stock.txt") as stock:
            text_body = stock.read()
        output_text = text_body.format(inputs_hash['contact_name'], 
                                       inputs_hash['position_name'],
                                       inputs_hash['job_listing_source'],
                                       inputs_hash['company_name'],
                                       inputs_hash['position_name']
                                      )
        address_block = address_parser(inputs_hash)
        output_text = "\n\n".join([address_block, output_text])
        return output_text

def build_letter(contact_name, position_name, job_listing_source, company_name, company_add_1, company_add_2, company_csz):
    inputs = inputs_sorter(contact_name, position_name, job_listing_source, company_name, company_add_1, company_add_2, company_csz)
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

    out_name = "generated_cover_letters/{}_{}_James_Huessy.pdf".format(company_name.replace(" ", "_"), position_name.replace(" ", "_"))
    try:
        pdf.output(out_name)
    except Exception as err:
        print("Could not build cover letter!\nError: {}".format(err))
    else:
        print("Cover letter written!")


parser = argparse.ArgumentParser(description='Enter all the data and we will make you a cover letter!')

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
                    help='The address of the company, line 2.\rIf not needed, just add ""')

parser.add_argument('--company_csz', type=str, nargs='?',
                    help='Company City, State Zipcode \rJust like that, with the comma')
args = vars(parser.parse_args())

build_letter(args['contact_name'],
    args['position_name'],
    args['job_listing_source'],
    args['company_name'],
    args['company_add_1'],
    args['company_add_2'],
    args['company_csz'])

