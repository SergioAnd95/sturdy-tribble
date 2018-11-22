## Sturdy-Tribble
#### Tasks:

- Create base Django project for book store. On the main page you have to see list of books with the following information: book title, authors info, ISBN (International Standard Book Number), price. Initial data has to be taken from fixtures.
- Create a page where manager can create/edit book data.
- Add the new field `publish_date` to the book and add calendar widget to this field on the edit page. For the existing books use today date for this field.
- Create admin site for our app and show link to admin edit page on the page where book are listed.
- Add possibility to save all http requests to database and display 10 last of then on the separate page.
- Add site copyright with start/end years.
- Add manage command to display list of books with possibility to order by publish date field defining ordering (asc/desc).
- Add info logging of books manipulations: create/edit/delete

#### Setup project local:
1. `git clone https://github.com/SergioAnd95/sturdy-tribble.git`
2. `cd sturdy-tribble`
3. `pip3 install -r requirements.txt` or `pip install -r requirements.txt` if you use virtualenv
4. Create file .env in settings directory(what content must be in .env file you can see in .env.example)
5. Setup your database in .env file(item #4) and run `./manage.py migrate` (for create all tables in your db)
6. For provide additional data run `./manage.py loaddata books.json`
7. `./manage.py createsuperuser` If you want create user 
8. For start project run command `./manage.py runserver`