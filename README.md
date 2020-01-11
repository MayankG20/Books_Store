# Books_Store
Django Project

# Commands to be performed

    1) git clone https://github.com/MayankG20/Books_Store.git
  
    2) cd Books_Store
  
    3) cd mysite
  
    4) . dja/bin/activate    (for activating virtual environment)(for deactivation virtual environment type deactivate dja/)
    5) python3 manage.py runserver
    6) Paste the link http://127.0.0.1:8000/books in your browser
  
   if you get the warning for unapplied migrations do:
            python3 manage.py migrate
  
    if you have done some changes to your database:
  
      1) python3 manage.py makemigrations "name/of/app/to/which/migrations/will/be/applied"
  
      2) python3 manage.py sqlmigrate "name/of/app/to/which/migrations/will/be/applied" 0001
  
      3) python3 manage.py migrate
  
       in our case "name/of/app/to/which/migrations/will/be/applied" is books
