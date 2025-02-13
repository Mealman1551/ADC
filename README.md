![banner](img/banner/Bannerfull.jpg)

[ADC contact e-mail address](mailto:adc@linuxmail.org)

IRC channel: #adcarchiver on OFTC

# ADC (ArchivedDataCodec)
![License: GPL-3.0](https://img.shields.io/badge/License-GNU%20GPL--3.0-orange.svg)
![Platform: Windows/Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.x-yellow.svg)
![Development](https://img.shields.io/badge/Development-Active-brightgreen)
![Latest version](https://img.shields.io/badge/Latest%20version-1.2.0-brightgreen)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)]()

Compatible with: <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg" alt="Windows 11" width="20"/> **&** <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="Linux" width="20"/>

**ADC (ArchivedDataCodec)** is an open-source <img src="https://raw.githubusercontent.com/Mealman1551/ADC/362a969f45ab6f17883ec68cb6172dc4ad3ce58b/img/svg/open-source-icn.svg" alt="Open-Source" width="30"/> file extension and archiving/compression tool that uses zlib for efficient compression and decompression of various file types. With a simple command-line interface, ADC supports both Windows and Linux, making it easy for users to archive and extract files.

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
- Python 3.x
- Zlib library (typically included with Python)
- Tkinter

***Users***
#### Windows
- Windows 10 or higher
#### Linux
- A Linux distro
- Python3
- Tkinter

## Installation

### Windows
1. Download the official installer here: [![Windows](https://custom-icon-badges.demolab.com/badge/ADC%20Setup-0078D6?logo=windows11&logoColor=white)](https://github.com/Mealman1551/ADC/releases/tag/ADC_Archiver_v1.2.0)

SHA-256 checksum: `04B705C23304055888151BA9A48E2A3FEBA7FA31422A9629AF72F979567C1266`

or download the Nullsoft alpha installer here: [ADC.Archiver.1.2.0.NSIS.alpha.setup.exe](https://github.com/Mealman1551/ADC/releases/download/ADC_Archiver_v1.2.0/ADC.Archiver.1.2.0.NSIS.alpha.setup.exe)

SHA-256 checksum: `1b2815700d43abffeaddf004a9dac31243eb4a868cf8a88904d17e6df11311e3`


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
  <summary>CentOS (RHEL)</summary>

  ```bash
  sudo yum install git
  ```

  **For CentOS 8+ and RHEL 8+ (with dnf):**
  ```bash
  sudo dnf install git
  ```
</details>

<details>
  <summary>openSUSE</summary>

  ```bash
  sudo zypper install git
  ```
</details>

<details>
  <summary>Arch Linux</summary>

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
    cd ~/adc/Linux-release
    ```
4. Grant execution permissions:
    ```bash
    chmod +x adc1.2
    ```
5. Run the script:
    ```bash
    ./adc1.2
    ```

SHA-256 checksum: `8F5D0B2DA09BCD057C84E5B087995A52D76E492CDBE341DC2268613E611A1A8D`

## Usage

Download the setup for Windows or use Git clone in Linux and run the executable.

## License

This project is licensed under the [GNU GPL-3.0 License](LICENSE). You are free to use, modify, and distribute it under the terms of the license.

## Issues

Create an issue easily without the need for a GitHub account via [this form](https://docs.google.com/forms/d/e/1FAIpQLSckLmPxVy7rW30_va7YpE42GAY5UKZqD8tjQgrSGWdbfRJUvA/viewform).

## Update Schedule

There will be two major stable updates per year. Meanwhile, the rolling release Python source script [ADC Aurora](https://github.com/Mealman1551/ADC/tree/ADC-Unstable-(Aurora)) will be updated monthly, if not weekly.

## Contributing

Contributions are welcome! Open an issue or submit a pull request if you'd like to contribute.

## Contact

Have questions or want to learn more? Feel free to reach out via [this mail address](mailto:adc@linuxmail.org).

## Notes

For testing see: [ADC Testing on GitLab](https://gitlab.com/Mealman1551/adc-archiver)
***DO NOT USE THIS AS MAIN SOURCE, THIS IS TESTING ONLY!***

---

![Made with ❤️](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20by%20Mealman1551-blue?style=for-the-badge)

###### © 2025 Mealman1551

