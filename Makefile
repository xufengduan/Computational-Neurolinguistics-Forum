.PHONY: generate clean serve

generate:
	python3 scripts/generate_event_pages.py

clean:
	rm -rf _site

serve: 
	bundle exec jekyll serve

build: 
	bundle exec jekyll build 