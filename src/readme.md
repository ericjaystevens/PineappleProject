Simple Pineapple Project
========================

Development Install Instructions 
--------------------

This has not been tested.

```powershell
choco install python3

mkdir pineapple
cd pineapple
git clone https://github.com/ericjaystevens/PineappleProject.git

py -3 -m venv venc
$env:FLASK_APP='.\src\pineapple.py'
Flask run
```

Browse to http://127.0.0.1:5000/pineapple/2