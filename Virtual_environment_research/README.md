This is my awersome research on virtual environments. The article is available at doi:10.1111/1000-7 
You can easily reproduce my results by running scripts locally.
Please cite me! <br>
from https://github.com/krglkvrmn/Virtual_environment_research

**Installation**:

0. General notes: <br>
the script pain.py works with python3.9 only <br>
the correct work of the script was checked on the Ubuntu 20.4 system and may not be applicable to other OSs.

1. Copy folder "Virtual enviroment research" into your local directory

for example you can use
``` 
git clone https://github.com/krglkvrmn/Virtual_environment_research
cd ./Virtual_environment_research
```

2. Using virtual environment is recommended

The script correct working is checked in virtualenv (v. 20.8.0)

*Install python 3.9 and venv:*
```
sudo apt-get update
sudo apt install python3.9 python3.9-venv
```

*Create and activate venv (ENV=name of virt. environment)*
```
python3.9 -m venv ENV
source ENV/bin/activate
```

3. Requirements installation

(file requirements.txt is already exists, so just run)
```
pip install -r requirements.txt
```

4. Run the pain.py
```
python pain.py
```

5. If you have "Illegal instruction (core dumped)" error (just like I am), you may comment strings with "scanpy" words or run pain\_for\_3-8.py with python 3.8
