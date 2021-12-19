# myApp
Demonstrate a dummy app release with CI-CD


## Local testing
### Local run app

```BASH
cd src
python -m StarterApp
```

### Local Build, Install and run

1. Build
    ```BASH
    cd src
    python setup.py build sdist bdist
    ```

2. Install
    ```BASH
    cd src/sdist
    # below version may change
    pip install myapp-1.0.0.tar.gz
    ```

3. Run 
    ```BASH
    # anywhere in your system
    myapp
    ```