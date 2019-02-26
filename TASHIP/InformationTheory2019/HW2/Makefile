all : ./hw2.pdf

%.pdf : %.tex 
	python ./prob1.py
	lualatex --shell-escape $<
