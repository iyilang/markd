# iyi-markd

A port of [markd](https://github.com/icyleaf/markd) 0.5.0 (commit
`d61dd52d40e659b53cb78712a7b1190cfdb9bc66`), written in iyi with no Crystal
code and no Crystal standard library underneath.

The upstream CommonMark, smart punctuation, and regression examples run
against the port.

iyi's module boundaries change the names of the options, parser, node, and
renderer types. Entity decoding and encoding live in markd modules rather
than reopening `HTML`. See [PORTING.md](PORTING.md) for the example map and
differences.

## Usage

After release, add the package with `iyi get github.com/iyilang/markd --as markd`.

```iyi
import markd

puts Markd.to_html("# Hello")
```

To encode HTML entities, import `markd/h_t_m_l_entities/encoder` and call
`Markd::HTMLEntities::Encoder.encode_entities`.

## Reach

`iyi mod reach` reports `std/env, std/random, std/time`. Optional timing
uses `std/time`, which imports `std/env` for time-zone configuration. URI
handling imports `std/idna`, whose `std/slice` and `std/indexable` imports
reach `std/random`. The parser does not call the environment or randomness
APIs directly.

## Platform notes

CI uses iyi 0.21.0 on Linux, macOS, and Windows. Windows uses the x86-64
release and requires the Visual C++ build tools with the Windows SDK, such as
Visual Studio Build Tools with the "Desktop development with C++" workload.
The compiler locates the toolchain through the Windows registry.

## Development

```sh
iyi test .
iyi fmt --check markd.iyi markd_test.iyi markd
```
