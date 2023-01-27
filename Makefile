.PHONY: all

.env/bin/activate: requirements.txt
	python3 -m venv .env
	.env/bin/pip install -r requirements.txt

run: .env/bin/activate
	.env/bin/python src/app.py

startdb:
	db/start_db.sh

stopdb:
	docker stop mariadb_dev

freeze: .env/bin/pip
	.env/bin/pip freeze > requirements.txt

clean:
	rm -rf __pycache__
	rm -rf ./.env
