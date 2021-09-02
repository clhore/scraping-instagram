# library
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import wget

# module file
from module import JSON


class INSTAGRAM:

    def __init__(self, driver_path=None, path_bar='\\'):
        super().__init__()

        # options windows
        self.driver_op = webdriver.ChromeOptions()
        self.driver_op.add_argument('--start-maximized')
        self.driver_op.add_argument('--disable-extensions')

        # variables
        self.anchors = None
        self.path = None
        self.path_bar = path_bar
        if driver_path is None:
            self.driver_path = 'driver.exe'
        else:
            self.driver_path = driver_path

        self.driver = webdriver.Chrome(self.driver_path, options=self.driver_op)

    def open(self):
        # open chrome and search url
        self.driver.get('https://www.instagram.com/?hl=es')

        # cookie accept
        time.sleep(2)
        cookie = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Aceptar todo")]'))) \
            .click()

    def login(self, username, password):
        # log in
        time.sleep(2)
        _username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]')))
        _password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
        # inset credentials
        _username.send_keys(username)
        _password.send_keys(password)

        # click login
        time.sleep(2)
        submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))) \
            .click()

        # waiting 4 seconds
        time.sleep(4)
        # click two alert
        for i in range(2):
            # click alert
            cookie = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Ahora no")]'))) \
                .click()
            # waiting 0.5 seconds
            time.sleep(0.5)

    def search(self, username=None, description=False):
        # waiting 1 seconds
        time.sleep(1)
        # search username
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Busca']")))
        # clear content search_box
        search_box.clear()
        # search username
        search_box.send_keys(username)
        # open username
        time.sleep(2)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "{desc}")]'.format(desc=description)))) \
            .click()
        # scroll down 2 times
        # increase the range to scroll more
        n_scrolls = 20
        for j in range(0, n_scrolls):
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 120)")
            time.sleep(0.5)

    def post(self, num=2):
        # target all the link elements on the page
        anchors = self.driver.find_elements_by_tag_name('a')
        anchors = [a.get_attribute('href') for a in anchors]
        # narrow down all links to image links only
        anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]
        # info user
        print('Found ' + str(len(anchors)) + ' links to images')
        # number articles
        n_articles = num
        # valid n_articles
        if n_articles > len(anchors):
            n_articles = len(anchors)
        # info user
        print(n_articles)
        # selected articles
        self.anchors = anchors[:n_articles]

    def file_valid(self, ruta='article'):
        path = os.getcwd()
        path = os.path.join(path, ruta)
        # valid directory
        file_article = os.path.exists(path)
        if not file_article:
            # create the directory
            os.mkdir(path)
        # save ruta
        self.path = path

    def extract_img_and_text(self, ruta):
        # valid ruta save from file
        self.file_valid(ruta=ruta)
        # create list
        images = list()
        count = 1
        # follow each image link and extract only image at index=1
        for a in self.anchors:
            self.driver.get(a)
            time.sleep(2)
            img = self.driver.find_elements_by_tag_name('img')
            img = [i.get_attribute('src') for i in img]
            images.append(img[1])
            # copy content article
            ctx = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span')
            ctx = ctx.text
            # create file name
            filename = '{ruta}{bar}{article}{num_art}.txt'.format(
                ruta=self.path, bar=self.path_bar, article=ruta, num_art=count
            )
            # create file article
            with open(filename, 'wb') as f:
                ctx = ctx.encode('latin-1', errors='ignore')
                # print(ctx)
                f.write(ctx)
            # renew count
            count += 1
            # Wait for 0.5 seconds
            time.sleep(0.4)

        # download images
        list_img = list()  # create list
        counter = 0  # initial count
        for image in images:
            name_img = 'article' + str(counter + 1) + '.jpg'
            list_img.append(name_img)
            # valid file name
            valid = os.path.exists('{path}{bar}{file}'.format(
                path=self.path, bar=self.path_bar, file=name_img)
            )
            if valid:
                # remove file
                os.remove('{path}{bar}{file}'.format(
                    path=self.path, bar=self.path_bar, file=name_img
                ))
            # Wait for 0.5 seconds
            time.sleep(0.5)
            # save image
            save_as = os.path.join(self.path, name_img)
            wget.download(image, save_as)
            counter += 1

        # writer file.json
        JSON.JSON(file='file.json').write(ctx=list_img)
        print(list_img)

    def close(self):
        # close windows
        self.driver.quit()
