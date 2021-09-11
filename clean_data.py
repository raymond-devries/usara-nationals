import json


def clean_data(path: str):
    with open(path) as f:
        data = json.load(f)
    print(data)


def main():
    clean_data("raw_data.json")


if __name__ == '__main__':
    main()
