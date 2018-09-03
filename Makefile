clean:
	rm -rf docs

serve:
	reveal-md slides.md --theme white --css static/custom.css -w

render:
	python scripts.py render

qr:
	python scripts.py contactqr
	python scripts.py slidesqr
