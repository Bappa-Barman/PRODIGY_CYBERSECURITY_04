1. PRODIGY_CYBERSECURITY_04 - Simple Keylogger

 This is a Python project that creates a simple keylogger program to capture and store keystrokes.  
 It was developed as part of the Cyber Security Internship offered by Prodigy Infotech.

2.  What This Project Does

 This tool listens to your keyboard and:

- Records every key you press (letters, numbers, symbols, etc.)
- Logs special keys like **space**, **enter**, **backspace**
- Stores everything into a text file named `key_log.txt`

3. Ethical Use

> **This project is for educational purposes only.**  
> Never use keyloggers without proper permission. Unauthorized use is illegal and unethical.

4. Requirements

 Make sure you have:

- **Python 3** installed
- The **pynput** library Install the required library by running```bash pip install pynput

5. How to run the program

- Open your project folder in VS Code or any code editor.
- Make sure the file keylogger.py is present.
- Open a terminal in that folder.
- Install the required library (if not already):
  pip install pynput
- Run the script:
  python keylogger.py
- Now open a different window (like Notepad) and start typing.
- After a few seconds, open the file key_log.txt in your folder — your keystrokes will be recorded there.
