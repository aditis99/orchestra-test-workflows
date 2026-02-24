import json

def main():
    with open("output.json", "r") as f:
        data = json.load(f)

    print("Received from Task 1:", data)
    print("Number * 2 =", data["number"] * 2)

if __name__ == "__main__":
    main()