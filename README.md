# PyAPI

A lightweight Python API client built using only the standard library.  
It uses `urllib` for HTTP requests and a custom `jsonify()` function powered by Python’s built-in JSON tools.

---

## 🚀 Features

- ✅ No external dependencies  
- 🌐 Built on `urllib`  
- 📦 Simple base URL client  
- 🔍 Query parameter support  
- 🧾 Automatic JSON parsing  
- ✨ Custom `jsonify()` for formatting output  

---

## 📦 Installation

First, clone the repository on GitHub by using this Linux command:


```bash
git clone github.com/PyAPI-Project/pyapi.git
```

Then you integrate this file into your project:

```
pyapi.py
```


No pip install required.

---

## 🛠 Usage

```python
from pyapi import BaseClient

client = BaseClient("https://jsonplaceholder.typicode.com")

data = client.fetch("posts", {"userId": 1})

print(client.jsonify(data))
```

Make your data in JSON and filter using other tools, will fix that in update.
