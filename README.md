# Magic Calculator

Magic Calculator is a Python package that contains magic functions for random calculation along with normal functions for simple calculation. 

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Magic Calculator like below. 
Rerun this command to check for and install updates .

> pip install magic_calculator

## Usage
Features:
* functions.add
> add 2 numbers
* functions.sub
> subtract 2 numbers
* functions.mult
> multiply 2 numbers
* functions.div
> divide 2 numbers
* decorators.magic
> perform magic operation like random calculation

#### Demo of some of the features:

```python
import magic_calculator.functions as mcf
import magic_calculator.decorators as mcd

sum_num = mcf.add(2,4)

mag_cal = mcd.magic(5,7)

```

## Contributing
For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
