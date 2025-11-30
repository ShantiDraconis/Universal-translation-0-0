PDF=whitepaper.pdf

all: $(PDF)

$(PDF): main.tex sections/*.tex refs.bib
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex
	mv main.pdf $(PDF)

clean:
	rm -f *.aux *.log *.out *.bbl *.blg *.toc

.PHONY: all clean
