from flask import Flask, render_template, request, jsonify
import pandas as pd
import subprocess
import threading

app = Flask(__name__)

csv_path = './static/graph_gen/data/ai_universities_full_data.csv'

# Function to load the data from CSV
def load_data():
    return pd.read_csv(csv_path)

# Function to save the data to CSV
def save_data(df):
    df.to_csv(csv_path, index=False)

# Function to regenerate all charts (runs in a separate thread)
def regenerate_all_charts():
    try:
        # Run each chart generation script
        subprocess.run(['python', './static/graph_gen/line_plot.py'], check=True)
        subprocess.run(['python', './static/graph_gen/scatter_plot.py'], check=True)
        subprocess.run(['python', './static/graph_gen/histogram.py'], check=True)
        subprocess.run(['python', './static/graph_gen/density_contour.py'], check=True)
        subprocess.run(['python', './static/graph_gen/geograph.py'], check=True)
        subprocess.run(['python', './static/graph_gen/text_anno.py'], check=True)
        subprocess.run(['python', './static/graph_gen/three_dim.py'], check=True)
        subprocess.run(['python', './static/graph_gen/visual_error.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error in chart generation: {e}")

# Function to run regenerate_all_charts in a separate thread
def regenerate_charts_in_background():
    chart_thread = threading.Thread(target=regenerate_all_charts)
    chart_thread.start()

# Route to the homepage
@app.route('/')
def index():
    df = load_data()
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

# Route to handle data editing and chart regeneration
@app.route('/edit', methods=['POST'])
def edit():
    try:
        # Get updated data from the form and save it to the CSV file
        updated_data = request.form.to_dict(flat=False)
        df = pd.DataFrame(updated_data)
        save_data(df)

        # Regenerate all charts in the background
        regenerate_charts_in_background()

        return jsonify({"status": "success", "message": "Data updated successfully, charts regenerating!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
