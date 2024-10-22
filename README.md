Basic ATM Machine Project

Project Overview:
This project simulates a basic ATM machine in Python that allows users to perform operations such as depositing money, withdrawing money, checking their balance, and exiting the system. It incorporates login functionality, balance checks, and limits on deposit and withdrawal amounts, formatted according to the Indian currency system.

Features:
Login System:
➡️Users can log in using their unique user_id and a 4-digit PIN.
➡️It verifies credentials from a predefined list of users and passwords.

Main Menu Options:
➡️Deposit Amount: Users can deposit an amount up to ₹1,00,000 at a time.
➡️Withdraw Amount: Users can withdraw an amount up to ₹10,000 in multiples of 100, provided they have         sufficient balance.
➡️Balance Enquiry: Users can check their balance with currency formatting.
➡️Exit: Users can safely exit the ATM system.

Indian Currency Formatting:
➡️The project uses the locale module to format currency as per the Indian money representation with commas, making it user-friendly.

How to Run:
➡️Ensure that you have Python installed on your system.
➡️Run the script ATM.py in your Python environment.
➡️Enter your user_id (predefined users: "srihari", "vamsi") and corresponding PIN.
➡️After a successful login, select an option from the displayed menu:
    ➡️Press 1 to deposit money.
    ➡️Press 2 to withdraw money.
    ➡️Press 3 to check your balance.
    ➡️Press 4 to exit the system.

Code Breakdown:
➡️login() Function: Handles user authentication by checking if the entered user_id and PIN match the predefined credentials.
➡️credit() Function: Allows users to deposit money up to ₹1,00,000.
➡️debit() Function: Enables users to withdraw money in multiples of 100, up to ₹10,000 per transaction.
➡️display() Function: Displays the user's balance, formatted in Indian rupees.
➡️exit() Function: Safely exits the ATM system.
➡️Main Loop: Provides the interface for the user to choose the desired action.

Conclusion:
This Basic ATM Machine project is a good introductory exercise in Python, demonstrating user login functionality, basic financial operations, and currency formatting. However, with improvements in user management, security, and data persistence, it can evolve into a more complete and practical system.