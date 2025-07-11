# LangChain Document Loader Playground

A bite‑sized collection of Python scripts that show **exactly** how to load—and do something useful with—different document types using LangChain’s community loaders and open‑source LLMs from Hugging Face.

---

## 📚 What You’ll Learn

1. How to plug `TextLoader`, `WebBaseLoader`, `PyPDFLoader`, `DirectoryLoader`, and `CSVLoader` into the new LangChain **Runnable** pattern.
2. How to chain those documents through a prompt ➜ model ➜ output parser.
3. Real, runnable examples you can copy‑paste into your own projects.

---

## 🗂️ Repo Layout

```text
.
├── loaders/              # one loader = one script
│   ├── text_loader.py
│   ├── webbase_loader.py
│   ├── pdf_loader.py
│   ├── directory_loader.py
│   └── csv_loader.py
├── use_cases/            # higher‑level educational templates
│   ├── class_quiz.py
│   ├── class_summary.py
│   └── mentor.py
├── data/                 # sample assets you can play with
│   ├── story.txt
│   ├── classnotes.txt
│   ├── CSV_file.csv
│   ├── 2D Array Class summary – Audio.pdf
│   ├── 2D Array Mock test.pdf
│   ├── 2D Array Practice Questions Theory‑Coding Po….pdf
│   └── pdf_folder/        # drop any extra PDFs here
├── .env.example          # Hugging Face token goes here
├── requirements.txt
└── README.md             # you are here
```

---

## 🚀 Quick‑Start

```bash
# 1️⃣  clone & set up a venv
$ git clone https://github.com/<your‑handle>/<repo>.git
$ cd <repo>
$ python -m venv .venv && source .venv/bin/activate

# 2️⃣  install deps
$ pip install -r requirements.txt

# 3️⃣  drop your HF token in .env
HUGGINGFACEHUB_API_TOKEN=hf_********************************

# 4️⃣  run any example
$ python loaders/text_loader.py
```

Each script prints: *document count → first 500 chars → model answer/summary*.

---

## 🔍 Loader Walk‑Through

### 1. `text_loader.py`  — **TextLoader**

```python
loader = TextLoader("story.txt", encoding="utf-8")
docs   = loader.load()
```

* Reads a plain‑text file line‑by‑line → single `Document`.
* Prompt asks: “Summarise the following {story}”.
* Sends to `google/gemma-2-2b-it` via `HuggingFaceEndpoint`, returns a short recap.

---

### 2. `webbase_loader.py`  — **WebBaseLoader**

```python
url    = "https://blog.google/..."
loader = WebBaseLoader(url)
docs   = loader.load()
```

* Pulls raw HTML, strips tags with BeautifulSoup, outputs clean text.
* Two‑input prompt: **question** + **text** → get targeted answers (“What is the summary of this blog?”).
* Works with a list of URLs as well—just pass an array.

---

### 3. `pdf_loader.py`  — **PyPDFLoader**

```python
loader = PyPDFLoader("Pdf_paper.pdf")
docs   = loader.load()
```

* Splits each PDF **page** into its own `Document`; perfect for research papers.
* One‑shot prompt: “Summarise the following {ResearchPaper}”.
* Swap in `chunk_size`/`chunk_overlap` if you hit context limits.

---

### 4. `directory_loader.py`  — **DirectoryLoader + PyPDFLoader**

```python
loader = DirectoryLoader(path="pdf_folder", glob="*.pdf", loader_cls=PyPDFLoader)
docs   = loader.load()
```

* Recursively grabs every `*.pdf` in a folder and applies **PyPDFLoader** to each.
* Current script simply prints the metadata (title, page number, source file) so you can see what’s inside before further processing.
* Swap the print loop for your own chain once you’re comfortable.

---

### 5. `csv_loader.py`  — **CSVLoader**

```python
loader = CSVLoader(file_path="CSV_file.csv")
docs   = loader.load()
```

* Treats **each row** as an independent `Document` (column headers become metadata).
* Re‑uses the same summary prompt as the PDF example—great for literature‑review tables.

---

## 🎓 Educational Templates (`use_cases/`)

| File               | What It Generates                                                    |
| ------------------ | -------------------------------------------------------------------- |
| `class_quiz.py`    | Full lesson summary **plus** 5 MCQ quiz questions                    |
| `class_summary.py` | Same as above but without the quiz                                   |
| `mentor.py`        | Class overview, key concepts, code walkthrough, and 5‑slide PPT text |

Each follows the exact same pipeline: **PromptTemplate ➜ HuggingFaceEndpoint ➜ (optional) StrOutputParser**.

---

## 🛠️ Requirements

* Python ≥ 3.9
* Key libs: `langchain-community`, `langchain-core`, `langchain-huggingface`, `huggingface_hub`, `python-dotenv`, `beautifulsoup4`

---

## 🤔 FAQ

**Q. Can I use a different model?**  Yes—swap `repo_id` in any script. Smaller checkpoints = cheaper, faster.

**Q. How do I handle large PDFs or websites?**  See LangChain’s `RecursiveCharacterTextSplitter` and stick it between the loader and the model.

**Q. Rate limits?**  The free HF tier gives \~30 requests/min. Upgrade or run the model locally if you need more.

---

## 📄 License

MIT — use it, fork it, star it. ✨

---

*Last updated: July 11 2025*
