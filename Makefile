NAME=ADC_Archiver_1.4.2
SRC=ADC_Archiver_1.4.2.py

linux:
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist $(SRC)

windows:
	nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist $(SRC)

deps-linux:
	pip install -r requirements.txt --break-system-packages
	pip install nuitka scons --break-system-packages

deps-windows:
	pip install -r requirements.txt
	pip install nuitka scons

clean:
	rm -rf build dist


