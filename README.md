# Brownie Security Lab

A collection of smart contract security challenges and educational resources built with [Brownie](https://github.com/eth-brownie/brownie) and [Hardhat](https://hardhat.org/).

## Overview

This repository provides hands-on exercises for learning and practicing smart contract security. Each module demonstrates a specific vulnerability or security pattern, with example contracts, attack scripts, and test cases.

## Structure

- `contracts/` — Solidity smart contracts for each security topic
- `scripts/` — Python scripts for deploying and attacking contracts
- `tests/` — Automated test cases for vulnerabilities and mitigations
- `build/` — Compiled contract artifacts (auto-generated)
- `reports/` — Security analysis and findings
- `interfaces/` — Interface definitions for contracts

### Example Modules

- **Lack of Precondition Controls**
  - `contracts/lack_of_precondition_controls/`
  - `scripts/lack_of_precondition_controls/`
- **Reentrancy**
  - `contracts/reentrancy/`
  - `scripts/reentrancy/`

## Getting Started

### Prerequisites

- git >= 2.32.1
- python >= 3.11.0
- npm >= 8.11.0
- node >= 16.16.0

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/walkerchiu/brownie-security-lab.git
   cd brownie-security-lab
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # if requirements.txt exists
   npm install                      # for Hardhat
   ```
3. Set up Brownie:
   ```bash
   brownie compile
   ```

## Usage

- Run attack scripts:
  ```bash
  brownie run scripts/<module>/<attack_script>.py
  ```
- Run tests:
  ```bash
  brownie test
  ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
