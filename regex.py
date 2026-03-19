import re


def conversion(line: str):
    temp = ""
    # heading
    temp = re.sub(r"=", r"#", line)
    return temp


def convert():
    with open("example.typ", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            converted_heading = conversion(line.strip())
            print(i, line.strip())
            print(i, converted_heading)
            print("\n")
            with open("example.md", "a", encoding="utf-8") as out:
                out.write(converted_heading + "\n")


convert()
