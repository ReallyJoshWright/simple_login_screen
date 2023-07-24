TARGET = simple_login_screen
DIRS = . src forms

PY = python
SOURCES = $(foreach D, $(DIRS), $(wildcard $(D)/*.py))
MAIN = $(foreach D, $(DIRS), $(wildcard $(D)/*$(TARGET).py))
EXEDIRS = build dist
CACHEDIRS = $(foreach D, $(DIRS), $(wildcard $(D)/*__pycache__))

all: $(TARGET)

$(TARGET): $(SOURCES)
	@echo -e "#!/bin/sh\n" > temp
	@echo "$(PY)$(MAIN)" >> temp
	@install -m 755 temp $(TARGET)
	@rm -f temp
.PHONY: clean exe
clean:
	rm -rf $(TARGET) $(EXEDIRS) $(TARGET).spec $(CACHEDIRS)
exe: clean
	pyinstaller --onefile --noconsole $(MAIN)
