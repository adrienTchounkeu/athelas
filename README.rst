AThelas Wrinkles Images
========================

|Python-Versions| |pip-Verion| |fastapi-Version| |nuxt-Version|

``athelas wrinkles images`` is an Image transformation API that helps us to remove wrinkles from pictures.

--------------------------------------

.. contents:: Table of contents
   :backlinks: top
   :local:
   
Technologies used and Why ?
---------------------------

To resolve this problem, we have used ``python``, ``fastapi`` , and ``NuxtJs``.

* ``python``: among the best programming language used for image processing.
* ``fastapi``: we are supposed to build a small REST API. Even though *Flask* is a great python web framework, *fastapi*, coming with great features, has been built for rapid development, provides API support, and has a lightweight codebase. Thereby, it best fits with the solution.
* ``NuxtJs``: VueJs framework to quickly set the Frontend API.


Installation
------------

To run my solution, you must have ``python``, ``pip``, ``node``, and ``npm`` installed in your system. 

Download the project from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To clone my code, you run the command below in the CLI

.. code:: sh

    git clone "https://github.com/adrienTchounkeu/athelas.git"

You can also download the project by clicking the link `athelas-wrinkles-images <https://github.com/adrienTchounkeu/athelas.git>`_


Install Dependencies
~~~~~~~~~~~~~~~~~~~~~

After downloading the code, Please follow the steps below to display the app:

Backend
--------
To use the backend, you should create a *.env file* under the **/backend** directory 
and set these two variables : 
*SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@127.0.0.1:5432/athelas'*
*SQLALCHEMY_TEST_DATABASE_URI='postgresql://postgres:postgres@127.0.0.1:5432/test_athelas'*
You should have PostgreSQL installed in your computer.

Under the **/backend** directory, execute the command :

.. code:: sh

   pip install -r requirements.txt


NB: *"requirements.txt is a file which contains all the project dependencies"*

All the project dependencies installed, run the command

.. code:: sh

   uvicorn app.main:app --reload --env-file <ENV_FILE_NAME>

NB: *FastAPI* runs under the port 8000 and comes with a great Swagger UI. In your browser, you can hit *localhost:8000/docs* 
and you should see a great UI.

<insert swagger image here>

Fronted
--------

Under the **/frontend** directory, execute the command :

.. code:: sh

   npm install


All the project dependencies installed, run the command

.. code:: sh

   npm run dev

NB: *Nuxt* runs under the port 3000. In your browser, you can hit *localhost:3000* 
and you should see a simple UI.

<insert frontend image here>

    
Solving ``athelas wrinkles images``
-----------------------------

Use Case
~~~~~~~~

Below are the results when using the app:

* After running the *backend* with the command ``uvicorn app.main:app --reload``, the server will be available under the port *8000*. Thereby, ``127.0.0.1:8000``
* After running the *frontend* with the command ``npm run dev``, the frontend will be available under the port *3000*. Thereby, ``127.0.0.1:3s000``
* When displaying the Frontend, this image is displayed  ![Screenshot_1](screenshots/index.png)
* When you click on the button, you can select a file : ![Screenshot_2](screenshots/image_selection.png)
* When the image is uploaded, you should see this response : ![Screenshot_3](screenshots/upload_result.png)
* You can check that the image has been saved in the **wrinkle_images** folder under the */backend* directory : ![Screenshot_4](screenshots/write_in_folder.png)

Tests
~~~~~

*No unit tests* have been done to test the endpoints. However, tests templates are performed under the tests directory


.. |Python-Versions| image:: https://img.shields.io/pypi/pyversions/pip?logo=python&logoColor=white   :alt: Python Version 
.. |pip-Verion| image:: https://img.shields.io/pypi/v/pip?label=pip&logoColor=white   :alt: pip  Version
.. |fastapi-Version| image:: https://img.shields.io/pypi/v/fastapi?label=fastapi   :alt: Fastapi
.. |nuxt-Version| image:: https://img.shields.io/npm/v/nuxt?label=nuxt&logo=nuxt   :alt: Nuxt
