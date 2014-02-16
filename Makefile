all: coffee

coffee:
	coffee --compile --output static/js/ static/coffee/; cd -
	# coffee -o static/js -c static/coffee; cd -

coffee-watch:
	coffee -o static/js -cw static/coffee; cd -