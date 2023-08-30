import inputManager
import fileHandler
import json


def generateOpeningStatement():
    detailsJson = open(fileHandler.get_asset_path() + "details.json")
    details = json.load(detailsJson)
    openingStatement = "    " + details["title"] + "\n" + "     Version: " + details["version"]
    openingStatement += "\n" + details["description"]
    return openingStatement
def main():
    print(generateOpeningStatement())
    inputManager.input_loop()

if __name__ == "__main__":
    main()