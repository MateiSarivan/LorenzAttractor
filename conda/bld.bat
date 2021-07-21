"%PYTHON%" setup.py install --single-version-externally-managed --record record.txt

cd "%PREFIX%"
mkdir Menu
copy "%RECIPE_DIR%\menu-windows-manual.json" "%PREFIX%\Menu\lorat.json"

cd "%SRC_DIR%"
