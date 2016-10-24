DocsBR
======

Esse projeto visa criar uma API para verificação de alguns documentos
rotineiros dentre os documentos oficiais do Brasil.

--------------

Quick links
-----------

-  `Features <#features>`__
-  `Requirements <#requirements>`__
-  `Project Setup <#project-setup>`__
-  `Usage <#usage>`__
-  `Optional Arguments <#optional-arguments>`__
-  `Contribute <#to-contribute>`__
-  `Project Structure <#project-structure>`__
-  `License <#license>`__

--------------

Features
--------

`↑ <#quick-links>`__

--------------

Requirements
------------

-  `python <https://www.python.org/download/releases/3.0/>`__ >= 3.2
-  *(optional)* `pip <https://pypi.python.org/pypi/pip/>`__
-  *(optional)* `venv <https://docs.python.org/3/library/venv.html>`__

`↑ <#quick-links>`__

--------------

Project Setup
-------------

-  **Clone** the project
-  Move into the **project dir**
-  *(Optional)* Create a new **virtual environment**
-  *(Optional)* Install project's **requirements**
-  *(Optional)* View **documentation**
-  *(Optional)* Run the **tests**
-  *(Optional)* **Install** project's packages
-  **Run** the project

**Step 1**: Clone the project:

::

    git clone https://github.com/nullhack/DocsBR.git

**Step 2**: Move into project's path:

::

    cd DocsBR

**Step 3**: *(Optional, but good practice)* Create a new virtual
environment (ENV):

::

    python3 -m venv ENV
    source ENV/bin/activate

If you want to deactivate the virtual environment:

::

    deactivate

If you are new to virtual environments, please see the
``Virtual Environment section`` of Kenneth Reitz's `Hitchhiker's Guide
to Python <http://docs.python-guide.org/en/latest/>`__.

**Step 4**: *(Optional)* Install project's requirements:

::

    pip3 install -r requirements.txt

**Step 5**: *(Optional)* View documentation:

::

    firefox docs/build/html/index.html

**Step 6**: *(Optional)* Run the tests:

::

    python3 -m doctest -v ./tests/*

**Step 7**: *(Optional)* Install project's packages:

::

    python3 setup.py install

**Step 11**: Run the project:

::

    python3 main.py

`↑ <#quick-links>`__

--------------

Usage:
------

::

    main.py [-h] [-V]

Optional arguments:
~~~~~~~~~~~~~~~~~~~

::

    -h, --help     show this help message and exit
    -V, --version  show program's version number and exit

`↑ <#quick-links>`__

--------------

To contribute
-------------

The general workflow that GitHub supports is:

-  **Fork** this repo to your own account.
-  **Clone** the repo to your machine.
-  Check out a new **"topic branch"** and make changes.
-  **Push** your topic branch to your fork.
-  Use the diff viewer on GitHub to create a **pull request** via a
   discussion.
-  Make any requested **changes**.
-  The pull request is then **merged** and the "topic branch" is deleted
   from the upstream (target) repo.

The naming conventions for topic branches are: issue\_ID, where the ID
is the ID # of a GitHub issue.

Use the official guides:

-  https://help.github.com/articles/fork-a-repo/
-  https://guides.github.com/activities/forking/

Or the reference
`tutorial <https://code.tutsplus.com/tutorials/how-to-collaborate-on-github--net-34267>`__
for this documentation.

Some commands that would complete the workflow above:

**Step 1**: Forking

In the top-right corner of the page, click **Fork Button**

**Step 2**: Cloning

Clone the repo using your own github login (YOUR\_USERNAME):

::

    git clone git@github.com:YOUR_USERNAME/DocsBR.git

**Step 3**: Adding the Upstream Remote

Change into the directory and then you can add the upstream remote:

::

    cd DocsBR
    git remote add upstream git@github.com:nullhack/DocsBR.git

To pull in changes from the source locally and merge them:

::

    git fetch upstream
    git merge upstream/master

**Step 4**: Checking Out a Topic Branch

Checkout a topic branch using the issue ID:

::

    git checkout -b issue_ID

**Step 5**: Committing

**Make your changes** and create a commit that tracks those changes.

::

    git commit -am "adding some specific change."

**Step 6**: Pushing

Push this topic branch to your own fork of the project.

::

    git push origin issue_ID

**Step 7**: Creating a Pull Request

Now you may create a pull request:

-  Go to your fork of the repo
-  Click on issue\_ID at "your recently pushed branches"
-  Choose "Compare and Pull Request"

Or:

-  Select your branch from the dropdown
-  click "Pull Request" or "Compare"

`↑ <#quick-links>`__

--------------

Project Structure
-----------------

::

    DocsBR
    ├── docs
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    │       ├── conf.py
    │       └── index.rst
    ├── LICENSE
    ├── main.py
    ├── MANIFEST.in
    ├── br_docs
    │   ├── __init__.py
    │   └── metadata.py
    ├── README.md
    ├── requirements-dev.txt
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    └── tests
        └── test_metadata.txt

`↑ <#quick-links>`__

--------------

License
-------

DocsBR is released under MIT license.

Copyright (c) 2016 Eric Lopes

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Original license text can be found at the `LICENSE <LICENSE>`__ file.

`↑ <#quick-links>`__

--------------

