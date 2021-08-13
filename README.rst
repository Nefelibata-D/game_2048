================
Game 2048
================


|pyversions| |license| |pypi| |status| |github|


Fun and challenging puzzle game -- 2048 !

Install immediately and enjoy yourself !

Screenshot 
---------------
|game-2048.png|

Installation
---------------

1. Installing Game 2048 is simple with pip：

   .. code:: bash

      $ python3 -m pip install pygame-2048


2. Once installed the game can be played using the following command

   .. code:: bash

      $ game_2048


3. If you want to uninstall the game using the following command

   .. code:: bash

      $ python3 -m pip uninstall pygame-2048

   
Development 
---------------
1. After cloning the repository, install the game in development mode using the following command 
   
   .. code:: bash

      $ python3 setup.py develop


2. You can modify the program and then test it by using the following command 

   .. code:: bash

      $ game_2048


Tips
-------

-  You can use ⬅️⬆️➡️⬇️ keys or 'AWSD' keys to remove the blocks on the
   screen

-  Screenshot will be saved to ' ~/Desktop/game-2048/screenshots '

- You can't make 4096 block when you have two 2048 blocks.
  So what you should do next is reset this game and start a new challenge.

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/pygame-2048.svg
.. |license| image:: https://img.shields.io/pypi/l/pygame-2048.svg
.. |pypi| image:: https://img.shields.io/pypi/v/pygame-2048.svg
.. |status| image:: https://img.shields.io/pypi/status/pygame-2048.svg
.. |github| image:: https://img.shields.io/github/watchers/dzc217/game_2048?style=social
.. |game-2048.png| image:: https://www.z4a.net/images/2021/08/12/game.png
