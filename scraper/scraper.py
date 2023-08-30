import csv
from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_presidential_data(url: str) -> List[Tuple[str, List[str]]]:
    driver = webdriver.Safari()
    driver.get(url)

    name_elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "option"))
    )

    print('Presidential names:', [name.text for name in name_elements])

    presidential_data = []

    for name_element in name_elements:
        president_name = name_element.text

        speech_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "views-field-title"))
        )

        speeches = [speech.find_element(By.TAG_NAME, "a").get_attribute(
            "href") for speech in speech_elements]
        presidential_data.append((president_name, speeches))

    driver.quit()

    return presidential_data


def save_to_csv(data: List[Tuple[str, List[str]]], filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["President Name", "Speech Links"])
        csv_writer.writerows(data)

