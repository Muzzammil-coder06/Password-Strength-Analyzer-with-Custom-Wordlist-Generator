# Password Strength Analyzer with Custom Wordlist Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This project is a **Password Strength Analyzer** tool with an integrated **Custom Wordlist Generator** aimed at cybersecurity enthusiasts, penetration testers, and developers. It helps analyze the strength of passwords using advanced entropy calculations and generates customized attack wordlists based on user input keywords to aid in password cracking simulations.

---

## Features

- **Password Strength Analysis:**  
  Uses `zxcvbn` and custom entropy measures to provide a detailed strength score, estimated crack time, and feedback.

- **Custom Wordlist Generation:**  
  Allows users to input personalized keywords (e.g., names, dates, pets) and generates wordlists incorporating common password patterns, leetspeak variations, and appended years.

- **GUI Interface:**  
  Built with `tkinter` for an easy-to-use graphical interface, making the tool accessible even for beginners.

- **Export Wordlists:**  
  Exports the generated wordlists as `.txt` files, ready to be used with popular cracking tools like `John the Ripper` or `Hashcat`.

---

## Technologies Used

- **Python 3.8+**  
- **Tkinter** for GUI  
- **zxcvbn** for password strength estimation  
- **argparse** for CLI support (future feature)  
- **NLTK** for advanced wordlist manipulations (optional)  

--------------------------------------------------------------------------------------------------------------------------------------------------

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/password-strength-analyzer.git
   cd password-strength-analyzer

2. **Create a virtual environment (recommended):**

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

3. **Install required libraries:**

pip install -r requirements.txt

4. **Run the GUI:**

python gui.py

--------------------------------------------------------------------------------------------------------------------------------------------------
**Usage**
* Analyze Password Strength:
Enter a password in the first input box and click Analyze Password to view the strength score, estimated crack time, and feedback.

* Generate Custom Wordlist:
Enter comma-separated keywords (like names, dates, pets) in the second input box and click Generate Wordlist. The wordlist will be saved as custom_wordlist.txt in the project directory.

---

**Packaging as Executable**
To create a standalone Windows executable (.exe):

python -m PyInstaller --onefile --windowed gui.py

---

**Future Enhancements**

Add CLI mode using argparse for terminal-based usage.

Include more attack patterns like keyboard sequences, repeated characters.

Integrate with breach databases to check password leaks.

Add multilingual support for wordlist generation.

Contribution
Contributions are welcome! Feel free to open issues or submit pull requests for new features or bug fixes.

License
This project is licensed under the MIT License.

Contact
Muzzammil Khan
Email: muzzammil25edu@gmail.com
GitHub: https://github.com/Muzzammil-coder06

Secure your passwords, empower your pentests! 🔐

--------------------------------------------------------------------------------------------------------------------------------------------------


 
