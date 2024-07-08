# GTR Internship Task

This project is specifically for the GTR Internship task. The project is a simple python bot using autogen that allows user to ask questions about Bangladesh and get answers from wikipedia.

## Run the project locally

1. Clone the repository

```bash
git clone https://github.com/fardeenes7/gtr-internship-task.git
```

2. Change the directory

```bash
cd gtr-internship-task
```

3. Copy the `.env.example` file to `.env` and update the values for either the `OPENAPI_API_KEY` or `GROQ_API_KEY` depending on the API you want to use.

```bash
cp .env.example .env
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python3 main.py
```
