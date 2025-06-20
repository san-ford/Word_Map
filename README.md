# Word_Map
The word map is a collection of the most common English words organized by their semantic similarity. The map is organized in a 2-dimensional field of 100 nodes by an unsupersived machine learning algorithm known as the self-organizing map (SOM).

I have created a web application to explore the word map interactively. The app randomly retrieves 5 words semantically similar to a word submitted by the user. It then gives the user the option to submit another word or choose one of the retrieved words to repeat the process.

### Create Virtual Environment
To run the app, clone this repository and navigate to the 'Word_Map' directory. To create a virtual environment for the app using conda, run the following commands
```bash
conda create -n word_map_env
conda activate word_map_env
```

### Make Database
To create and populate the database, navigate to the 'deployment' directory and run the following commands
```bash
Python3 manage.py migrate
python3 manage.py sqlmigrate word_retrieval 0001
python3 populate.py
```

### Run App
```bash
Python3 manage.py runserver
```

Once the app is running, use a browser to navigate to:

[http://localhost:8000/word_retrieval/](http://localhost:8000/word_retrieval/)


To visualize the map, I have taken a sample of 10 words closest to each of the 100 nodes and plotted them. I have made a plot for each of the nodes, color coded to distinguish between different nodes. Note that some nodes are empty, so no words are plotted in that space.

![image](https://github.com/user-attachments/assets/4fc2dadf-0648-4187-a31b-71bb3df6066f)
