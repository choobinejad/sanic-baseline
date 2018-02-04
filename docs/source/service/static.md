# Static Resources

### What?

Need some images? Static files? host your docs?  

Put those things in `service/static`, and in one of your endpoint/bluepint modules, reference it like this:

### Example

```python
from sanic import Blueprint  
  
root_blueprint = Blueprint('root', url_prefix='/', strict_slashes=False)
root_blueprint.static('favicon.ico', './static/favicon.ico')
```
