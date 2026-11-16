# Porting markd 0.5.0

Source: https://github.com/icyleaf/markd, tag v0.5.0, commit
`d61dd52d40e659b53cb78712a7b1190cfdb9bc66`.

The parser and renderer are the generated migration output and still require
Crystal. The native node, options, and HTML entity decoding modules are under
active porting. The package must not be released until all upstream examples
pass and the Crystal dependency is removed.
