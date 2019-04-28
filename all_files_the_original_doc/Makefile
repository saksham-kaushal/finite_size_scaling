PROJECT = docu 
NAME = autoScale_guide

$(PROJECT) : $(NAME).pdf 
	
$(NAME).pdf: $(NAME).tex autoScale_main.tex
	pdflatex $(NAME)
	pdflatex $(NAME)

spell:
	aspell --mode=tex -c $(NAME).tex 

.PHONY: clean, ready
clean:
	rm -f *.log *.toc *.out *.aux *.toc *~ *.bak $(NAME).pdf
	
ready:
	rm -f $(NAME).log $(NAME).toc $(NAME).out *.aux $(NAME).toc *~ *.bak
	
