import importlib.metadata

import requests


def main():
    try:
        print("version", importlib.metadata.version("poetry-release-please-example"))
    except importlib.metadata.PackageNotFoundError:
        print("package not installed")
    print("my ip", requests.get("https://api.ipify.org").text)
    print("done")


if __name__ == "__main__":
    main()
