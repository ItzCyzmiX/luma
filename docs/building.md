# Building your game

## Installing Pyinstaller

To build a Luma game you will need to have Pyinstaller installed. You can install it using pip:

```bash
pip install pyinstaller
```


## Simple Build
To build your game, navigate to the root directory of your project and run the following command:

```bash 
pyinstaller --onefile --windowed --collect-all luma main.py
```
With main.py being the main entry point for your game. This will create a single executable file in the `dist` directory, named `main.exe`  (or `main.app` on macOS) that you can distribute to others.

## Adding Additional Assets

If you have any additional assets (like images, sounds, etc.) that your game needs, you will need to include them in the build. You can do this by adding the `--add-data` option to the command. For example:

```bash
pyinstaller --onefile --windowed --collect-all luma --add-data "assets:assets" main.py
```
You can also specify additional options to customize the build process. For example, you can use the `--icon` option to specify an icon for your game:

```bash
pyinstaller --onefile --windowed --collect-all luma --add-data "assets:assets" --icon "icon.ico" main.py
```

## More Information

For more information on the available options, you can refer to the Pyinstaller documentation: https://pyinstaller.readthedocs.io/en/stable/ Just make sure to include the `--collect-all luma` option to ensure that all necessary Luma files are included in the build, and the `--windowed` option to prevent a console window from appearing when you run your game.