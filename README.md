# My HackerRank exercices

See https://www.hackerrank.com/

## Installation

Bash 5 is needed for some complex exercises.

    brew install bash

## Running

Most applications need some input to be piped in standard input. The various samples
are not included. Go to the HackerRank site, locate the exercice by using the source
file's name and create a sample file `test.txt` holding it.

You can then run, for example:

````bash
cd statistics
cat ../test.txt | cargo run -- poisson-distribution
````

In order to facilitate testing, any file named `test.txt` or `test2.txt` at the root
of this project is ignored by Git.

## Authors

* [HackerRank](https://www.hackerrank.com/) for script templates
* Farzad FARID <[farzy@farzy.org](mailto:farzy@farzy.org)>
