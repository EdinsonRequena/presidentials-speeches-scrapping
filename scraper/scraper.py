# import csv
# from typing import List, Tuple
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup


# def scrape_presidential_data(url: str) -> List[Tuple[str, List[str]]]:
#     driver = webdriver.Safari()
#     driver.get(url)

#     name_elements = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "option"))
#     )
#     presidential_names = [name.text for name in name_elements]

#     print('Presidential names:', presidential_names)

#     speech_data = []

#     for president_name in presidential_names:
#         president_link = driver.find_element_by_link_text(president_name)
#         president_link.click()

#         president_soup = BeautifulSoup(driver.page_source, "html.parser")
#         speech_elements = president_soup.find_all(
#             "div", class_="views-field-title"
#         )
#         speeches = [speech.find("a")["href"] for speech in speech_elements]

#         speech_data.append((president_name, speeches))

#         driver.back()

#     driver.quit()

#     return speech_data


# def save_to_csv(data: List[Tuple[str, List[str]]], filename: str) -> None:
#     with open(filename, "w", newline="", encoding="utf-8") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow(["President Name", "Speech Links"])
#         csv_writer.writerows(data)


# if __name__ == "__main__":
#     url = "https://millercenter.org/the-presidency/presidential-speeches"

#     presidential_data = scrape_presidential_data(url)
#     save_to_csv(presidential_data, "presidential_speeches.csv")
#     print("Datos de discursos guardados en presidential_speeches.csv")

import csv
from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_presidential_data(url: str) -> List[Tuple[str, List[str]]]:
    driver = webdriver.Safari()
    driver.get(url)

    name_elements = WebDriverWait(driver, 50).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "option"))
    )

    # print('Presidential names:', [name.text for name in name_elements])

    presidential_data = []

    for name_element in name_elements:
        president_name = name_element.text

        # president_element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.NAME, name_element.get_attribute("value")))
        # )

        # print('president_element:', president_element)
        # president_element.click()

        # president_link = driver.find_element(
        #     By.PARTIAL_LINK_TEXT, name_element)
        # print('president_link:', president_link)
        # president_link.click()

        speech_elements = WebDriverWait(driver, 50).until(
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


if __name__ == "__main__":
    url = "https://millercenter.org/the-presidency/presidential-speeches"

    presidential_data = scrape_presidential_data(url)

    save_to_csv(presidential_data, "presidential_speeches.csv")
    print("Datos de discursos guardados en presidential_speeches.csv")
