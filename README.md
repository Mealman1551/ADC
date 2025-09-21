# ADC Archiver Aurora

![Status](https://img.shields.io/badge/Status-Unstable-red)
![GitHub license](https://img.shields.io/github/license/Mealman1551/ADC)
![Platform: Windows/Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.12.x-yellow.svg)
![Development](https://img.shields.io/badge/Development-Active-brightgreen)
![Latest version](https://img.shields.io/badge/Latest%20version-2025.09.1-purple)



<img src="https://raw.githubusercontent.com/Mealman1551/ADC/cb41406a7d58017fc92ddb800519fc54563acc1a/img/ADC%20Aurora%20concept%20logo.svg" alt="Aurora" width="100"/>

Compatible with: <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg" alt="Windows 11" width="20"/> **&** <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="Linux" width="20"/>

Latest news can be found [here.](https://github.com/Mealman1551/ADC/discussions/categories/adc-unstable-aurora)

[ADC contact e-mailadres](mailto:adc@linuxmail.org)

IRC channel: #adcarchiver on OFTC

Forum: [https://groups.google.com/g/adc-archiver](https://groups.google.com/g/adc-archiver)

>[ !note]
> ### New features in the September update (ADC_Aur_2025.09.1.py):
>
> Added zipfile support, create and extract zip files.


### What is Aurora?

Aurora is the unstable/rolling release of ADC Archiver that features a newer version than stable and is only usable as a Python script.

Aurora is the release after [ADC Canary](https://gitlab.com/Mealman1551/adc-canary), ADC Canary is only for live development and **NOT** for using!

### Which Python version is needed?

Aurora and the main branch use Python 3.12.x

### When to use Aurora?

Aurora is perfect for users who prefer cutting-edge updates over stability.

### Where can I request features or get support?

To request features and get support go [here.](https://github.com/Mealman1551/ADC/discussions/categories/adc-unstable-aurora)

GitHub issues related to Aurora will not be handled!

### How to use Aurora?

Aurora follows a rolling release model by updating the source code to a higher version. Every half a year a new major stable version will be released. Aurora continues as a rolling release.

### Python packages required

- os
- zlib
- tkinter
- socket
- time
- progress
- progress.bar
- colorama
- fernet
- cryptography
- base64

### Additional Installation Requirements

Some of these libraries are included in the default Python installation.

The `socket`, `tkinter`, `progress`, `progress.bar`, `fernet`, `cryptography`, `base64` and `colorama` modules need to be installed separately, `TKinter` only on Linux.

---

The requirements.txt is also available. install it with:
```python
pip install -r requirements.txt
```

---

### SHA256 checksum for ``ADC_Aur_2025.09.1.py``

SHA256: `9473c9b1d698995704afc33255ebb796efe55ce15f24c162d8b232f1bf8e034d`

#### Other comments

ADC Aurora can from now of on only open and create archives with a byte-key of 8.

Read more about this [here.](https://github.com/Mealman1551/ADC/discussions/21)

---

If you want to support the project please consider a small donation: <a href="https://www.paypal.com/donate/?hosted_button_id=LEE83CJJ2BEJC">
	<img src="https://centerproject.org/wp-content/uploads/2021/11/paypal-donate-button-high-quality-png-1_orig.png" alt="Donate button" width="100"/>
</a>

## Notes

### No macOS support
ADC Archiver does **not** support macOS, and it never will.
This is a deliberate decision to take a stand against the growing dominance of proprietary ecosystems and Apple’s developer restrictions.
This project supports **open platforms only**: Windows and Linux.

You can ofc run the source code but official binary and/or setups are not compiled for macOS!

---

###### © 2025 Mealman1551
