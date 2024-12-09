day 1- 31/08/2024 (module 1,2)
### Various ways creating a virtual environment 
- like we have npm to manage js pakages
- we have to do the same to lock our python project pakages so that it doesnot conflict with our code 
```python
    conda create -p {name of the virtual environment} python=={version of python}
    conda create -p venv python==3.10
    to active 
    conda activate venv
```
```python
   another way 
   python -m  venv myenv
   myenv\Scripts\activate

```
```python
   pip i virtualenv
   -p python3 virtual_env
   virtual_env\Scripts\activate
```
we can use the venv and install pakages in it and also use this kernel to execute the ipynb file

- "shift enter" to run jupyter notebook  

- python is dynameically typed language

