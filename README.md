# Towards AI Online course "" #
<p>
This repository contains the code developed while attending the online course:
<a href="https://academy.towardsai.net/courses/beginner-to-advanced-llm-dev" target="_blank">From Beginner to Advanced LLM Developer</a>.
</p>

Directory tree:
<ul>
<li><a href="src_lessons" target="_blank">src_lessons</a>: notebooks and Python script related to the lessons. </li>
<li><a href="src_py" target="_blank">src_py</a>: Python libraries used by multiple scripts and notebooks. </li>
</ul>

## Installation of the required packages

The requirement.txt for a given project is either in the root directory of the repository.<br>
The environment is, for example, in a directory called <code>env</code>. To create it:<br>

<code>
<pre>
    python3 -m venv ./venv

    source venv/bin/activate  # Activate the environment

    sudo apt-get install pipx         # Needed by poetry
    pipx install poetry               # Poetry
    pip  install -r requirements.txt  # Installs the packages listed in requirements.txt
</pre>
</code>


### Environment activation
Activate the environment with the command:

<code>
<pre>
  # cd to the root directory of the towards_ai_course repo
  export REPO_ROOT=$(pwd)
  export TAI_DATASET_ROOT=${REPO_ROOT}/dataset

  source venv/bin/activate

  # Loads the keys to the API(s).
  source ${REPO_ROOT}/api_keys/api_keys.sh

  export PYTHONPATH=${PYTHONPATH}:${REPO_ROOT}/src_py/lib

  # Langchain POC Notebooks
  cd ${REPO_ROOT}/src_lessons/part_01_2_chroma_vector_db
  cd ${REPO_ROOT}/src_notebooks/nb_langchain
  jupyter notebook
</pre>
</code>

<hr>

# Links
<ul>
  <li> <a target="_blank" href="https://github.com/towardsai/ai-tutor-rag-system">Towards AI gitHub: AI Tutor RAG system</a> </li>
  <li> <a target="_blank" href=""></a> </li>
</ul>
