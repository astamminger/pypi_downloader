# PyPi Downloader Utility                                                          
                                                          
                                                                                 
PyPi Downloader is a small utility provided to download multiple packages from   
the [PyPi Index](https://pypi.org/) index fulfilling the specified requirements (i.e. a package        
version and package type). It's main purpose (or how I use it) is to download    
multiple version of a single package which may then be added to package          
cache used as input for an internal PyPi server. This is useful if you           
work on a cluster without internet access to easily setup internal package       
ressources.                                                                      
                                                                                 
## Getting Started                                                                                                                                    
                                                                                 
The following instructions will tell you how to install the downloader and       
gives a short example on how to use the utility.                                 
                                                                                 
### Installing                                                                                                                                              
                                                                                 
After cloning the repository to your local disc switch to the top folder         
of the project containing the `setup.py` file and execute                                                                      
                                                                                 
```console                                                    
  $ python setup.py install    
```
                                                                                 
which will install the PyPi Downloader to your currently loaded python           
environment. If the installation went okay the provided `sync_package_cache` 
command should now be available from the command line:

```console
  $ sync_package_cache --help 
  usage: sync_package_cache [-h] configfile

  Reads the provided config file and builds the package cache according to the
  defined settings.

  positional arguments:
    configfile  Path to a valid config file.

  optional arguments:
    -h, --help  show this help message and exit
```
 
 ### Downloading Packages from PyPi
 
 To download packages from PyPi using this utility setup a configuration
 file containing a general settings section `[settings]` defining the type
 of packages to look for and the location to which the downloaded packages will 
 be stored (Note that each package will be stored to a subfolder corresponding
 to the package name located inside the folder specified by the `cache_folder`
 variable). The packages you are interest in are specified under the `[packages]` 
 section, accepting a list of packages (and a version / version range). An example
 configuration file is shown below.
 
 ```console
   $ cat sample_config
   [settings]                                                                       
     cache_folder: ./cache                                                         
     packagetypes: bdist_wheel,sdist                                               
                                                                                 
   [packages]                                                                       
     requests>=2.19.0                                                               
     pip>=9.0.0,<10.0.0
```

To download the specified packages to the `~/cache` folder call the implemented
`sync_package_cache` command with the setup configuration file as argument:

```console
  $ sync_package_cache sample_config
  requests-2.19.1.tar.gz      [####################################################################]  100%
  pip-9.0.3.tar.gz            [####################################################################]  100%
```

After the script has finished successful, all files matching the defined specifications
have been stored to the set `cache_folder`:

```console
  $ ls cache/requests
  requests-2.19.0-py2.py3-none-any.whl  requests-2.19.0.tar.gz  
  requests-2.19.1-py2.py3-none-any.whl  requests-2.19.1.tar.gz
  $ ls cache/pip
  pip-9.0.0-py2.py3-none-any.whl  pip-9.0.0.tar.gz  pip-9.0.1-py2.py3-none-any.whl  
  pip-9.0.1.tar.gz  pip-9.0.2-py2.py3-none-any.whl  pip-9.0.2.tar.gz  pip-9.0.3-py2.py3-none-any.whl  
  pip-9.0.3.tar.gz
```
