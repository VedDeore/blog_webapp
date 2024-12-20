# Blog Web Application

#### Technologies Used: Python, Flask, HTML5, CSS3, JavaScript, MySQL

### Project Overview

The **Blog Web Application** is a platform designed for publishing and managing blog content. It allows users to interact with blog posts, and administrators can manage the content through an intuitive dashboard. The application leverages **Flask** for backend development, while **HTML5**, **CSS3**, and **JavaScript** are used for a responsive and interactive frontend. **MySQL** is integrated to handle data storage and management efficiently.

### Key Features

- **Admin Dashboard:**
  - Enabled administrators to manage blog posts, including adding new content, editing existing posts, and removing outdated posts.
- **Responsive User Interface:**
  - Built a user-friendly interface using **HTML5**, **CSS3**, and **JavaScript**, ensuring that users can easily navigate and interact with the blog content.
- **Database Integration:**
  - Utilized **MySQL** to store blog post data, ensuring smooth interaction between the front end and back end.
  - Allowed for efficient data retrieval, ensuring that users can view the latest blog posts.

### Technologies Used

- **Python:** For backend development and server-side logic.
- **Flask:** To build the web application and manage HTTP requests.
- **HTML5, CSS3, JavaScript:** For designing the interactive and responsive front-end.
- **MySQL:** For storing blog post data and managing user interactions with the blog content.

### Conclusion

The **Blog Web Application** combines backend and frontend technologies to create a seamless platform for managing and interacting with blog content. By integrating a user-friendly admin dashboard with real-time updates, the application provides a powerful tool for content management and ensures an engaging experience for users.

## How to Run the App

To run the Blog Web Application, follow these steps:

1.  **Install Dependencies:**

    - First, make sure you have Python installed on your system. You can download Python from the official website.
    - Create a virtual environment (optional but recommended):

          python -m venv venv

    - Activate the virtual environment:

      - On Windows:

            venv\Scripts\activate

      - On macOS/Linux:

            source venv/bin/activate

    - Install the required dependencies by running:

          pip install -r requirements.txt

      - The requirements.txt file includes all the necessary libraries, such as Flask, scikit-learn, MySQL connector, and others.

2.  **Set Up MySQL Database:**

    - Create a MySQL database for the app. In the database folder, you will find SQL queries to create the necessary tables. Run the queries in your MySQL database.
    - Create a .env file in the root directory of the project and set up the variables. An example is provided in the .env.example file.

3.  **Run the Application:**

    - You can run the app directly from your IDE (such as PyCharm, VSCode, etc.) by running the main.py file.
    - Alternatively, you can run the app using Gunicorn for a production-ready setup:

          gunicorn main:app

      - This command will start the app using Gunicorn, which is a WSGI HTTP server for Python web applications.

4.  **Access the App:**

    - Once the app is running, the URL will pop up on the screen, allowing you to interact with the app.

5.  **Credentials:**

    - For admin access, use the following credentials:
      - Username: admin
      - Password: pass1

That’s it! You can now start using the blog web application to read and post blogs.
