<p align="center">
  <img src="https://raw.githubusercontent.com/The-ADC-Archiver-Project/Assets/refs/heads/main/banner/ADC%20banner.jpg" alt="ADC Banner" width="200">
</p>

# ADC (ArchivedDataCodec)

[![GitHub license](https://img.shields.io/github/license/Mealman1551/ADC)](#)
[![Platform: Windows/Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue.svg)](#)
[![Development](https://img.shields.io/badge/Development-Active-brightgreen)](#)
[![Latest version](https://img.shields.io/github/v/release/Mealman1551/ADC?label=Latest%20stable%20version&color=brightgreen)](https://github.com/mealman1551/adc/releases/latest)
[![Status](https://img.shields.io/badge/Status-Development-red)](#)
[![GitHub repo size](https://img.shields.io/github/repo-size/Mealman1551/ADC)](#)
[![GitHub issues](https://img.shields.io/github/issues/Mealman1551/ADC)](https://github.com/Mealman1551/ADC/issues)
[![GitHub stars](https://img.shields.io/github/stars/Mealman1551/ADC)](#)
[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](#)
[![CodeQL](https://github.com/Mealman1551/ArchivedDataCodec/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Mealman1551/ArchivedDataCodec/actions/workflows/github-code-scanning/codeql)
[![Build Status](https://github.com/Mealman1551/ADC/actions/workflows/build.yml/badge.svg)](https://github.com/Mealman1551/ADC/actions/workflows/build.yml)
[![Mirror to GitLab](https://github.com/Mealman1551/ArchivedDataCodec/actions/workflows/gitlab-mirror.yml/badge.svg?branch=main)](https://github.com/Mealman1551/ArchivedDataCodec/actions/workflows/gitlab-mirror.yml)
![Total Downloads](https://img.shields.io/badge/dynamic/json.svg?url=https://raw.githubusercontent.com/Mealman1551/ArchivedDataCodec/main/.github/downloads.json&query=$.total_downloads&label=Total%20Downloads&color=97CA00)


**Mailing list:** [Subscribe](https://www.freelists.org/list/adc) | [Archive](https://www.freelists.org/archive/adc)

**Main announcements:** [Mail archive](https://the-adc-archiver-project.github.io/adc-mail-archive) (look for "[ANN]" label)

**Community:** [Forum](https://groups.google.com/g/adc-archiver) | IRC: OFTC #adc-archiver | [Matrix](https://matrix.to/#/#adc-archiver:matrix.org) | [XMPP](xmpp:vuwirer@chat.disroot.org?join)


Compatible with: <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg" alt="Windows 11" width="20"/> **&** <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="Linux" width="20"/>

# ADC develop branch

Realtime development


## Download

ADC development branch Source code download 

| Platform: | Download                                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------|
| Windows   | [sourcecode.zip](https://github.com/Mealman1551/ArchivedDataCodec/archive/refs/heads/develop.zip)       |
| Linux     | [sourcecode.tar.gz](https://github.com/Mealman1551/ArchivedDataCodec/archive/refs/heads/develop.tar.gz) |


## License

ADC Archiver is dual-licensed.

You may use, modify and distribute ADC Archiver under the terms of the
GNU General Public License v3 (GPLv3).

If you provide ADC Archiver as a network service, SaaS, or through a remote
or online virtual machine environment, the GNU Affero General Public License v3 (AGPLv3) applies.

See [LICENSE](LICENSE) and [LICENSE_AGPLv3](LICENSE_AGPLv3) for the full license texts.

## Issues

Create an issue easily without the need for a GitHub account via [this form](https://docs.google.com/forms/u/0/d/e/1FAIpQLSckLmPxVy7rW30_va7YpE42GAY5UKZqD8tjQgrSGWdbfRJUvA/viewform?usp=form_confirm).

#### Release flow

1. the develop branch is an upstream development branch
2. if code works stable enough, a new tag is created for Aurora (testing branch)
3. After Aurora is stable enough it will be ported to stable.


## Contributing

Contributions are welcome! See the [CONTRIBUTING.md](docs/CONTRIBUTING.md) file.

## Contact

Have questions or want to learn more? Open an issue in the GitHub repository. [Open the issues page](https://github.com/Mealman1551/ArchivedDataCodec/issues)
---

## Notes

If you want to support the project please consider a small donation: <a href="https://www.paypal.com/donate/?hosted_button_id=LEE83CJJ2BEJC">
<img src="https://centerproject.org/wp-content/uploads/2021/11/paypal-donate-button-high-quality-png-1_orig.png" alt="Donate button" width="100"/>
  
  ---

## Build ADC

> [!Note]
> For compiling on Python 3.13 and up, a C compiler is required. On Linux, GCC is sufficient. On Windows, MSVC (cl.exe) is required via Visual Studio Build Tools 2022. Python 3.12 can compile without a C compiler using MinGW64.

### Building on Windows

#### Preparing build environment on Windows

Please disable Windows Defender as it may block compilation.

##### Installing Make

Options to install GNU Make:

**Option 1 — WinGet**

```
winget install GnuWin32.Make
```

Add Make to PATH. [More info](https://leangaurav.medium.com/how-to-setup-install-gnu-make-on-windows-324480f1da69)

**Option 2 — Chocolatey (Recommended)**

```
choco install make
```

##### Cloning the repository

```bash
 git clone --branch develop --single-branch https://github.com/Mealman1551/ArchivedDataCodec.git
```



##### Installing Python and VS Build Tools

1. Install Python 3.13.x (64-bit). Ensure pip is installed and Python is added to PATH.

```
python --version
```

2. Install Visual Studio Build Tools 2022:

```powershell
winget install Microsoft.VisualStudio.2022.BuildTools --override "--add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
```

3. Open VS Developer PowerShell:

```powershell
Import-Module "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\Microsoft.VisualStudio.DevShell.dll"
Enter-VsDevShell -VsInstallPath "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools" -DevCmdArguments "-arch=x64 -host_arch=x64"
```

Then:

```powershell
cd ArchivedDataCodec
```

Then:

```
make deps-windows
```

#### Start building on Windows

> [!Warning]
> Do ***NOT*** run the binary while compiling!

> [!Warning]
> Do ***NOT*** install MinGW64 if Nuitka asks for it.
> You ***CAN*** install depends.exe if Nuitka asks for it.

Compile the latest version:

```powershell
make windows
```

Run the binary:

```powershell
cd dist
./adc.exe
```

Clean build:

```powershell
make clean-windows
```

Debug build (Optional) Only use if you really need to, normally `make windows` is the best option:

```powershell
make debug-windows
```

---

### Building on Linux

#### Preparing build environment on Linux

Install dependencies:

```bash
sudo apt install build-essential pip python3-tk make patchelf ccache scons
```

Ensure Python 3.10+:

```bash
python3 --version
```

##### Cloning the repository

```bash
 git clone --branch develop --single-branch https://github.com/Mealman1551/ArchivedDataCodec.git
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
make install #Linux only
```

---

###### Made with 💚 by Mealman1551

---

###### © 2024 - 2026 Mealman1551 – The ADC Project and [contributors](community/contributors.txt)

###### Licensed under the GNU GPL v3.0 - ADC is Libre software.
