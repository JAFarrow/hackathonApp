# FlashMash
---
## Overview

FlashMash is a convenient replacement for physical flashcards. 
Users are able to input a question and answer and a card is added to their deck for review.

---
## Design Considerations.

Considering the scope of the assignment, I have chosen to go with lightweight tooling in order to keep a simple project.. simple.

HTML and pure CSS are responsible for the interface structure and visuals.
A few lines of JS were needed in order to activate a modal. 
Flask is used to serve up the page and with the help of jinja2, provide some degree of interactivity in the application.
Flasks' session storage and routing is used to store user entered data.

I dedicded against using a database to store user information as it felt unneccesary for an application that is meant for individual study sessions.

A neutral and bright colour scheme was chosen as it would be the least distracting for a study aid. 

In terms of my approach, I knocked togehter a skeleton of the site structure as quickly as possible and then fleshed out the interactivity.
Once the core user interation loop was working, I 'prettified' the site and added some finishing touches.

---
## Getting Started

1. Clone this repository
```shell
git clone git@github.com:JAFarrow/hackathonApp.git
```
2. Navigate to the main directory
```shell
cd hackathonApp
```
3. Install Requirements
```shell
pip install -r requirements.txt
```

4. Localhost App
```shell
flask run
```

5. A link will be generated in your terminal. Once clicked, the project should open in your browser.

---
## Tech stack

* HTML and CSS for site structure and visuals.
* Flask via Python in order to implement dynamic usability and session storage.

---
## Requirements

* Flask
* Flask-Session
* 
**INSTALLABLE VIA PIP**

```shell
pip install -r requirements.txt
```