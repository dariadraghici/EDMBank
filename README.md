# EDMBank App

**EDMBank** is a modular, Python-based banking simulator designed to provide a secure, educational environment for managing financial operations. Developed using **Tkinter** for the GUI and **Google Firestore** for cloud storage, it offers a realistic dashboard experience for tracking balances, performing transfers, and managing account details.

## 👥 The Team

* **Drăghici Daria-Ioana**
* **Oanea Eliza-Maria**
* **Popa Marius**

## 🌟 Key Features

* **Authentication System:** Secure Login and Registration interfaces for personalized user accounts.
* **Digital Card Management:** A dynamic dashboard featuring a virtual card with a unique number, CVV, and "hide/reveal" functionality.
* **Financial Operations:** * Fund transfers between users via IBAN.
* Deposit funds and make payments to registered companies.
* Full transaction history tracking.
* **User Profile & Support:** Manage account credentials (email, password) and contact the dev team through an integrated support messaging system.
* **Responsive Design:** Adaptive layout that adjusts components based on window size (Desktop and Mobile-friendly modes).


## 🏗 System Architecture

The application follows an **Object-Oriented Programming (OOP)** paradigm with a structure similar to **Model-View-Controller (MVC)** to ensure modularity and scalability.

### 1. Frontend (View/UI)

Built with **Tkinter**, the interface is split into three strategic zones:

* **Top Menu:** Authentication and global navigation.
* **Main Content:** Card details, balance display, and action buttons.
* **Bottom Navigation:** Quick links to Card, Profile, Statistics, and Support.

### 2. Backend (Controller/Logic)

The `BankService` class acts as the brain of the app, handling:

* Data validation and business rule enforcement.
* IBAN generation and transaction processing.
* Communication between the UI and the Database.

### 3. Database (Model)

**Google Firestore** provides persistent storage. It manages:

* User account credentials and personal info.
* Real-time balance updates.
* Encrypted transaction logs.


## 🛠 Tech Stack

| Component | Technology |
| --- | --- |
| **Language** | Python 3.8+ |
| **GUI Framework** | Tkinter |
| **Database** | Google Firestore (Firebase) |
| **Dependencies** | `firebase_admin`, `cryptography`, `requests`, `json` |


## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher.
* Pip (Python package manager).

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/EDMBank-App.git
cd EDMBank-App

```


2. **Install dependencies:**
```bash
pip install firebase-admin cryptography requests

```


3. **Configure Credentials:**
Place your Firestore API key/JSON file in the project root (as required by `firebase_admin`).

### Running the App

Launch the application via the entry-point script:

```bash
python EDMBank_launcher.py

```


## 🔧 Detailed Component Design

* **`EDMBankApp` Class:** The central controller managing window states and navigation.
* **Authentication Module:** Validates credentials and initializes sessions.
* **Financial Module:** Dedicated functions for secure math operations and data consistency.
* **Adaptability Module:** Logic that dynamically resizes elements for consistent UX across different screen dimensions.


## 🧪 Testing & Deployment

* **Deployment:** The app is designed for standard desktop environments. It can be containerized using **Docker** for environment isolation.
* **Testing:** Currently verified through manual end-to-end testing (Registration → Deposit → Transfer → History). The modular codebase is prepared for future **pytest** or **unittest** integration.


## 📝 Conclusion

EDMBank represents a journey from foundational Python concepts to a complex, multi-layered application. By overcoming the challenges of UI responsiveness, asynchronous cloud storage, and secure financial logic, our team has produced a professional-grade simulator that demonstrates the power of modular software design.
