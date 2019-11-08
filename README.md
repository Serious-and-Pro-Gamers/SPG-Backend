# SPG Webapp Backend

### Project virtual environment setup
```
*** Installs virtual environment locally ***
$ python3 -m venv env
```

### Activate virtual environment
```
*** Linux ***
$ source env/bin/activate

*** Windows ***
$ env\Scripts\activate
```

### Install requirements / dependencies
```
(env) $ pip install -r requirements.txt
```

### Set "debug = True" to activate live changes (dev only)
```
(env) $ sudo vi app.py
app.run(debug=True)
```

### Run local instance of Flask app (dev only)
```
*** Use localhost for dev environment ***
(env) $ python app.py
```

### Deactivate virtual environment
```
*** Linux / Windows ***
(env) $ deactivate
```
