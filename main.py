# library
import platform

# module file
from module import pdf, JSON, auto_intagram

if __name__ == '__main__':

    # import password
    credentials = JSON.JSON(file='instagram_credentials.json').read()
    # import content system.json
    system = JSON.JSON(file='system.json').read()

    # check your system
    if platform.system().lower() == "windows":
        driver_system = 'chromedriver.exe'
        path_bar = '\\'
    else:
        driver_system = 'chromedriver'
        path_bar = '//'

    # create new session auto instagram
    instagram = auto_intagram.INSTAGRAM(driver_path=driver_system, path_bar=path_bar)

    # options and control
    instagram.open()  # open instagram
    instagram.login(username=credentials['username'], password=credentials['password'])  # login
    instagram.search(username='el_pais', description='EL PAÍS')  # search an select user
    instagram.post(num=2)  # extract post
    instagram.extract_img_and_text(ruta='article')
    instagram.close()  # close driver

    # create file PDF
    pdf_file = pdf.PDF(orientation='L')  # pdf object

    # create page article
    list_img = JSON.JSON(file='file.json').read()

    for name_art in list_img:
        # create new page
        pdf_file.add_page(orientation='L')
        pdf_file.flag_es()  # and flag from spain
        # select file
        _file = 'article{0}{1}'.format(path_bar, name_art)
        pdf_file.picture(file=_file, x=20, y=20.0, w=1586 / 15, h=1920 / 15)
        pdf_file.file_text(name='article{0}{1}'.format(path_bar, name_art.replace('jpg', 'txt')))

    # save PDF file
    pdf_file.set_author(system['author'])
    pdf_file.output('log_instagram.pdf', 'F')
    # info user
    print('PDF created')
