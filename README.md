# Iszis Framework
Current version: `0.0.1v-beta`

### Instalation
clone: `git clone https://github.com/limbocingo/mango/`

install: `pip install .`

### Examples

```python
import iszis

application = iszis.Application(__name__)

class Test(iszis.View):
    path = '/test'
 
if __name__ == '__main__:
  application.start()
```
