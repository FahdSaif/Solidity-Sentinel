# Solidity Vulnerability Scanner POC

This repository contains a quick and simple Proof-of-Concept (POC) for an automated smart contract security auditing tool. The tool, built with Python, uses regular expressions to detect potential reentrancy vulnerabilities in Solidity contracts.

## Files

- **contract.sol**: A sample Solidity contract that intentionally includes a potentially vulnerable pattern.
- **scanner.py**: A Python script that scans the Solidity file for common vulnerability patterns.

## How to Run

1. Make sure you have Python installed.
2. Clone the repository.
3. Open a terminal and navigate to the repository directory.
4. Run the scanner with:

   ```bash
   python scanner.py
