from hello import app
import os
with app.test_client() as c:
    response = c.get('/')
    env = os.getenv('env')
    if env in ('prd', 'stg', 'dev'):
        msg = f"Hello World from! {os.getenv('env')}"
    else:
        msg = 'none'
    assert response.data == str.encode(msg)
    assert response.status_code == 200