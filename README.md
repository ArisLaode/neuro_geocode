Usage example
---
Yandex Geocoder requires an API developer key, you can get it [here](https://developer.tech.yandex.com/services/) to use this library.

* create environment
```bash
pip install virtualenv
```
```bash
virtualenv -p python3 env
```

* install all package needed
```bash
pip install -r requirements.txt
```

* run tests
```bash
pytest
```

* run linters
```bash
flake8 api/api.py app.py tests/
```

* run project
```bash
flask run
```

* Test API address use postman :
  *  Method : POST
  *  Add url : http://127.0.0.1:5000/v1/address
  *  Select tab "Body" -> "form-data"
  *  insert two key:
     *  decimal_one = 36.440429
     *  decimal_two = 55.964957
  *  Click "Send"

* Test API coordinates use postman :
  *  Method : POST
  *  Add url : http://127.0.0.1:5000/v1/coordinates
  *  Select tab "Body" -> "form-data"
  *  insert key:
     *  coordinates = Россия, Московская область, городской округ Истра, А-108, Минско-Волоколамский перегон, 58-й километр
  *  Click "Send"

Running via Docker
---

*   Build Image
```bash
docker image build -t docker-neuro .
```
*  Running Container
```bash
docker run -p 5000:5000 docker-neuro
```
*  Test your api project