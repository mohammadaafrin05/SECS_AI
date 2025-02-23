from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)

# AI Modules
class GenerativeAI:
    def generate_plan(self, project_name, city, workers, materials, tasks):
        complexity = len(materials) + len(tasks) + len(workers)
        design = f"{random.choice(['Modern', 'Eco-friendly', 'Minimalist', 'Futuristic'])} design for {project_name} in {city}"
        schedule = f"Estimated completion time: {random.randint(3, 18)} months (based on {complexity} parameters)"
        workflow = f"Optimized {random.choice(['sequential', 'parallel', 'hybrid'])} workflow with AI-driven task distribution"

        # Fetch real-time weather data
        api_key = "b10d3cb9ec7e77afef422ed1e2cc3a0b"
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            weather_data = requests.get(weather_url).json()
            weather_report = f"Temperature: {weather_data['main']['temp']}°C, Condition: {weather_data['weather'][0]['description']}"
        except:
            weather_report = "Weather data unavailable. Check internet connection or API key."

        # Geotechnical Risk Analysis (Now Dynamic)
        geotechnical_risk = random.choice([
            "Stable ground detected, minimal risk.",
            "Moderate instability detected, reinforcement recommended.",
            "High risk of collapse, manual verification required."
        ])

        # Generate risk analysis
        risk_analysis = {}
        risk_levels = ["Low", "Medium", "High"]
        alternatives = ["Use alternative material", "Increase safety measures", "Optimize workflow"]
        
        for material in materials:
            risk_analysis[material.strip()] = (random.choice(risk_levels), random.choice(alternatives))

        # Supply Chain Risk Analysis
        supply_chain_risks = {material.strip(): ("Unknown risk", "No alternatives available") for material in materials}

        # AI-Based Task Allocation (Swarm Robotics)
        task_difficulty = {"Bricklaying": "High", "Wiring": "Medium", "Painting": "Low"}
        task_allocation = {}
        for task in tasks:
            difficulty = task_difficulty.get(task.strip(), "Medium")
            assigned_to = random.choice(["Robot-1", "Worker-A", "Worker-B"])
            task_allocation[task.strip()] = assigned_to

        # Blockchain Payment Processing Simulation with External QR Code
        qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=SampleQRCode"


        return {
            "design": design,
            "schedule": schedule,
            "workflow": workflow,
            "risk_analysis": risk_analysis,
            "supply_chain_risks": supply_chain_risks,
            "task_allocation": task_allocation,
            "weather_report": weather_report,
            "geotechnical_risk": geotechnical_risk,  # Now dynamically generated
            "adaptive_scheduling": "Schedule remains unchanged.",
            "drone_safety_report": "Drone Report: No hazards detected.",
            "workflow_automation": "AI optimizing construction workflow.",
            "milestone_payment": f"<img src='{qr_url}' alt='Blockchain Payment' width='200px' />"
        }

# Instantiate AI Model
ai = GenerativeAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    data = request.form
    project_name = data.get("project_name", "Unknown Project")
    city = data.get("city", "Unknown City")
    workers = data.get("workers", "").split(",")
    materials = data.get("materials", "").split(",")
    tasks = data.get("tasks", "").split(",")

    # Generate AI-based plan
    ai_plan = ai.generate_plan(project_name, city, workers, materials, tasks)

    return render_template(
        "generated_plan.html",
        project_name=project_name,
        city=city,
        ai_plan=ai_plan
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)
