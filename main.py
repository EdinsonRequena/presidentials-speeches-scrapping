from scraper import scrape_presidential_speeches, save_to_csv, scrape_presidential_names


def main():
    url = "https://millercenter.org/the-presidency/presidential-speeches"

    presidential_names = scrape_presidential_names(url)
    speech_data = scrape_presidential_speeches(url, presidential_names)

    save_to_csv(speech_data, "presidential_speeches.csv")
    print("Datos de discursos guardados en presidential_speeches.csv")


if __name__ == "__main__":
    main()
