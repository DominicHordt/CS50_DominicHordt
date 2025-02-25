import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if "to" not in s:
        raise ValueError ("Not a valid time")
    elif "AM" not in s or "PM" not in s:
        raise ValueError ("Not a valid time")
    elif re.search(r"([1-9]\d?)(:\d\d)?(AM|PM)", s):
        raise ValueError ("Not a valid time")
    time = []
    if matches := re.findall(r"([1-9]\d?)(:\d\d)? (AM|PM)", s):
        for _ in matches:
            if int(_[0])>12:
                raise ValueError ("Not a valid time")
            elif ":" in _[1]:
                if int(_[1].replace(":","")) >= 60:
                    raise ValueError ("Not a valid time")
                elif "PM" in _:
                    if _[0] == "12":
                        time.append(_[0] + _[1])
                    else:
                        time.append(str(int(_[0])+12) + _[1])
                else:
                    if len(_[0])==1:
                        time.append("0" + _[0] + _[1])
                    elif _[0] == "12":
                        time.append("00" + _[1])
                    else:
                        time.append(_[0] + _[1])
            else:
                if "PM" in _:
                    if _[0] == "12":
                        time.append(_[0] + ":00")
                    else:
                        time.append(str(int(_[0])+12) + ":00")
                else:
                    if len(_[0])==1:
                        time.append("0" + _[0] + ":00")
                    elif _[0] == "12":
                        time.append("00:00")
                    else:
                        time.append(_[0] + ":00")
    return time[0] + " to " + time[1]


if __name__ == "__main__":
    main()
