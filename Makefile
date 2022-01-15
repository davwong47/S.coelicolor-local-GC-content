manuscript.pdf: local_gc_content.png
	pandoc -f markdown -t latex -s manuscript.md -o manuscript.pdf --citeproc

local_gc_content.png: local_gc_content.csv
	Rscript csv2png.R

local_gc_content.csv: Sco.dna
	python3 dna2csv.py

Sco.dna:
	curl --location --output Sco.dna http://bit.ly/1Q8eKWT

clean:
	rm Sco.dna
	rm local_gc_content.csv
	rm local_gc_content.png
	rm manuscript.pdf