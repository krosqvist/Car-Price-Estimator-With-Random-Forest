# Car Price Estimator - Setup & Run Instructions

## Overview

This software can be used to estimate the price of any car using
a pretrained random forest machine learning model. It will also
predict the price development up to five years.

---

## Prerequisites

* **Python 3.8+**

  * Ensure Python is installed and added to your system PATH.
* **Node.js**

  * Ensure Node.js and npm are installed and added to your system PATH.

---

## Manual Setup Instructions

1. **Navigate to the project root folder**.

2. **Check Python installation**:

   ```bat
   python3 --version
   ```

   * If Python is not found, install Python 3.8+ and add it to PATH.

3. **Check Node.js installation**:

   ```bat
   node --version
   npm --version
   ```

   * If Node.js is not found, install Node.js and add it to PATH.

4. **Install Python backend dependencies**:

   ```bat
   pip install -r Backend\requirements.txt
   ```

5. **Install Node.js backend dependencies**:

   ```bat
   cd Backend
   npm install
   ```

9. **Start the backend server**:

   ```bat
   npm run dev
   ```

   * The software will be accessible on your browser at `http://localhost:3001`.

---

## Notes

* Always run these commands from the **project root folder**.
* Usage of venv can cause the program to malfunction due to node.js child process calling different python than what installed in venv
* Running `npm install` inside `Backend` ensures Node.js dependencies are correctly installed.
* The 1.7Gb model is downloaded from git tag in this repository during first calculation, so it will take some time. After that user experience will smoothen

---
