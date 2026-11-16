# iyi-markd

A port of [markd](https://github.com/icyleaf/markd) 0.5.0 (commit
`d61dd52d40e659b53cb78712a7b1190cfdb9bc66`), written in iyi with no Crystal
code and no Crystal standard library underneath.

The upstream CommonMark, smart punctuation, and regression examples run
against the port. Release verification is still in progress.

iyi's module boundaries change the names of the options, parser, node, and
renderer types. Entity decoding lives in a markd module rather than reopening
`HTML`. The former `HTML.encode_entities` entry point has not been ported.
See [PORTING.md](PORTING.md) for the example map and differences.

## Usage

```iyi
import markd

puts Markd.to_html("# Hello")
```

## Development

```sh
iyi test .
iyi fmt --check markd.iyi markd_test.iyi markd
```
