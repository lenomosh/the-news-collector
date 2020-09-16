## THE NEWS COLLECTOR 
#### [Lennox Omondi](https://linkedin.com/in/lenomosh)



## Description 
A news website that searches for trending, important and relevant news to a user based on an individual user's need.

## User Stories
As user I would like to:
* As a user, I would like to see various news sources on the homepage of the application.
* As a user, I would also want to select a news source and see all news articles from the selected news source in the application.
* As a user, I would want to see the image, description and the time a news article was created.
* As a user, I would want to click on an article and read the full article on the source website.


## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|To display various news sources| Click the View Article button|Redirected to a page with a list of articles from the source |
|Display the articles for the news source selected| Click Read More link| Redirected to the news source's site to read the entire article|

## Setup Instructions
* clone the repo
* From the project directory run `conda create --prefix=./env` or `python -m venv virtual`
* Run `source activate ./env` for conda or `source virtual/bin/activate`
* Run `pip install -r requirements.txt`
* Finally run `python app.py`

## LICENSE
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

Copyright (c) 2020 Lennox Omondi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
