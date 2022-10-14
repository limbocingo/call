# Fassy
Be easy to understand, productive and faster.

## Version
Current version: `0.0.1v-beta`

## Examples

```python
import fassy

server = fassy.Fassy(__name__)

class Test(server.View):
  pass
 
if __name__ == '__main__:
  server.run()
```
