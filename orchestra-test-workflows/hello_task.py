import json

def main():
    data = {
        "message": "Hello from Task 1",
        "number": 42
    }

    with open("output.json", "w") as f:
        json.dump(data, f)

    print("Task 1 completed and wrote output.json")

if __name__ == "__main__":
    main()