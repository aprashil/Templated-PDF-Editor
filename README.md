# Templated PDF editor

Templated PDF Editor is a python based application that replaces template fields in pdf files with additionally specified values.

## Non-Builtin Packages Used
1) [pdfminer.six](https://pypi.org/project/pdfminer.six/)
2) [fpdf](https://pypi.org/project/fpdf/)

## Usage
- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
 the required modules `pdfminer.six` and `fpdf`.

```bash
pip install pdfminer.six
pip install fpdf
```

- Run index.py manually or via the command line with the required arguments.

```bash
python index.py {templatePath} {valuesPath}
```
- Feel free to delete the already existing `template.pdf` and `values.json` files.

## Test
```bash
python index.py template.pdf values.json
```
## Contributing
Pull requests are welcome.

