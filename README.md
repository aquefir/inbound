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

The way we recommend getting started with Inbound is by sourcing it with
Earthbound. An Earthbound INI file is provided in `etc/` to do this.

Alternatively, you can vendor the two necessary sources, `prologue.mk`
and `epilogue.mk`, from the `src/` folder in this repository. Once you
have those two files, copy over and open for editing the example
Makefile inside `etc/`. Adjust their `include` lines so the paths are
valid and squadalah, you&rsquo;re off!

Inbound is structured to keep your main Makefiles as normal and sensible
as possible. When you have to change something or compensate for an edge
case, things should work all the same &ndash; Inbound won&rsquo;t get in
your way.

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
This is only intended to work on Linux and BSD hosts. IA-16 with the
IBM-PC is supported using [Bochs](https://github.com/bochs-emu/Bochs),
and all other architectures are supported with semi-hosted ELF binaries
using [QEMU user mode](https://www.qemu.org/docs/master/user/main.html).

The following systems should be targetable on the architectures shown in
this table using Inbound:

| System                        | Architecture     |
|-------------------------------|------------------|
| MS-DOS 6.22                   | IA-16            |
| Microsoft Windows 3.11        | IA-16 with i286  |
| Microsoft Windows 4.0         | IA-32            |
| Microsoft Windows NT 3.1      | IA-32            |
| Microsoft Windows NT 5.2      | Intel 64         |
| GNU/Linux with `glibc-compat` | Intel 64         |
| Nintendo Game Boy Advance     | ARMv4T           |
| Nintendo DS                   | ARMv5TE + ARMv4T |
| Nintendo 3DS                  | ARMv6K + ARMv5TE |
| Apple macOS 10.4              | Intel 64         |
| Apple macOS 11                | ARMv8.4-A        |

GNU/Linux is targeted with `glibc` but using `musl` with its
`glibc-compat` interposer to ensure cross-`libc` compatibility.

While some systems are more flexible in supporting many architectures,
a single architecture has been chosen for each system to keep complexity
manageable.
