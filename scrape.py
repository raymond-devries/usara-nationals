from selenium import webdriver
import json

from selenium.webdriver.firefox.options import Options


def main():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://adventureenablers.s3.amazonaws.com/Tracking/2021USARANationals/SI/index.html")
    data = driver.execute_script("return getData(5)")
    driver.quit()
    with open("raw_data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
