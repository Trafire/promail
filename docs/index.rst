Promailer
=========

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference

**Promail** is a library for extending the functionality of your email box with your own python code.

------------------

    - Send plain text emails
    - Send fancy HTML emails
    - Integrate with it's sister library promail-template to send json driven dynamic html emails
    - filter emails in your inbox and run your own python functions based on them


**Simple example**

Promail's :py:class:`promail.clients.GmailClient`  uses Oauth rather than a password to access your email.
You'll be taken to googles Oauth login page which will allow you to log in.

.. code-block::

    >>> from promail.clients import GmailClient
    >>> client = GmailClient("my_email@gmail.com")
    >>> client.send_email(
            recipients="your_email@gmail.com",
            cc="someelse@gmail.com",
            subject="My First Promail Email",
            htmltext="<h1>Hello World<h1>"
        )


Installation
------------

Promailer can be pip installed:

.. code-block:: console

   $ pip install promailer


