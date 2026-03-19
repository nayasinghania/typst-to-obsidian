def convert():
    lines = []
    with open("example.typ", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            print(f"{i} {line.strip()}")
            lines.append


convert()
