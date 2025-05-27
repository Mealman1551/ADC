![banner](img/banner/Bannerfull.jpg)

[ADC contact e-mail address](mailto:adc@linuxmail.org)

IRC channel: #adcarchiver on OFTC

[Forum](https://groups.google.com/g/adc-archiver)

[Gitter](https://matrix.to/#/#adc:gitter.im)

# ADC (ArchivedDataCodec)
[![GitHub license](https://img.shields.io/github/license/Mealman1551/ADC)](#)
[![Platform: Windows/Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue.svg)](#)
[![Python Version](https://img.shields.io/badge/Python-3.12.x-yellow.svg)](#)
[![Development](https://img.shields.io/badge/Development-Active-brightgreen)](#)
[![Latest version](https://img.shields.io/github/v/release/Mealman1551/ADC?label=Latest%20version&color=brightgreen)](https://github.com/mealman1551/adc/releases/latest)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)
[![GitHub repo size](https://img.shields.io/github/repo-size/Mealman1551/ADC)](#)
[![GitHub issues](https://img.shields.io/github/issues/Mealman1551/ADC)](https://github.com/Mealman1551/ADC/issues)
[![GitHub stars](https://img.shields.io/github/stars/Mealman1551/ADC)](#)
[![CodeQL](https://github.com/mealman1551/ADC/actions/workflows/codeql.yml/badge.svg)](https://github.com/mealman1551/ADC/actions/workflows/codeql.yml)


For Build Status and GitLab Sync status go [here](https://github.com/Mealman1551/ADC?tab=readme-ov-file#build--sync-status)

Compatible with: <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg" alt="Windows 11" width="20"/> **&** <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="Linux" width="20"/>

**ADC (ArchivedDataCodec)** is an open-source <img src="https://raw.githubusercontent.com/Mealman1551/ADC/362a969f45ab6f17883ec68cb6172dc4ad3ce58b/img/svg/open-source-icn.svg" alt="Open-Source" width="30"/> file extension and archiving/compression tool that uses Zlib for efficient compression and decompression of various file types. With a simple command-line interface, ADC supports both Windows and Linux, making it easy for users to archive and extract files.

ADC Archiver uses a byte-key of 4, meaning that it can create archives up to 4GB. This limit is ideal for standard file archiving but may not be suitable for very large files or datasets. Future stable updates may include support for larger archives. [ADC Aurora](https://github.com/Mealman1551/ADC/tree/ADC-Unstable-(Aurora)) is currently experimenting with a higher byte-key.

For the unstable/rolling release see: [ADC Aurora](https://github.com/Mealman1551/ADC/tree/ADC-Unstable-(Aurora))

## Features

- **Great Compression Algorithm**: Utilizes zlib for efficient compression.
- **Cross-Platform**: Compatible with both Windows and Linux.
- **Command-Line Interface**: Simple and intuitive interface.
- **Support**: Supports a wide range of file types.

## Getting Started

### Prerequisites
***Developers:***
- Python 3.12.x
- zlib library (typically included with Python)
- tkinter
- progress
- progress.bar
- colorama

***Users***
#### Windows
- Windows 8 or higher
#### Linux
- A Modern Linux distro that has at least glibc 2.34

## Installation

### Windows
1. Download the official installer here: [![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white)](https://github.com/Mealman1551/ADC/releases/latest)


Don't like the setup, won't the setup run or want a portable version. you can compile from source.

[Compile ADC](https://github.com/Mealman1551/ADC-compile-from-scratch)


### Linux

##### Installation via Terminal (for more options, visit the [Wiki!](https://github.com/Mealman1551/ADC/wiki/Linux-installation))

1. Install Git:
<details>
  <summary>Debian (Ubuntu, Mint etc.)</summary>

  ```bash
  sudo apt update
  sudo apt install git
  ```
</details>

<details>
  <summary>Fedora</summary>

  ```bash
  sudo dnf install git
  ```
</details>

<details>
  <summary>RHEL and RHEL-like OS'es</summary>

  ```bash
  sudo yum install git
  ```

  **For CentOS 8+ and RHEL 8+ (with dnf):**
  ```bash
  sudo dnf install git
  ```
</details>

<details>
  <summary>SLE & openSUSE</summary>

  ```bash
  sudo zypper install git
  ```
</details>

<details>
  <summary>Arch Linux and Arch based distributions</summary>

  ```bash
  sudo pacman -S git
  ```
</details>

<details>
  <summary>Alpine Linux</summary>

  ```bash
  sudo apk add git
  ```
</details>

<details>
  <summary>Gentoo</summary>

  ```bash
  sudo emerge --ask dev-vcs/git
  ```
</details>

<details>
  <summary>Void Linux</summary>

  ```bash
  sudo xbps-install -S git
  ```
</details>

<details>
  <summary>Flatpak</summary>

  ```bash
  sudo flatpak install flathub com.git.Git
  ```
</details>

<details>
  <summary>Snap</summary>

  ```bash
  sudo snap install git --classic
  ```
</details>



2. Clone the repository:
    ```bash
    git clone https://github.com/Mealman1551/adc.git
    ```
3. Navigate to the project directory:
    ```bash
    cd ~/adc/linux-release
    ```
4. Extract the binary and dependecies:
    ```bash
    tar xf bin.tar.xz
    ```
5. Make it executable:
    ```
    chmod +x adc.bin
    ```

6. Run the script:
    ```bash
    ./adc.bin
    ```

### Unix (BSD, Solaris)

1. Install Python3

2. Donwload the source code from /src

3. Run the source code in python3

## Usage

Download the setup or clone the repo on Linux and install or follow above instructions for using the program

## License

This project is licensed under the [GNU GPL-3.0 License](LICENSE). You are free to use, modify, and distribute it under the terms of the license.

## Issues

Create an issue easily without the need for a GitHub account via [this form](https://tally.so/r/3EAlrr).

## Update Schedule

There will be two major stable updates per year, 15 may and 15 november. Meanwhile, the rolling release Python source script [ADC Aurora](https://github.com/Mealman1551/ADC/tree/ADC-Unstable-(Aurora)) will be updated monthly, if not weekly.

## Contributing

Contributions are welcome! Open an issue or submit a pull request if you'd like to contribute.

Also see the CONTRIBUTING.md file

## Contact

Have questions or want to learn more? Feel free to reach out via [this mail address](mailto:adc@linuxmail.org).

## GitLab

I have 2 ADC Repos on Gitlab, one is a continously updated mirror of the Main branch (Stable only), and the other is a testing repo

Mirror/Main(Stable) GitLab repo of ADC: [ADC on GitLab](https://gitlab.com/Mealman1551/ADC)

Unstable (Aurora) is only on GitHub!

---

For testing see: [ADC Testing on GitLab](https://gitlab.com/Mealman1551/adc-testing)
#### ***DO NOT USE TESTING REPO AS MAIN SOURCE, THIS IS TESTING ONLY!***

---

### Syncing to GitLab

Syncing to GitLab is done via the [`gitlab-sync.yml`](https://github.com/Mealman1551/ADC/blob/main/.github/workflows/gitlab-sync.yml) file in `/main/.github/workflows/gitlab-sync.yml`

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

## Build & Sync Status

| Workflow      | Status        |
|---------------|---------------|
| **Build Status** | [![Build Status](https://github.com/Mealman1551/ADC/actions/workflows/build.yml/badge.svg)](https://github.com/Mealman1551/ADC/actions/workflows/build.yml) |
| **GitLab Sync**  | [![GitLab Sync Status](https://github.com/Mealman1551/ADC/actions/workflows/gitlab-sync.yml/badge.svg?branch=main)](https://github.com/Mealman1551/ADC/actions/workflows/gitlab-sync.yml) |
|               |               |

**Build Status**: Builds and compiles ADC's source code with Nuitka and testing binary after it for errors.

**GitLab Sync**: Syncing Main branch to GitLab.

---


![Made with ❤️](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20by%20Mealman1551-blue?style=for-the-badge)

###### © 2025 Mealman1551

