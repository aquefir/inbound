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
Earthbound. Alternatively, you can vendor the two necessary sources,
`prologue.mk` and `epilogue.mk`, from the `src/` folder in this
repository. Once you have those two files, copy over and open for
editing the example Makefile inside `etc/`. Adjust their `include` lines
so the paths are valid and squadalah, you&rsquo;re off!

Inbound is structured to keep your main Makefiles as normal and sensible
as possible. When you have to change something or compensate for an edge
case, things should work all the same &ndash; Inbound won&rsquo;t get in
your way.
