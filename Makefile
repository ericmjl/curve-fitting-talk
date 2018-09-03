clean:
	rm -rf docs

render:
	python scripts.py render

qr:
	python scripts.py contactqr
	python scripts.py slidesqr

build: render qr
	cp -r assets docs/.
