django-autotextmail
===================

- Tired of having to have to write templates for both text and html version ?
- Want to have compatibility with old mail clients at no cost ?

**Autotextmail is for you !**

``AutoTextMail`` is a simple email class that automatically creates a text version of a html email.
Just write an html format and let ``autotextmail`` do the rest.

Installation
------------
just add ``'autotextmail'`` to your ``INSTALLED_APPS``

Usage
-----
``AutoTextMail`` is a subclass of ``EmailMultiAlternatives``, hence the constructor accept all the options related to classic ``EmailMultiAlternatives``, plus the following perks:

- ``subject`` is automatically linebreak free
- ``body`` should be an html template

and that's it ! the ``text/plain`` and ``text/html`` are directly set and you're good to go!

To Do
-----
This is currently more of a proof of concept

- This currently uses html2text to do the html to do the conversion, write own code
- Personalisation of the rendering (custom html2text ?)
