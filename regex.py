import re


def conversion(line: str):
    # heading text
    temp = re.sub(r"=", r"#", line)

    # bold text
    temp = re.sub(r"\*(.*?)\*", r"**\1**", temp)

    # italic text
    temp = re.sub(r"\_(.*?)\_", r"*\1*", temp)

    return temp


def convert():
    with open("example.typ", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            converted = conversion(line.strip())
            print(f"(typ) {i} {line.strip()}\n(md)  {i} {converted}\n")


convert()
