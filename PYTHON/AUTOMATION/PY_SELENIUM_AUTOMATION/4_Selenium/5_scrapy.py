import scrapy
import os
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
from PIL import Image
from io import BytesIO

class FullPageScreenshotSpider(scrapy.Spider):
    name = 'full_page_screenshot'
    start_urls = ['https://www.saucedemo.com/']

    def parse(self, response):
        # Input login credentials
        yield scrapy.FormRequest.from_response(
            response,
            formcss='form',
            formdata={'user-name': 'standard_user', 'password': 'secret_sauce'},
            callback=self.after_login
        )

    def after_login(self, response):
        # After login, take the screenshot
        image = Image.open(BytesIO(response.body))
        print(os.getcwd())
        file_path = os.path.join(os.getcwd(), 'full_page_screenshot.png')
        image.save(file_path)
        self.log(f'Screenshot saved to: {file_path}')

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'DOWNLOAD_DELAY': 1,
        'LOG_ENABLED': False
    })
    process.crawl(FullPageScreenshotSpider)
    process.start()
