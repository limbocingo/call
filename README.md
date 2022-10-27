# Fassy
Current version: `0.0.1v-beta`

### Instalation
clone: `git clone https://github.com/limbocingo/fassy/`

install: `pip install .`

### Examples

```python
import fassy

application = fassy.Fassy(__name__)

class Test(fassy.View):
  pass
 
if __name__ == '__main__:
  application.start()
```
