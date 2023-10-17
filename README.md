# Call Framework
Current version: `0.0.1v-beta`
You can use this code with total freedom.

### Instalation
Clone: `git clone https://github.com/limbocingo/call.git`

Go to the folder: `cd call/`

Install: `pip install .`

### Example

```python
import call

application = call.Application(__name__)

class Test(call.View):
    def __init__(self, request) -> None:
        super().__init__(request, '/test')

    def get(self) -> dict: return {'message': 'default-message'}

    def create(self) -> dict: return {'message': 'default-message'}

    def update(self) -> dict: return {'message': 'default-message'}

    def delete(self) -> dict: return {'message': 'default-message'}
 
if __name__ == '__main__':
  application.start()
```
