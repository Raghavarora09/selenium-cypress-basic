# Selenium & Cypress Web Automation Exercise

This repository contains files for a web automation exercise using both Selenium and Cypress. The goal of this assignment is to introduce you to web automation using Selenium and Cypress by creating a custom HTML page with various elements and then writing scripts to interact with these elements.

## Files

- `page.html`: HTML file containing a custom registration form with various elements such as input fields, checkboxes, radio buttons, and dropdown menus.
- `script.js`: JavaScript file adding interactivity to the HTML page, such as form submission handling.
- `style.css`: CSS file containing styles to enhance the visual appearance of the HTML form.
- `selenium_script.py`: Python script using Selenium WebDriver to interact with the `page.html` and perform tasks such as filling out the form and submitting it.
- `cypress.cy.js`: Cypress script for automating interactions with the `page.html` using Cypress.

## Instructions

1. **Clone the Repository**: Clone this repository to your local machine using Git.

```bash
git clone https://github.com/Raghavarora09/selenium-basic.git
```
2. **Navigate to Repository**: Change directory to the cloned repository.
```bash
cd selenium-web-automation
```
3. **Install Dependencies**: Ensure you have Python and Selenium WebDriver installed. You can install Selenium using pip.

```bash
pip install selenium
```

4. **Download WebDriver**: Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and place it in a directory accessible from your PATH.
5. **Run the Selenium Script**: Execute the selenium_script.py using Python.

```bash
python selenium_script.py
```
This script will open the page.html in a browser, interact with the elements of the registration form, and submit it. You will see the actions being performed in the browser window.

6. **Run the Cypress Script**: Execute the Cypress script using Cypress.

```bash
npx cypress open
```
This will open the Cypress Test Runner. Click on the cypress.cy.js test file to run the Cypress script. It will automate interactions with the page.html, filling out the form and submitting it.

7. **Verify Results**: After running each script, verify that the form has been submitted successfully. You can check the console output for a confirmation message.

###Contribution
Contributions are welcome! If you have any suggestions, improvements, or issues, feel free to open an issue or create a pull request.
**Happy automating!**
