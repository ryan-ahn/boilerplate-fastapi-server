# Ryan's FastAPI Starter


![Author](https://img.shields.io/badge/Author-ryan-orange.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Last Commit](https://img.shields.io/github/last-commit/ryan-ahn/npm-fastapi-starter)


## Setting Stack
- Language : Python
- Framework : FastAPI
- Database : MySql, MongoDB
- ORM, ODM : Prisma, Mongoose


## Project Start
1. Installation
```
$ git clone https://github.com/ryan-ahn/boilerplate-fastapi-starter.git
$ cd boilerplate-fastapi-starter
```
2. Run Project
```
$ uvicorn application:app --reload
```


## Code Structure
&nbsp;⎣&nbsp;**core** - configuration<br/>
&nbsp;⎣&nbsp;**controllers** - error handling, business logic controls<br/>
&nbsp;⎣&nbsp;**constants** - static resource<br/>
&nbsp;⎣&nbsp;**dependency** - dependencies<br/>
&nbsp;⎣&nbsp;**database** - schema, query<br/>
&nbsp;⎣&nbsp;**routes** - routes<br/>
&nbsp;⎣&nbsp;**services** - service logic controls<br/>
&nbsp;⎣&nbsp;**utils** - connector, handler, helper<br/>
