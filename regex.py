import re


def heading(line: str):
    return re.sub(r"=", r"#", line)


def convert():
    with open("example.typ", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            converted_heading = heading(line.strip())
            print(i, line.strip())
            print(i, converted_heading)
            print("\n")
            with open("example.md", "a", encoding="utf-8") as out:
                out.write(converted_heading + "\n")


convert()
