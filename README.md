# Inbound

_An agnostic software building system._

![Inbound](https://cdn.tohoku.ac/inbound-banner.jpg)

Inbound is a normalisation layer for GNU Make. It is the first stop that
good code takes on its run through the developmental quartet; after
building with Inbound, it can be packaged with Outbound, distributed
with Rebound, and procured with
[Earthbound](https://github.com/aquefir/earthbound)&mdash;all in an
_ecosystem-agnostic_ fashion. In other words, even if you use Inbound
alone, you still get the full experience. &#128519;

-----

## Getting started

The way we recommend getting started with Inbound is by procuring it
with Earthbound. An Earthbound INI is provided in `etc/` to do this.

Alternatively, you can vendor the two necessary sources, `prologue.mk`
and `epilogue.mk`, from the `src/` folder in this repository. Once you
have those two files, copy over and open for editing the example
Makefile inside `etc/`. Adjust their `include` lines so the paths are
valid and squadalah, you&rsquo;re off!

Inbound is structured to keep your main Makefiles as normal and sensible
as possible. When you have to change something or compensate for an edge
case, things should work all the same &ndash; Inbound won&rsquo;t get in
your way.

## Host platforms

In general, Inbound is meant to only depend on an operating system that
is compliant with POSIX.1-2001. In practise, however, this presently
only includes GNU/Linux and Apple macOS, because those are the only
POSIX-compliant systems that are also target platforms of Inbound.

GNU/Linux and Apple macOS also have one difference between them: only
the former supports [Bochs](https://github.com/bochs-emu/Bochs) and
[QEMU user mode](https://www.qemu.org/docs/master/user/main.html), which
is required for testing architectures non-natively and running any test
suites. Apple macOS is currently required for producing Mach-O binaries,
although this limitation may (hopefully) go away in the future.

## Target platforms

Inbound should be able to facilitate building native machine code for
the following architectures:

- IA-16 (original 8086 &amp; optionally 8087, i286, i287)
- IA-32 (i386 &amp; optionally i387, MMX, SSE2)
- Intel 64 (Nocona/K6 &amp; optionally AVX, AVX2, AVX512)
- ARMv4T (ARM7TDMI with Thumb-1 interworking)
- ARMv5TE (ARM946)
- ARMv6K (ARM11 MPCore)
- ARMv8.4-A (Apple M1)
- SPARC V9 (UltraSPARC T1)

Although targeting of the relevant hardware systems is the ideal, a
virtualisation (or emulation in the case of IA-16) approach is used.
This is only intended to work on Linux hosts. IA-16 with the IBM-PC is
supported using [Bochs](https://github.com/bochs-emu/Bochs) and all
other architectures are supported with semi-hosted ELF binaries using
[QEMU user mode](https://www.qemu.org/docs/master/user/main.html).

The following systems should be targetable on the architectures shown in
this table using Inbound:

| System                        | Architecture     | Object code |
|-------------------------------|------------------|:-----------:|
| MS-DOS 6.22                   | IA-16            | _none_      |
| Microsoft Windows 3.11        | IA-16 with i286  | PE          |
| Microsoft Windows 4.0         | IA-32            | PE          |
| Microsoft Windows NT 3.1      | IA-32            | PE          |
| Microsoft Windows NT 5.2      | Intel 64         | PE          |
| GNU/Linux with `glibc-compat` | Intel 64         | ELF         |
| Nintendo Game Boy Advance     | ARMv4T           | ELF         |
| Nintendo DS                   | ARMv5TE + ARMv4T | ELF         |
| Nintendo 3DS                  | ARMv6K + ARMv5TE | ELF         |
| Apple macOS 10.4              | Intel 64         | Mach-O      |
| Apple macOS 11                | ARMv8.4-A        | Mach-O      |

GNU/Linux is targeted with `glibc` but using `musl` with its
`glibc-compat` interposer to ensure cross-`libc` compatibility.

While some systems are more flexible in supporting many architectures,
a single architecture has been chosen for each system to keep complexity
manageable.

## Compiling and contributing

In lieu of proper `COMPILING` and `CONTRIBUTING` documents in the
project repository&rsquo;s root, here are some notes about the process:
- Inbound does not&mdash;and should not&mdash;employ a build step
	- An emplacement technique is used to update Bitbound as embedded
	  into the Makefile sources; see `util/emplbb.py` for details
- A test suite of _Hello, World!_ programs is being developed to ensure
  the efficacy of Inbound; it will only use Bochs and QEMU user mode
- Inbound is licenced under the BSD-2-Clause; see the `COPYING` document
  for full terms
