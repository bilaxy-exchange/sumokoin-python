Python Sumokoin module
====================

A comprehensive Python module for handling Sumokoin cryptocurrency.

* release 0.6.1
* open source: https://github.com/sumoprojects/sumokoin-python
* works with Sumokoin 0.6.x and `the latest source`_ (at least we try to keep up)
* Python 2.x and 3.x compatible

.. _`the latest source`: https://github.com/sumoprojects/sumokoin

Copyrights
----------

Released under the BSD 3-Clause License. See `LICENSE.txt`_.

Copyright (c) 2019 Sumokoin Project

Copyright (c) 2017-2018 Michał Sałaban <michal@salaban.info> and Contributors: `lalanza808`_, `cryptochangements34`_, `atward`_, `rooterkyberian`_, `brucexiu`_,
`lialsoftlab`_, `moneroexamples`_.

Copyright (c) 2016 The MoneroPy Developers (``sumokoin/base58.py`` and ``sumokoin/ed25519.py`` taken from `MoneroPy`_)

Copyright (c) 2011 thomasv@gitorious (``sumokoin/seed.py`` based on `Electrum`_)

.. _`LICENSE.txt`: LICENSE.txt
.. _`MoneroPy`: https://github.com/bigreddmachine/MoneroPy
.. _`Electrum`: https://github.com/spesmilo/electrum

.. _`lalanza808`: https://github.com/lalanza808
.. _`cryptochangements34`: https://github.com/cryptochangements34
.. _`atward`: https://github.com/atward
.. _`rooterkyberian`: https://github.com/rooterkyberian
.. _`brucexiu`: https://github.com/brucexiu
.. _`lialsoftlab`: https://github.com/lialsoftlab
.. _`moneroexamples`: https://github.com/moneroexamples

Want to help?
-------------

If you find this project useful, please consider a donation to the following address:
``Sumoo64zh7dRFyB8dgDWZMLmzKBgGXYWZCG4NBF2VcvzEuiSQpMjyyiYJ1Ra696pZu56PPFQNBDdB1rZjyeX1RVKeWZgHg7pTxj``


Development
-----------

1. Clone the repo
2. Create virtualenv & activate it

.. code-block:: bash

    python3 -m venv .venv
    source .venv/bin/activate

3. Install dependencies

.. code-block:: bash

    pip install -r requirements.txt -r test_requirements.txt

4. Do your thing

5. Run tests

.. code-block:: bash

    pytest
