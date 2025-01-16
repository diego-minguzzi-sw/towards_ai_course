# Towards AI Online course "" #


## Installation of the required packages

The requirement.txt for a given project is either in the root directory of the repository.<br>
The environment is, for example, in a directory called <code>env</code>. To create it:<br>

<code>
<pre>
    python3 -m venv ./venv
</pre>
</code>


### Environment activation
Activate the environment with the command:

<code>
<pre>
    cd to the root directory of the repo
    export REPO_ROOT=$(pwd)

    source venv/bin/activate
    
    # Loads the keys to the API(s).
    source ${REPO_ROOT}/api_keys/api_keys.sh

    export PYTHONPATH=${PYTHONPATH}:${HOME}/repo/video_processing/src_py/lib

    # Langchain POC Notebooks
    cd ${REPO_ROOT}/src_notebooks/nb_langchain
    jupyter notebook
</pre>
</code>


# Links
<ul>
  <li> <a target="_blank" href=""></a> </li>
  <li> <a target="_blank" href=""></a> </li>
</ul>
