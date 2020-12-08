# python-xlogs
logging toolkit


# install
```commandline
pip install xlogs
```

# Usage
## Use as decorator
```python
from xlogs import log

if __name__ == '__main__':
    # config_file: the logging config template, use the default if None
    @log(log_file='./logs',config_file=None)
    def division():
        pass
```

## load ini config file
```python
from xlogs import Log
import logging

if __name__ == '__main__':
    Log(config_file= '/xxx.ini', log_file = '/xxx/')

    logging.info('Default load to root')
    info = logging.getLogger('root')
    info.info('write msg to test.log')

    info = logging.getLogger('test')
    info.info('write msg to test.log')

    info = logging.getLogger('info')
    info.info('write msg to info.log')

    error = logging.getLogger('error')
    error.error('write msg to error.log')
    
    # reload a new config file 
    Log(config_file= '/yyy.ini', log_file = '/yyy/').log_reset()
    logging.getLogger().info("info with new logger")
```