<p align="center">
  <img src="https://raw.githubusercontent.com/The-ADC-Archiver-Project/Assets/refs/heads/main/banner/borealis%20banner.jpg" alt="ADC Banner" width="500">
</p>

# ADC (ArchivedDataCodec)
ADC - the future of simple archiving.


[![GitHub license](https://img.shields.io/github/license/Mealman1551/ADC)](#)
[![Platform: Windows/Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue.svg)](#)
[![Development](https://img.shields.io/badge/Development-Active-brightgreen)](#)
[![Latest version](https://img.shields.io/github/v/release/Mealman1551/ADC?label=Latest%20version&color=brightgreen)](https://github.com/mealman1551/adc/releases/latest)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)
[![GitHub repo size](https://img.shields.io/github/repo-size/Mealman1551/ADC)](#)
[![GitHub issues](https://img.shields.io/github/issues/Mealman1551/ADC)](https://github.com/Mealman1551/ADC/issues)
[![GitHub stars](https://img.shields.io/github/stars/Mealman1551/ADC)](#)
[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](#)
[![CodeQL](https://github.com/Mealman1551/ArchivedDataCodec/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Mealman1551/ArchivedDataCodec/actions/workflows/github-code-scanning/codeql)
[![Build Status](https://github.com/Mealman1551/ADC/actions/workflows/build.yml/badge.svg)](https://github.com/Mealman1551/ADC/actions/workflows/build.yml)
[![Mirror to GitLab](https://github.com/Mealman1551/ArchivedDataCodec/actions/workflows/gitlab-mirror.yml/badge.svg?branch=stable%2F1.4)](https://github.com/Mealman1551/ArchivedDataCodec/actions/workflows/gitlab-mirror.yml)
![Total Downloads](https://img.shields.io/badge/dynamic/json.svg?url=https://raw.githubusercontent.com/Mealman1551/ArchivedDataCodec/main/.github/downloads.json&query=$.total_downloads&label=Total%20Downloads&color=97CA00)


**Mailing list:** [Subscribe](https://www.freelists.org/list/adc) | [Archive](https://www.freelists.org/archive/adc)

**Main announcements:** [Mail archive](https://the-adc-archiver-project.github.io/adc-mail-archive) (look for "[ANN]" label)

**Community:** [Forum](https://groups.google.com/g/adc-archiver) | IRC: OFTC #adc-archiver | [Matrix](https://matrix.to/#/#adc-archiver:matrix.org) | [XMPP](xmpp:vuwirer@chat.disroot.org?join)


Compatible with: <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg" alt="Windows 11" width="20"/> **&** <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="Linux" width="20"/>

# Index / Quick Links

* [ADC Overview](#adc-archiveddatacodec)
* [Features](#features)
* [Getting Started](#getting-started)
* [Download](#download)
  * [Windows](#windows)
  * [Linux](#linux)
* [Usage](#usage)
* [License](#license)
* [Why ADC](#why-adc)
* [Issues](#issues)
* [Update Schedule](#update-schedule)
* [Contributing](#contributing)
* [Contact](#contact)
* [GitLab](#gitlab)
* [Supported Versions](#supported-versions)
* [Prepare Build environment on Linux .1](#preparing-build-environment-on-linux)
  * [Start building on Linux .2](#start-building-on-linux)

**ADC (ArchivedDataCodec)** is an open-source <img src="https://raw.githubusercontent.com/Mealman1551/ADC/362a969f45ab6f17883ec68cb6172dc4ad3ce58b/img/svg/open-source-icn.svg" alt="Open-Source" width="30"/> file extension and archiving/compression tool that uses Zlib for efficient compression and decompression of various file types. With a simple command-line interface, ADC supports both Windows and Linux, making it easy for users to archive and extract files.

ADC Archiver uses a byte-key of 8, meaning that it can create archives without limitations.

Test archives [here](https://github.com/The-ADC-Archiver-Project/adc-example-archive)

For container/format info go to [FORMAT.md](docs/FORMAT.md)

## Features

- **Great Compression Algorithm**: Utilizes zlib for efficient compression.
- **Cross-Platform**: Compatible with both Windows and Linux.
- **Command-Line Interface**: Simple and intuitive interface.
- **Support**: Supports a wide range of file types.

## Getting Started

### Prerequisites

***Users***

- Windows 8 or higher
- A modern Linux distro with at least glibc 2.31

***Developers***

- Python 3
- zlib
- tkinter
- progress
- colorama
- cryptography
- base64
- zipfile
- webbrowser
- urllib
- json
- ssl

## Download

Release Canidate (RC) downloads can be found here: [Release Canidate Downloads](https://codeberg.org/Mealman1551/adc_1.5.0_rc_bin/releases)


ADC 1.5.0 Source code download 

| Platform: | Download                                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------|
| Windows   | [sourcecode.zip](https://github.com/Mealman1551/ArchivedDataCodec/archive/refs/heads/development/1.5.zip)       |
| Linux     | [sourcecode.tar.gz](https://github.com/Mealman1551/ArchivedDataCodec/archive/refs/heads/development/1.5.tar.gz) |

### Unix (BSD, Solaris)

1. Install Python 3
2. Install `requirements.txt`
3. Install python3-tk
4. Download the source code from `/src`
5. Run the source code with `python3`

## Usage

Download the program for Windows or Linux. Tarballs and setups are available in the Releases tab.

## License

ADC Archiver is dual-licensed.

You may use, modify and distribute ADC Archiver under the terms of the
GNU General Public License v3 (GPLv3).

If you provide ADC Archiver as a network service, SaaS, or through a remote
or online virtual machine environment, the GNU Affero General Public License v3 (AGPLv3) applies.

See [LICENSE](LICENSE) and [LICENSE_AGPLv3](LICENSE_AGPLv3) for the full license texts.

## Why ADC

* **ADC is a purpose-built archiving format**
  No historical baggage, no legacy compromises. ADC is designed with a single, clear structure and a strict data layout.
* **Linear and predictable archive layout**
  Archives are written and read sequentially from start to end. No central directories, no backward seeks, no hidden tables.
* **Straightforward to implement in any language**
  The format is compact and explicit. A complete reader or writer can be implemented without complex or specialized libraries.
* **Full control over the archive contents**
  Each file is processed, compressed, and stored individually. There is no implicit metadata or opaque behavior.
* **Built-in modern encryption**
  Optional password protection is integrated into the format using proven cryptography, not external tooling.
* **Deterministic behavior**
  ADC behaves consistently and predictably. The same input produces the same structural output every time.
* **Tooling-first design**
  ADC is designed as a technical foundation. The CLI is an interface on top of the format, not the core of it.
* **Extensible without legacy constraints**
  The format can evolve without being locked into decades of backward-compatibility decisions.
* **Cross-platform by design**
  ADC archives behave identically across supported operating systems.
* **Fully transparent and open**
  The format is inspectable, understandable, and auditable. No black boxes, no closed specifications.
* **Built for engineers**
  ADC is focused, explicit, and controlled. It is designed for people who want to understand and own their tooling.

## Issues

Create an issue easily without the need for a GitHub account via [this form](https://docs.google.com/forms/u/0/d/e/1FAIpQLSckLmPxVy7rW30_va7YpE42GAY5UKZqD8tjQgrSGWdbfRJUvA/viewform?usp=form_confirm).

## Update Schedule

I select a date myself what is the best time, cuz i have work. Meanwhile, the rolling release Python source script [ADC Aurora](https://github.com/Mealman1551/ArchivedDataCodec/tags) will be updated monthly.

#### Release flow

1. Development starts on the `Develop` branch
2. When code is stable on `Develop`, it will me snapshoted to an Aurora (Testing) tag (You need to compile yourself)
3. If Aurora is stable it will be ported to a stable build.

## Contributing

Contributions are welcome! See the [CONTRIBUTING.md](/docs/CONTRIBUTING.md) file.

## Contact

Have questions or want to learn more? open issues on the main repository on GitHub. (Mealman1551/ArchivedDataCodec)

---

## Notes

If you want to support the project please consider a small donation: <a href="https://www.paypal.com/donate/?hosted_button_id=LEE83CJJ2BEJC">
<img src="https://centerproject.org/wp-content/uploads/2021/11/paypal-donate-button-high-quality-png-1_orig.png" alt="Donate button" width="100"/>
</a>

---

### No macOS support

ADC Archiver does **NOT** support macOS, and it never will.
This is a deliberate decision to take a stand against the growing dominance of proprietary ecosystems and Apple’s developer restrictions.
This project supports **open platforms only**: Windows and Linux/Unix.

You can ofc run the source code but official binaries and/or setups are not compiled for macOS!

---

## Supported Versions

| Version | Release Type | Supported | EOL (End Of Life) |
| ------- | ------------ | --------- | ----------------- |
| 1.5.x   | Regular      | ✅        | 14-5-2027         |
| 1.4.x   | LTS          | ✅        | 18-10-2029        |
| 1.3.x   | Regular      | ❌        | 15-08-2026        |
| 1.2.0   | Regular      | ❌        | 15-05-2026        |
| 1.1.0   | Regular      | ❌        | 15-05-2026        |
| 1.0.0   | Regular      | ❌        | 15-11-2025        |

Current version is: 1.5

## Build ADC

> [!Note]
> For compiling on Python 3.13 and up, a C compiler is required. On Linux, GCC is sufficient. On Windows, MSVC (cl.exe) is required via Visual Studio Build Tools 2022. Python 3.12 can compile without a C compiler using MinGW64.

### Building on Windows

[Instructions on building on Windows](https://github.com/Mealman1551/ArchivedDataCodec/wiki/Building-ADC-on-Windows)

### Building on Linux

#### Preparing build environment on Linux

Install dependencies:

```bash
sudo apt install build-essential python3-pip python3-tk make patchelf ccache scons
```

Ensure Python 3.10+:

```bash
python3 --version
```

##### Cloning the repository

```bash
git clone --branch development/1.5 --single-branch https://github.com/Mealman1551/ArchivedDataCodec.git
```

Enter directory:

```bash
cd ArchivedDataCodec
```

Install additional dependencies:

```bash
make deps-linux
```

Restart or logoff to apply packages.

#### Start building on Linux

> [!Warning]
> Do ***NOT*** run the binary while compiling!

> [!Note]
> Reboot or logoff after installing via ``make install``

Compile latest version:

```bash
make linux
```

Run the binary:

```bash
cd dist
./adc.bin
```

Clean build:

```bash
make clean-linux
```

Debug build (optional):

```bash
make debug-linux
```

To install:

```bash
make install # Linux only
```

---

###### Made with 💚 by Mealman1551

---

###### © 2024 - 2026 Mealman1551 – The ADC Project and [contributors](community/contributors.txt)
