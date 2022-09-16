import re

trainNumberRegex = re.compile(
    r"(?:(?<=Рейс)|(?<=\s))\d{1,5}(?=[\s]|прибыл|отправился)", re.IGNORECASE)
cityRegex = re.compile(r"(из|в)\s+\w*\s+", re.IGNORECASE)
timeRegex = re.compile(r"[\d:]+$", re.IGNORECASE)
replaceSpacesRegex = re.compile(r"\s+", re.IGNORECASE)

with open("logs.txt", "r") as logFile:
    trainLogs = []
    for line in logFile:
        line = line.strip()
        if line and line.startswith("Рейс"):
            trainNumber = int(trainNumberRegex.search(line).group(0))
            city = cityRegex.search(line).group(0)
            city = replaceSpacesRegex.sub(" ", city)
            time = timeRegex.search(line).group(0)
            trainLogs.append(f'[{time}] - Поезд № {trainNumber} {city}\n')

    with open("trainLogs.txt", "w") as trainLogsFile:
        trainLogsFile.writelines(trainLogs)
