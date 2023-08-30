from scraper import scrape_presidential_data, save_to_csv


def main():
    url = "https://millercenter.org/the-presidency/presidential-speeches"

    presidential_data = scrape_presidential_data(url)

    save_to_csv(presidential_data, "presidential_speeches.csv")
    print("Datos de discursos guardados en presidential_speeches.csv")


if __name__ == "__main__":
    main()
