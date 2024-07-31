Usage
=====

.. _installation:

Installation
------------

This application requires numpy, scipy, lmfit to
perform all the Math.

Running
-------

Open the Jupyter notebook:

.. code-block:: console

   run_cmdline.ipynb

Alternatively, instantiate an object of the class
``rpn_class()``.

.. code-block:: console

   my_rpn = rpn_class()

.. autofunction:: rpn_class.evaluate_list

The ``expression`` parameter should be a string
containing a rpn (reverse Polish notation) expression.
Otherwise, :py:func:`rpn_class.evaluate_list`
will raise an exception.

.. autoexception:: rpn_class.InvalidKindError

For example:

.. autofunction:: rpn_class.evaluate_list

>>> import rpn_class
>>> rpn_class.evaluate_list("44+4*")
