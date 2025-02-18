import re

def check_reentrancy(contract_code):
    warnings = []
    # Look for the use of call{value: ...} which may indicate a reentrancy vulnerability
    pattern = r'\.call\s*{value:'
    if re.search(pattern, contract_code):
        warnings.append("Potential reentrancy vulnerability detected: usage of call{value: ...}")
    return warnings

def main():
    try:
        with open("contract.sol", "r") as file:
            code = file.read()
    except FileNotFoundError:
        print("Error: 'contract.sol' not found. Please create it first.")
        return

    warnings = check_reentrancy(code)
    if warnings:
        print("Vulnerability Warnings:")
        for warning in warnings:
            print(" -", warning)
    else:
        print("No obvious vulnerabilities found.")

if __name__ == "__main__":
    main()
