LATEXMK?=latexmk -pdflatex='lualatex -synctex=1' -shell-escape -pdf -auxdir=_aux

.PHONY: all clean realclean view

all: main.pdf

clean:
	rm -f *.{aux,fls,log,out,fdb_latexmk,bbl,blg,toc,brf,synctex.gz,snm,nav}
	rm -f *.{bcf,run.xml,vrb,idx,ilg,ind,.synctex\(busy\)}
	rm -rf -- _minted-* _aux

realclean: clean
	rm -f out.pdf

%.pdf: %.tex
	$(LATEXMK) -interaction=nonstopmode $<

view:
	$(LATEXMK) -interaction=nonstopmode -pvc main.tex
