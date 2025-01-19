Artist Community Website
------------------------

This is a website built for artists to upload their paintings. An artist
can sign up or use their google account to log in. They can add artists and their paintings. Other artists can leave
comments/feedback on the paintings. An artist may delete or modify
artists or paintings they have created. He/she may also delete
comments on his/her paintings.

Requirements:
-------------

Python
VM and vagrant
sqlite


Setup Database:
---------------

To setup the artists.db sqlite database, run this command from the shell:
python database_setup.py

To populate the database with some data for testing, run this command from the shell:
python somedata.py

Run webserver:
--------------
To startup the website, run the project.py file using this command form the shell:
python project.py

This webserver listens in on port 5000.

