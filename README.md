# {app name}
{description}

### installing with pip directly from Nexus:
Create requirements.txt file which includes the following
```text
--trusted-host nexus3.dev.4m-a.org
--extra-index https://${NEXUS_USERNAME}:${NEXUS_PASSWORD}@nexus3.dev.4m-a.org/repository/4m-pypi-development/pypi
--extra-index-url https://${NEXUS_USERNAME}:${NEXUS_PASSWORD}@nexus3.dev.4m-a.org/repository/4m-pypi-development/simple
--extra-index https://${NEXUS_USERNAME}:${NEXUS_PASSWORD}@nexus3.dev.4m-a.org/repository/4m-pypi-releases/pypi
--extra-index-url https://${NEXUS_USERNAME}:${NEXUS_PASSWORD}@nexus3.dev.4m-a.org/repository/4m-pypi-releases/simple
4ma-dict-model=={VERSION}.dev0
```
Then in terminal write the following
```commandline
export NEXUS_USERNAME=<nexus_username>
export NEXUS_PASSWORD=<nexus_password>
pip install -r requirements.txt
```

### Use it as a library:
```commandline
git clone https://github.com/4ma/<repo name>
```

#### Installation
Run under your venv:
```bash
pip install /path/to/built/wheel/xxxx_utils-x.x.x-py3-none-any.whl
```
 
### Examples
See: example_notebook

## License
Public library only  

## Comment
A version of Python 3.8 or lower is required to install Azure-core
A version of pandas 1.2.0 or lower is required in order to use .resample() function in time_agg_mean.py

### Dependencies
add to requirement.txt:

--trusted-host nexus3.dev.4m-a.org
--extra-index https://${NEXUS_USERNAME}:${NEXUS_PASSWORD}@nexus3.dev.4m-a.org/repository/4m-pypi-development/pypi
--extra-index-url https://${NEXUS_USERNAME}:${NEXUS_PASSWORD}@nexus3.dev.4m-a.org/repository/4m-pypi-development/simple
--extra-index https://${NEXUS_USERNAME}:${NEXUS_PASSWORD}@nexus3.dev.4m-a.org/repository/4m-pypi-releases/pypi
--extra-index-url https://${NEXUS_USERNAME}:${NEXUS_PASSWORD}@nexus3.dev.4m-a.org/repository/4m-pypi-releases/simple
--no-binary :4ma-vault-utils:
4ma-vault-utils==0.1.3.dev0