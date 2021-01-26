## Cover Letter Generator
This repo contains a cover letter generator that can easily be cloned and used on the fly.

### Useage
Currently the generator accepts two kinds of inputs:
* A path to a yaml config file which has all of the neccessary info in key value form

EXAMPLE:
```
python cover_letter_gen.py --config="configs/new_config.yaml"
```

* A series of manually entered key values

EXAPMLE:
```
python cover_letter_gen.py --company_name="Barry Bluestone Paper Company" --contact_name="Elda Flenderson" --position_name="The Temp" --job_listing_source="the Scranton Times website" --company_add_1="1135 Tremont St" --company_add_2="3rd Floor" --company_csz="Boston, MA 02115"
```

If you want to know what the available input args are, just run the following to get the help output:

`python cover_letter_gen.py -h`


### Background
I found myself shying away from applying to jobs because they required cover letters. I never really learned what a "good" cover letter should look like, nor did I feel confident in writing one so I would just not apply to jobs that required them. Bad! Eventually I got to the point where I had a stock base cover letter and would just swap out titles and companies and submit boring word docs. Also bad! Things would sometimes get sloppy when mass applying to jobs and cover letters would get sent out with incorrect swapped elements. So bad!

My solution was to build this, a simple set of scripts that use a config file to pull from a prewritten stock cover letter, fill in the blanks correctly, and save it all as a PDF with custome headers and footers. This is by no means the "correct" way of building, writing, or submitting cover letters, but it is a very good way for me to showcase my Python ability and automate a very boring and daunting task.

This project started in R, but I've since "ported" it to Python and added more functionality behind the scenes. Now I can fill out a config file, run the script, and I will have a "custom made" cover letter waiting for me to attach to an application.


