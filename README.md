# DANPOS3

For questions on this code, please feel free to checkout: 
- The DANPOS project forum at: https://groups.google.com/forum/#!forum/danpos
- The Issues tab
- The Discussions tab(work in progress right now!)

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
1. Install as a bioconda package(new!)
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
Then you can run `cd DANPOS` to move to the correct directory.
You can also scroll up to the "code" button and look at the clone options there. Make sure you're cloning off of the main branch!


To build from source you have 3 options:
1. Build with conda(or pixi). I have included both the recipe.yaml and meta.yaml.
2. `pip install .`. Installs the package from the cloned code. I have included a pyproject.toml for this.
3. Run as a module(`python -m`)
#### Build with Conda(recipe.yaml)
This method uses the newer v1 recipe format.

Install the build tool (if not already installed):
```
conda install -c conda-forge rattler-build
```
Build the package from your local recipe.yaml:
```
rattler-build build --recipe recipe.yaml
```
Install the freshly built package into your environment:
```
conda install --use-local danpos
```
#### Build with Conda(meta.yaml)
This uses the standard conda-build tool that has been the industry standard for years.

Install the build tool:
```
conda install conda-build
```
Build the package from your local meta.yaml
```
conda build .
```
Install the locally built package
```
conda install --use-local danpos
```
#### Build with Pixi
Build with rattler-build (via pixi global)
```
pixi global install rattler-build
rattler-build build --recipe recipe.yaml
```
Add the local build to a pixi project
```
pixi add --path ./path/to/generated/package.conda danpos
```
#### Build with Pip
Standard installation
```
pip install .
```
Editable mode (changes to code take effect immediately)
```
pip install -e .
```
#### Run as a python module
```
python -m danpos
```
### Package and Library versions
* Python >=3.7.6
* R version >=4.0.1
* samtools >=1.7
* Python Libraries
  * rpy2 >=3.3.3
  * argparse >=1.1
  * numpy >=1.18.5
  * pysam >=0.16.0.1

To test your environment for these packages, use the command:
```
python scripts/print_versions.py
```
