## Tarantool CLI Go best-practices

This repo contains a simple CLI written in Go with tests and development
environment set up.

Code is placed in [`cli`](./cli) directory.

### Quick start

```bash
> mage build  # build supercli executable

> ./supercli --help  # list supercli help
This is the most powerful CLI in the world!

Usage:
  supercli [command]

Available Commands:
  hello       Say hello
  help        Help about any command

Flags:
  -h, --help      help for supercli
  -v, --version   version for supercli

Use "supercli [command] --help" for more information about a command.

> ./supercli hello  # run supercli hello command
Hello, world!
```

### Lint

* `go fmt` + `go vet` for Go
* `flake8` for Python

### Tests

* Unit tests use `go test`.
  See [`./cli/some_test.go`](./cli/some_test.go).

* Integration tests are written using `pytest`
  See [`test/integration`](./test/integration).

### CLI

* CLI library: `github.com/spf13/cobra`
* Logger: `github.com/apex/log` with `cli.Default` handler

There are global command flags that allow to specify log level:

* by default log level is `info`, long operations
  (like `tarantoolctl rocks make`) logs are replaced by spinner,
  but are shown on error
* `--verbose` - log level is `debug`, long operations logs are shown
* `--debug` - `--verbose` + temporary files and Docker images aren't deleted

### Tools

#### Magefile

[Magefile](https://magefile.org/) is used to build executable, run linter, tests
and publish packages to S3.
See [`magefile.go`](./magefile.go),
[`magefile.publish.go`](./magefile.publish.go).

```bash
mage build  # build supercli executable

mage lint  # run linter
mage unit  # run unit tests (see cli/hello/hello_test.go)
mage integration  # run integration tests (see test/integration)

mage test  # run linter, unit and integration tests

mage clean  # clean up
```

Magefile also contains command that can be used on GitHub Actions, such as

* `mage sdk` - Download Tarantool Enterprise to tmp/tarantool-enterprise dir
* `mage publishS3` - publish packages to S3


#### Goreleaser

[Goreleaser](https://github.com/goreleaser/goreleaser) is used to create DEB and
RPM packages for application.
It also creates tarballs with Linux and MacOS executables and creates a draft
release on GitHub with packages attached.
See [`.goreleaser.yml`](./.goreleaser.yml).

To build packages say

```bash
goreleaser release --rm-dist --skip-validate --skip-publish --snapshot
tree dist  # list created packages
```
