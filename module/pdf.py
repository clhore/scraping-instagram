# library
from fpdf import FPDF

class PDF(FPDF):

    def __init__(self, page='A4', orientation='P'):
        super().__init__()

        # variables
        self.orientation = orientation

        # select size page
        if page == 'A4':
            self.page_W = 210.0
            self.page_H = 297.0
        elif page == 'A3':
            self.page_W = 210.0
            self.page_H = 297.0
        elif page == 'A5':
            self.page_W = 210.0
            self.page_H = 297.0

    def file_text(self, name):
        with open(name, 'rb') as xy:
            txt = xy.read().decode(encoding='latin-1', errors='ignore')
        self.set_xy(130.0, 20.0)
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('Arial', '', 14)
        self.multi_cell(0, 5, txt)

    def marco(self, margin=5.0, size=0.0, color=None):
        # modifier width line
        self.set_line_width(size)
        # modifier color
        if color is None:
            color = [253, 254, 254]
        self.set_fill_color(color[0], color[1], color[2])
        # create height and width
        h = self.page_H-margin-margin
        w = self.page_W-margin-margin
        # create marco
        if self.orientation == 'P':
            self.rect(margin, margin, w, h, 'DF')
        elif self.orientation == 'L':
            self.rect(margin, margin, h, w, 'DF')

    def picture(self, x=8.0, y=8.0, w=1586 / 40, h=1920 / 40, file=None):
        if file is not None:
            self.set_xy(x, y)
            self.image(file, link='', type='', w=w, h=h)

    def flag_es(self):
        # Marco Spanish flag
        self.marco(color=[205, 97, 85], margin=4.0)  # Red
        self.marco(color=[244, 208, 63], margin=4.8)  # Yellow
        self.marco(color=[205, 97, 85], margin=6)  # Red
        self.marco(color=[255, 255, 255], margin=6.8)  # White