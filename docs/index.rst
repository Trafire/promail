Promailer
=========

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference

**Promail** is a library for handling emails directly in python. With Promail you can:

------------------

    - Send plain text emails
    - Send fancy HTML emails
    - Integrate with it's sister library promail-template to send json driven dynamic html emails
    - filter emails in your inbox and run your own python functions based on them


**Simple example** ::
    >> import
    >>> client =

Installation
------------

Promailer can be pip installed:

.. code-block:: console

   $ pip install promailer

.. code-block:: python

    client = GmailClient("your-gmail@gmail.com")
    # The first time you do this it will open a web browser allowing you to sign into your google account directly
    client.send_email()

