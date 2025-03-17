# Digital Logic Calculator

A web-based calculator for digital logic operations including basic gates, half/full adders, and half/full subtractors.

## Features

- Basic Logic Gates (AND, OR, NOT, NAND, NOR, XOR)
- Half Adder
- Full Adder
- Half Subtractor
- Full Subtractor

## Setup Instructions

1. Make sure you have Python installed on your system (Python 3.6 or higher)

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Use

1. Select the desired operation from the dropdown menu
2. Set the input values using the checkboxes:
   - Input A
   - Input B
   - Carry/Borrow In (only for Full Adder and Full Subtractor)
3. Click the "Calculate" button to see the results

## Operations Available

- **Basic Gates:**
  - AND: Output is 1 only if both inputs are 1
  - OR: Output is 1 if at least one input is 1
  - NOT: Inverts the input
  - NAND: Inverted AND operation
  - NOR: Inverted OR operation
  - XOR: Output is 1 if inputs are different

- **Adders:**
  - Half Adder: Adds two bits, produces sum and carry
  - Full Adder: Adds three bits (including carry in), produces sum and carry

- **Subtractors:**
  - Half Subtractor: Subtracts two bits, produces difference and borrow
  - Full Subtractor: Subtracts three bits (including borrow in), produces difference and borrow 