# app.py
from flask import Flask, request, jsonify, render_template
from crewai import Agent, Task, Crew
from langchain_community.chat_models import ChatLiteLLM
import os

# Initialize Flask app
app = Flask(__name__)

# Set your Google API Key (ensure this is handled securely in a real app, e.g., environment variables)
# In a real application, you'd load this from an environment variable:
# os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = "your_api_key"

# Initialize LLM
llm = ChatLiteLLM(
    model="gemini/gemini-1.5-flash",
    temperature=0,
    api_key=os.environ["GOOGLE_API_KEY"]
)

# Define Agents (these can be global or initialized within the function if needed)
evaluator = Agent(
    role="Resume Evaluator",
    goal="Evaluate resumes for AI/ML job fit",
    backstory="Expert in talent assessment and AI hiring standards.",
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Reply Writer",
    goal="write clear replies to candidates",
    backstory="An HR pro who crafts polite offer/reject messages.",
    llm=llm,
    verbose=True
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate_resume', methods=['POST'])
def evaluate_resume():
    data = request.json
    resume_text = data.get('resume_text', '')

    if not resume_text:
        return jsonify({"error": "Resume text is empty"}), 400

    # Define Tasks with the dynamic resume_text
    evaluator_task = Task(
        description=f"""Check if the following resume is fit for the AI/ML engineer role.
        respond with YES or NO and a short reason :\n\n{resume_text}""",
        agent=evaluator,
        expected_output="YES or NO with short reason"
    )

    reply_task = Task(
        description="""Using the evaluation result, write:
        - An acceptance message if YES
        - A polite rejection message if NO
        """,
        agent=writer,
        context=[evaluator_task],
        expected_output="A professional message to the candidate"
    )

    # Run the Crew
    crew = Crew(
        agents=[evaluator, writer],
        tasks=[evaluator_task, reply_task],
        verbose=False # Set to False for production to avoid excessive console output
    )

    try:
        result = crew.kickoff()
        # --- IMPORTANT CHANGE HERE ---
        # Convert the CrewOutput object to its raw string representation
        return jsonify({"message": result.raw})
        # Alternatively, if you need a dictionary, use:
        # return jsonify({"message": result.to_dict()})
        # Or for a JSON string if you configured JSON output:
        # return jsonify({"message": result.json})
        # --- END IMPORTANT CHANGE ---
    except Exception as e:
        # It's good practice to log the full traceback for debugging
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) # debug=True for development, set to False in production
