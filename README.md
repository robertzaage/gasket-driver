# Coral Gasket Driver

[![copr build status](https://copr.fedorainfracloud.org/coprs/robertzaage/gasket-dkms/package/gasket-dkms/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/robertzaage/gasket-dkms/package/gasket-dkms/)

The Coral Gasket Driver allows usage of the [Coral EdgeTPU](https://coral.ai/) on Linux systems. The driver contains two modules:

* Gasket: Gasket (Google ASIC Software, Kernel Extensions, and Tools) is a top level driver for lightweight communication with Google ASICs.
* Apex: Apex refers to the [EdgeTPU v1](https://coral.ai/technology)

This driver landed in the staging of [4.19 kernel tree](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=9a69f5087ccc20bb411025decab455836df04168) and was removed due to discontinued development in [kernel version 5.13](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=918ce05bbe52df43849a803010b4d2bcd31ea69c).
Google also publishes [DKMS packages](https://coral.googlesource.com/gasket-dkms-debian/) for Debian-ish distros. Unfortunately that doesn't help non-Debian-ish users running kernels without this driver built in and package managers which aren't deb-based.

This RPM/DKMS package is based on corals master branch and is build for Fedora 37 and later (rawhide).

## Installation

Releases from this repo are built/hosted on [Fedora copr](https://copr.fedorainfracloud.org/coprs/robertzaage/gasket-dkms/).
Currently, only Fedora 37 and rawhide builds are available.

Enable the repo:

```
# dnf copr enable robertzaage/gasket-dkms
```

Install the package after enabling the repo:

```
# dnf install gasket-dkms
```

Reboot your machine to activate the kernel module.

## Bugs?
Keep an eye on the kernel log and feel free to report bugs in corals official [repository](google-coral/edgetpu).
