# 🤖 CrewAI Resume Evaluator

An AI-powered multi-agent system that evaluates resumes for AI/ML job fit and generates professional candidate response messages — built using **CrewAI**, **LangChain**, and **Gemini LLM**.

![Resume Evaluator UI](https://github.com/Balachandharsriram/CrewAI_Resume_Evaluator/blob/main/static/images/Screenshot%202025-07-20%20062022.png)
(https://github.com/Balachandharsriram/CrewAI_Resume_Evaluator/blob/main/static/images/Screenshot%202025-07-20%20061938.png)

---

## 🚀 Features

✅ Multi-agent CrewAI system  
✅ Resume evaluation using Gemini-1.5-flash  
✅ Automatically writes acceptance or rejection replies  
✅ Clean HTML frontend + FastAPI/Flask backend  
✅ Scalable, customizable, and developer-friendly  

---

## 🧠 Technologies Used

- 🧠 [CrewAI](https://github.com/joaomdmoura/crewai) – multi-agent workflow engine  
- 🔗 [LangChain](https://www.langchain.com/) – LLM chaining and context sharing  
- 🤖 Gemini 1.5 Flash – fast, powerful LLM from Google  
- ⚙️ FastAPI or Flask – for backend API  
- 🌐 HTML, JS – simple frontend UI  
- 🐳 Docker (optional) – for containerized deployment  

---

## 📦 Project Structure

```

CrewAI\_Resume\_Evaluator/
├── backend/               # FastAPI or Flask server
│   └── main.py
├── frontend/              # Simple HTML frontend
│   └── index.html
├── static/                # Images and static files
│   └── images/
│       └── resume\_evaluator.png
├── templates/             # Jinja2 templates (if Flask)
│   └── index.html
├── requirements.txt
└── README.md

````

---

## 🧪 Example Flow

1. Paste a resume into the frontend form.
2. CrewAI agent evaluates the resume.
3. Based on the result, it generates a:

   * ✅ Acceptance message — if suitable
   * ❌ Rejection message — if not suitable
4. Final message is shown to the user.

---

## 📌 To Do

* [ ] Add authentication
* [ ] Enable file upload for resumes
* [ ] Store submissions to database
* [ ] Deploy using Streamlit / Render / Vercel

---

## 🙌 Author

**Balachandharsriram M**
🎓 B.Tech AI & Data Science
🌐 [GitHub](https://github.com/balachandharsriram)

---

## ⭐ Show Your Support

If you like this project, don’t forget to:

🌟 Star the repo
🍴 Fork it
🐛 Report issues
💬 Share feedback

---

## 📄 License

This project is licensed under the MIT License.

![Resume Evaluator UI](https://github.com/Balachandharsriram/CrewAI_Resume_Evaluator/blob/main/static/images/Screenshot%202025-07-20%20062022.png)
(https://github.com/Balachandharsriram/CrewAI_Resume_Evaluator/blob/main/static/images/Screenshot%202025-07-20%20061938.png)


