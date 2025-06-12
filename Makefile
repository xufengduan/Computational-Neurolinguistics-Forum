.PHONY: generate clean serve

generate:
	python3 scripts/generate_event_pages.py

clean:
	rm -rf _site

serve: generate
	bundle exec jekyll serve

build: generate
	bundle exec jekyll build 