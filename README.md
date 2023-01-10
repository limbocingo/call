# Iszis Framework
Current version: `0.0.1v-beta`

### Instalation
clone: `git clone https://github.com/limbocingo/call.git'

requirements: `pip install -r requirements.txt`
install: `pip install .`

### Examples

```python
import iszis

application = iszis.Application(__name__)

class Test(iszis.View):
    def __init__(self, request) -> None:
        super().__init__(request, '/test')
 
if __name__ == '__main__':
  application.start()
```
