import json


def main():
    s = None
    with open("./config.txt", "r") as f:
        s = json.load(f)
    print(s["gtoken"])

if __name__ == "__main__":
    main()
