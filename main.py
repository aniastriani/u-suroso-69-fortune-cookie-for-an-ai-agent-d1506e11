import os

# One original fortune-cookie line, written fresh for this bounty:
# a fortune cookie speaks in lucky numbers, and an AI agent's luck
# is measured in HTTP status codes.
LINE = "Your lucky numbers are 404, 500, and 200 \u2014 in that order, and only on Fridays."


def main():
    assert len(LINE) <= 140, "fortune must fit in 140 characters"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
