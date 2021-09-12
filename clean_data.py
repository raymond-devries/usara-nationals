import json
import datetime


def get_seconds(time: str):
    h, m, s = time.split(':')
    return int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())


def extract_data_from_record(record):
    return {
        "place": int(record[1]),
        "team_number": int(record[2]),
        "team_name": record[3],
        "team_type": record[5],
        "score": int(record[6]),
        "finish_time": 0 if "disq" in record[7] else get_seconds(record[7]),
        "points": int(record[8]),
        "bonus_penalty": 0 if record[9] == "&nbsp;" else int(record[9]),
        "time_penalty": 0 if record[10] == "&nbsp;" else get_seconds(record[10])
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
