# hfmc
A Hypersonic Facility Modelling Code

### Notes
hfmc utilises the [gdtk](https://gdtk.uqcloud.net/) and the [Eilmer](https://gdtk.uqcloud.net/docs/eilmer/about/) CFD capability to model hypersonic ground test facilitity in high fidelity in 1D or 2D-axisymmetric models. Using the power of the compressible flow functionality implemented in the gdtk, hfmc can model everything from supersonic shock tubes to hypersonic expansion tube facilities.

### Setup
1. Clone the repository.

```
git clone git@github.com:tvdherik/hfmc
```

2. Navigate to /src/ and run 'make install'

```
make install
```

3. Add the following to your .bash_aliases (or .bashrc) file (enabling python to locate the hfmc package).

```
export HFMC=$HOME/hfmcinst
export PYTHONPATH=${PYTHONPATH}:${HFMC}/lib
```


### Usage (python 3.10.0+) (requires matplotlib and numpy)
```
import hfmc
```

_or use by command line_
