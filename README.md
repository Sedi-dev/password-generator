# 🔐 Password Generator (Python)

## 📌 Project Overview

This program is a secure password generator built in Python. It generates strong, random passwords using a combination of letters, numbers, and special characters.

---

## ⚙️ Features
- Generate passwords with adjustable strength levels:
    - Weak (letters only)
    - Medium (letters + numbers)
    - Strong (letters + numbers + symbols)
- Enforced password complexity rules
- Randomized secure password generation
- Password strength scoring system (0–100)
- User input validation for safe execution
- Clean command-line interface

---

## 🧠 Key Concepts & Skills Demonstrated

This project demonstrates understanding of:

- Random number generation
- String handling and concatenation
- List manipulation and shuffling
- Input validation
- Basic security principles in password creation
  
--- 

## 🧠 How It Works

The program generates a password by:

1. Selecting a character pool based on chosen strength
2. Ensuring required character types are included for stronger passwords
3. Filling the remaining length with random characters
4. Shuffling the result for unpredictability
5. Evaluating password strength using a scoring system

---

## 📌 Challenges Faced

One of the main challenges was ensuring **true randomness** while still meeting strength requirements (e.g., a "strong" password must contain at least one uppercase, one lowercase, one number, and one symbol).

**Solution:** I implemented a two-step approach:
1. Guarantee required character types are included first
2. Fill remaining length with random characters from the full pool
3. Shuffle the result to avoid predictable patterns

Another challenge was designing the **strength scoring system** to be objective and useful. I weighted factors like length, character variety, and user-selected strength level to produce a 0-100 score with clear interpretations.

---

## 🛠️ Technologies Used
- Python 3
- Built-in random module
- Built-in string module

---

## ▶️ How to Run the Project

1. Clone the repository:
git clone https://github.com/Sedi-dev/password-generator
2. Navigate into the project folder:
cd password-generator
3. Run the program:
python main.py

---

## 📊 Strength Scoring System

Each generated password is evaluated based on:

- Length of password
- Presence of lowercase letters
- Presence of uppercase letters
- Presence of numbers
- Presence of symbols
- Selected strength level

The final score is displayed as a percentage with an interpretation:

- 🟢 0–49 → Weak
- 🟡 50–79 → Medium
- 🔴 80–100 → Strong

## 💡 Learning Outcome

This project strengthened my understanding of randomness and how to generate secure, unpredictable outputs, which is important in cybersecurity and real-world applications.

- How to design modular Python programs using functions
- Input validation and error handling
- Working with randomness for secure generation
- Basic security principles in password design
- Building user-focused command-line tools

## 🚀 Future Improvements
- Allow user-defined character sets
- Create a GUI version using Tinker or web interface
- Add password strength estimation without user-selected level (pure entropy-based)
- Save generated passwords to an encrypted file (basic password manager)
- Add clipboard copy functionality

## 👨🏻‍💻 Gameplay Demo

![Password generator running](https://github.com/user-attachments/assets/caad33d3-87b3-4bf9-9c0c-3d8614aab487)

![Input validation example](https://github.com/user-attachments/assets/eaff80d7-ca60-4fc7-bcfd-1f03bef7c938)

![Password and strength input validation example](https://github.com/user-attachments/assets/4aa0278c-195f-4eb6-a579-17aee13301a3)


---

## Dependencies
No external libraries required - runs with Python standard library only. 

---

## 🖥️ Code Structure

- `main.py` contains:
  - `generate_password(length, strength)` → returns password string
  - `check_strength(password, expected_strength)` → returns score (0-100)
  - `get_user_input()` → validates all user inputs
- Functions are modular with single responsibilities
- Includes type hints (Python 3.6+)
  
---

⭐ This project was built as part of my learning journey in Computer Science to strengthen my understanding of programming fundamentals and practical problem-solving.

---

Last updated: May 2026
