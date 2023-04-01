# Simple classification machine learning app. 

## Functions. Start training - `POST /train`
The endpoint is only accepting `POST` requests.
When you hit the endpoint. The flask backend service will fetch the data from UCI iris data and run the classification training.

## Functions. Fit the data by parsing the query params - `GET /get-result`
The endpoint is only accepting `GET` requests.
Returns a class of iris for the params parsed. In case of success, it responds with a `200` HTTP code and the text representation of iris flower class.

### Example call

```python
In [1]: import requests

In [2]: result = requests.post("http://localhost:5000/train")

In [3]: result.status_code
Out[3]: 200

In [4]: result = requests.get("http://localhost:5000/get-result?sepal_length=1&sepal_width=2&petal_length=3&petal_width=4")

In [5]: result.status_code
Out[5]: 200

In [6]:result.text
Out[6]:'iris-setosa'
```