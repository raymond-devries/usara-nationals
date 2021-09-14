import json
import datetime
from bs4 import BeautifulSoup


def parse_seconds(time: str):
    h, m, s = time.split(':')
    return int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())


def parse_checkpoint_data(raw_data: list):
    data = raw_data[0::2]
    data = [point for point in data if point != "&nbsp;"]
    checkpoint_data = []
    for point in data:
        soup = BeautifulSoup(point, "html.parser")
        stripped = list(soup.stripped_strings)
        checkpoint_data.append(
            {
                "name": stripped[0][:-4],
                "time": parse_seconds(stripped[2])
            }
        )

    return checkpoint_data


def extract_data_from_record(record):
    return {
        "place": int(record[1]),
        "team_number": int(record[2]),
        "team_name": record[3],
        "team_type": record[5],
        "score": int(record[6]),
        "finish_time": 0 if "disq" in record[7] else parse_seconds(record[7]),
        "points": int(record[8]),
        "bonus_penalty": 0 if record[9] == "&nbsp;" else int(record[9]),
        "manual_adjustment": 0 if record[10] == "&nbsp;" else int(record[10]),
        "time_penalty": 0 if record[11] == "&nbsp;" else parse_seconds(record[11]),
        "checkpoints": parse_checkpoint_data(record[12:]),
    }


def clean_data(path: str):
    with open(path) as f:
        data = json.load(f)
    cleaned = [extract_data_from_record(record) for record in data]

    with open("clean_data.json", "w") as f:
        json.dump(cleaned, f, indent=4, ensure_ascii=False)


def main():
    clean_data("raw_data.json")


if __name__ == '__main__':
    main()
