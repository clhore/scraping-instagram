
# module file
from module import pdf, JSON, auto_intagram

if __name__ == '__main__':

    # import password
    credentials = JSON.JSON(file='instagram_credentials.json').read()

    # create new session auto instagram
    instagram = auto_intagram.INSTAGRAM(driver_path='chromedriver.exe')

    # options and control
    instagram.open() # open instagram
    instagram.login(username=credentials['username'], password=credentials['password']) # login
    instagram.search(username='el_pais', description='EL PAÍS') # search an select user
    instagram.post(num=2) # extract post
    instagram.extract_img_and_text(ruta='article')
    instagram.close() # close driver

    # create file PDF 
    pdf_file = pdf.PDF(orientation='L')  # pdf object

    # create page article
    list_img = JSON.JSON(file='file.json').read()

    for name_art in list_img:
        # create new page
        pdf_file.add_page(orientation='L')
        pdf_file.flag_es() # and flag from spain
        # select file
        _file = 'article\\{}'.format(name_art)
        pdf_file.picture(file=_file, x=20, y=20.0, w=1586 / 15, h=1920 / 15)
        pdf_file.file_text(name='article\\{}'.format(name_art.replace('jpg', 'txt')))

    # save PDF file
    pdf_file.set_author('@clhore')
    pdf_file.output('log_instagram.pdf', 'F')
    # info user
    print('PDF created')