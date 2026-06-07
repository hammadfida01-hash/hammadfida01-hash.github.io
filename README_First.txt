================================================
   MY PORTFOLIO WEBSITE — Built with Django
   Developer: Hammad
   Email: hammadfida01@gmail.com
   GitHub: https://github.com/hammadfida01-hash
   LinkedIn: https://www.linkedin.com/in/m-hammad-7869ba358/
================================================

ABOUT THIS PROJECT
------------------
This is my personal portfolio website built using Django (Python web framework).
It showcases my skills, projects, and contact information.
The site is fully responsive and designed with a clean, modern look.


PAGES
-----
1. Home     — Hero section with skills, tech stack, and featured projects
2. About    — About me, tech stack skills, and profile photo
3. Contact  — Contact form that sends messages directly to my email via Django


TECH STACK USED
---------------
Backend:
  - Python
  - Django
  - Django Email (send_mail)

Frontend:
  - HTML5
  - CSS3 (custom, no framework)
  - JavaScript (minimal)

Database:
  - SQLite (default Django)

Other:
  - Git & GitHub (version control)
  - VS Code (editor)


PROJECT STRUCTURE
-----------------
portfolio/
│
├── portfolio/               -- Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── main/                    -- Django app
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── include/
│   │       ├── navbar.html
│   │       └── footer.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   ├── logo.svg
│   │   ├── myimg2.jpg
│   │   ├── tic_tac_toe.jpg
│   │   ├── bmi_calculator.jpg
│   │   ├── currency_conv.jpg
│   │   └── password_gen.jpg
│   └── cv/
│       └── hammad_cv.pdf
│
└── manage.py


HOW TO RUN THIS PROJECT
-----------------------
Step 1 — Clone the repository
  git clone https://github.com/hammadfida01-hash/portfolio.git
  cd portfolio

Step 2 — Install Django
  pip install django

Step 3 — Run the server
  python manage.py migrate
  python manage.py runserver

Step 4 — Open in browser
  http://127.0.0.1:8000/


FEATURES
--------
  - Responsive design (mobile + desktop)
  - Smooth scroll to projects section
  - Contact form with Django email backend
  - Success message after form submission
  - Project cards linked to GitHub repositories
  - Favicon (SVG logo) in browser tab
  - GitHub & LinkedIn links in footer
  - Download CV button


FEATURED PROJECTS
-----------------
1. Tic Tac Toe          — HTML, CSS, JavaScript
2. BMI Calculator       — HTML, CSS, JavaScript
3. Currency Converter   — React.js, API
4. Password Generator   — React.js


CONTACT
-------
If you want to hire me or collaborate on a project:
  Email:    hammadfida01@gmail.com
  GitHub:   https://github.com/hammadfida01-hash
  LinkedIn: https://www.linkedin.com/in/m-hammad-7869ba358/

================================================
  © 2026 Hammad. All rights reserved.
================================================
