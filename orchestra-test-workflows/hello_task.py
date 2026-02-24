import json

def main():
    result = {
        "number": 5
    }

    # Print structured JSON output
    print(json.dumps(result))

if __name__ == "__main__":
    main()