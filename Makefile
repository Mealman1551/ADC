NAME=ADC_Archiver_1.4.2
SRC=src/ADC_Archiver_1.4.2.py

linux:
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist $(SRC)

windows:
	nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist $(SRC)

deps-linux:
	pip install -r requirements.txt --break-system-packages
	pip install nuitka scons --break-system-packages

deps-windows:
	python -m pip install -r requirements.txt
	python -m pip install nuitka scons

clean:
	rm -rf build dist


