all : hw3.pdf

%.pdf : %.tex prob3.csv
	lualatex --shell-esacape $<

prob3.random.csv : prob3.py
	python $<
