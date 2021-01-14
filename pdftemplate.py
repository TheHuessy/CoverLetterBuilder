from fpdf import FPDF

class CoverLetterPDF(FPDF):
 
    def header(self):
        self.set_y(.5)
        self.set_font("Times", size=18, style="B")
        self.cell(w=6.5, h=.25, txt='James Huessy', ln=1, align="C")
        self.set_font("Times", size=12)
        self.cell(w=6.5, h=.25, txt='Jamaica Plain, MA | jameshuessy@gmail.com | 802-735-5650 | GitHub: TheHuessy', ln=1, align="C")
        self.cell(w=6.5, h=.5, txt='', ln=1, align="L")
    
    def footer(self):
        self.set_y(-.5) 
        self.set_font('Times', 'I', 9)
        self.multi_cell(w=6.5, h=.15, txt='This cover letter was generated in Python by a custom script I wrote. For the source code and other projects, visit https://github.com/TheHuessy/', align="C")