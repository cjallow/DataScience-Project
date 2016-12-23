main = notes
css = light2.css
deps := reveal.js $(css)
MKD = pandoc
REVEAL = ~/repos/others/reveal.js/
opts := -s -S -f markdown -t revealjs -V theme:solarized
ifneq ($(strip $(css)),)
	opts += -c $(css)
endif

.PHONY : all
all : $(main).html

sc : opts += --self-contained
sc : all
.PHONY : sc

$(main).html: %.html: $(main).mkd $(deps)
	$(MKD) $(opts) -o $@ $<

reveal.js :
	[[ -d $(REVEAL) ]] && ln -s $(REVEAL) $@ \
		|| git clone https://github.com/hakimel/reveal.js.git
