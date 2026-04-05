# DANPOS3

For questions on this code, please feel free to checkout the DANPOS project forum at: 
https://groups.google.com/forum/#!forum/danpos

## Background

This repo contains updated code from DANPOS3.
* This package was originally forked from code from danpos-2.2.2 (Jun 15 10:20) which is dependent on python 2.7
 * https://sites.google.com/site/danposdoc/download/danpos-2.2.2.tgz
* It was then forked from danpos-3.2.1
* For information on how to use Danpos3 commands please see the Danpos2 manual at :
https://sites.google.com/site/danposdoc/ where this code originated from.

## Summary

This code was written to conintue maintaining DANPOS, which previously has not been maintained in more than a year.

## Installation
To install, you may do it one of 2 ways.
1. ~~Install as a bioconda package(new!)~~ Temporarily broken, sorry!
2. Build from source

### Bioconda install
#### If you're using pixi:
Configure pixi to use bioconda in addition to it’s default (conda-forge):
```
pixi config set default-channels '["conda-forge", "bioconda"]'
```
Afterwards, you can install DANPOS from bioconda globally:
```
pixi global install danpos3
```
or locally into an environment associated with a directory:
```
cd myproject
pixi init
pixi add danpos3
```
While globally installed packages are available everywhere on your system, locally installed packages are only available when you activate the associated environment via:
```
pixi shell
```
in the respective directory. For more options and details see the pixi documentation.

#### If you're using conda:
Make sure you add the correct channels:
```
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
```
Then install:
```
conda install danpos3
```
### Build from source(this was taken from the source, but modified). 
To download the repository
```
git clone https://github.com/boenc28-cmyk/DANPOS
```

To install the exact versions of the dependencies use type:
```
cd DANPOS
pip install -r requirements.txt
```

[To be able to execute these scripts from other directories 
easily, please set your current working directory to your
$PATH variable.](https://opensource.com/article/17/6/set-path-linux)

You can also scroll up to the "code" button and look at the clone options there. Make sure you're cloning off of the main branch!

### Package and Library versions
* Python 3.7.6
* R version 4.0.1
* samtools 1.7 using htslib 1.7
* Python Libraries
  * rpy2 3.3.3
  * argparse 1.1
  * numpy 1.18.5
  * pysam 0.16.0.1

To test your environment for these packages, use the script `print_versions.py`
