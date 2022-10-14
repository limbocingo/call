# Fassy
Current version: `0.0.1v-beta`

### Instalation
clone: `git clone https://github.com/limbocingo/fassy/`\n
install: `pip install .`

### Examples

```python
import fassy

server = fassy.Fassy(__name__)

class Test(server.View):
  pass
 
if __name__ == '__main__:
  server.run()
```
