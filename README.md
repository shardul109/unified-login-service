Steps to run :

open the authentication service directory , create a python virtual environment . Install all the dependencies from requirements.txt using the command : ` pip3 install -r requirements.txt `


start the server with `python main.py`


follow the same with server flam


by default the authentication service runs on 5001 port and the flam server runs on 5002. You can add multiple flam servers on differnt ports.

You can test the APIs using swagger :

after starting the server go to `http://127.0.0.1:5001/docs` (for authentication service routes , 5002 for flam server routes)

You can create a user from flam server using the createuser route .
It creates a user on the authentication server as well as stores the encrypted password in a sqlite database.

For encryption python libraries were used (bcrypt and cryptcontext)

FastAPI servers were used as runtime environment and SQLite database was used.
