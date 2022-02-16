# HashSpot
Helps identifying what algorithm has been used to produce an hash

## Getting Started

### Installation

HashSpot has no external dependencies, so you only need to clone the repository to start using it.

### Usage

HashSpot is very straightforward. Start by running:
```powershell
> python hashspot.py
```

#### Single Checking

By selecting the option #1 on the menu, you will be prompted to enter an hash. HashSpot will be checking the provided hash and will return the possible algorithms that could generate it, based on what it has stored. These will be provided in order, from the most likely one to the less likely (based on algorithm popularities).

#### Bulk Checking

The second option, bulk checking, will first ask for a text file (adding `.txt` to the file name is optional since if it is not provided, HashSpot will add it by itself). It will then ask for another file name (non-existent) to output the results to. Again, providing HashSpot with the `.txt` extension is optional.

## Errors, Bugs and feature requests

If you find an error or a bug, please report it as an issue.
If you wish to suggest a feature or an improvement please report it in the issue pages.
Feel free to fix bugs or add features on your own and submit as pull requests.
Adding more algorithms for it to identify is highly looked up to.