# Test Task

---

### Requirements

1. Git
2. Python >= 3.8
3. Pipenv = *

> [!TIP]
> You can also see all requirements in the Pipfile.

### Installation Windows (Not tested on other OS systems)
* Create working directory for the project
* Clone repository to the working directory
* Install pipenv
  ```
  pip install --user pipenv
  ```

  > [!IMPORTANT]
  > Make sure that %USERPROFILE%\AppData\Roaming\Python\Python3X\Scripts\ in the path environment variable.
  > If not, add manually. Check pipenv correctly installed by ```pipenv -h```
    
* Go to the cloned repo in the working directory
* Install project dependencies
  ```
    pipenv sync --dev
  ```
  > [!TIP]
  > Or you can use ```pipenv install``` to re-lock your dependencies


> [!IMPORTANT]
> Make sure that the virtual environment is activated and choose like general interpreter.
> You can the status of your virtual env by ```pipenv --venv```

### Run tests

```
pipenv run pytest tests -v
```

---

### Additional Information about the structure of the project

_This example of the RestAPI test project for general validation of the API.
For the test task, I used the https://github.com/thundercomb/poetrydb#readme API.
This is a simple flat structure based on the separate functions
Instead of the class-based structure, as I used in the WAP project._

_This is a good solution for the fast and simple test automation with the basic functionality.
The error handling and traceback minimized. It can be improved in the future._

The tests make 4 general validation of the API:
* code (Could use for positive and negative test cases)
* json data (Actual data - related to the request)
* response time (Should be less than 1 second)
* response schema (Should be valid according to the schema)

>Some of the test failing due to the API response.
>The reason:
>```
>ProtocolError("Response ended prematurely") from None
>requests.exceptions.ChunkedEncodingError: Response ended prematurely
>```
>Looks like the error related to the existing issues in the API.

Test cases: 

| Test Case ID | Test Description                                                                       | Endpoint/Parameters                                                                                                                                                                 | Expected Result Type                                                   |
|--------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| test_01      | Validate the basic response for a valid query.                                         | * author<br/> * title                                                                                                                                                               | * 200 OK<br/> * JSON contains list (authors, titles) of valid results  |
| test_02      | Verify the response for a valid query. <br/>Mixing title and author in the same query. | * {"title": "Ozymandias"}<br/> * {"author": "Matthew Prior"}<br/> * {"title": "Mother"}<br/> * {"author": "Julia Ward Howe", "title": "Mother"}<br/> * {"author": "Jonathan Swift"} | * 200 OK<br/> * Responcse contains  filtered list of results           |
| test_03      | Validate the response for an unknown author.                                           | author/UnknownAuthor                                                                                                                                                                | * 200 OK<br/> * reason: "Not found"<br/> * status: 404,                |
| test_04      | Validate the response schema.                                                          | random                                                                                                                                                                              | * 200 OK<br/> * JSON contains valid results<br/> * schema is correct   |

