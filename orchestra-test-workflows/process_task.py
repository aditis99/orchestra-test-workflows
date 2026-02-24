import json
import sys

def main():
    # Get input passed as argument
    input_data = sys.argv[1]

    data = json.loads(input_data)

    print("Received from Task 1:", data)
    print("Number * 2 =", data["number"] * 2)

if __name__ == "__main__":
    main()