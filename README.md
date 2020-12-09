# python-xlogs
logging toolkit


# install
```commandline
pip install xlogs
```

# Usage
## 1. Use as decorator
```python
from xlogs import log

if __name__ == '__main__':
    # config_file: the logging config template, use the default if None
    @log(log_dir='./logs',config_file=None)
    def division():
        pass
```

## 2. Load from ini config file
```python
from xlogs import LogConfig
import logging

if __name__ == '__main__':
    LogConfig(config_file= '/xxx.ini', log_file = '/xxx/')

    logging.info('Default load to root')
    info = logging.getLogger('root')
    info.info('write msg to test.log')

    info = logging.getLogger('test')
    info.info('write msg to message.log')

    info = logging.getLogger('info')
    info.info('write msg to info.log')

    error = logging.getLogger('error')
    error.error('write msg to error.log')
    
    # reload a new config file 
    LogConfig(config_file= '/yyy.ini', log_file = '/yyy/').reset()
    logging.getLogger().info("info with new logger")
```

## 3. config with args
```python
from xlogs import get_logger

if __name__ == '__main__':
    logger = get_logger(debug=True, logfile='/message.log')
    logger.info("info oooooo")
    logger.debug("debug ggggg")
    logger.error("err rrrr")
```