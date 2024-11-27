from flask import Flask, render_template, request, jsonify
import pandas as pd
import subprocess
import threading
import logging

# Initialize Flask app
app = Flask(__name__)

# Path to the CSV file
csv_path = './static/graph_gen/data/ai_universities_full_data.csv'

# Set up logging to track chart generation process
logging.basicConfig(filename='chart_generation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to load data from CSV
def load_data():
    return pd.read_csv(csv_path)

# Function to save updated data to CSV
def save_data(df):
    df.to_csv(csv_path, index=False)

# Function to regenerate all charts with error handling
def regenerate_all_charts():
    charts = [
        './static/graph_gen/line_plot.py',
        './static/graph_gen/scatter_plot.py',
        './static/graph_gen/histogram.py',
        './static/graph_gen/density_contour.py',
        './static/graph_gen/geograph.py',
        './static/graph_gen/text_anno.py',
        './static/graph_gen/three_dim.py',
        './static/graph_gen/visual_error.py'
    ]

    for chart in charts:
        try:
            logging.info(f"Running chart generation: {chart}")
            # Run each chart generation script
            subprocess.run(['python', chart], check=True)
            logging.info(f"Successfully generated chart: {chart}")
        except subprocess.CalledProcessError as e:
            # If chart generation fails, log the error and skip the chart
            logging.error(f"Error generating chart {chart}: {e}")
            continue  # Skip this chart and proceed with the next one

# Function to run regenerate_all_charts in a background thread
def regenerate_charts_in_background():
    chart_thread = threading.Thread(target=regenerate_all_charts)
    chart_thread.start()

# Route to the homepage
@app.route('/')
def index():
    df = load_data()
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

# Route to handle data editing and trigger chart regeneration
@app.route('/edit', methods=['POST'])
def edit():
    try:
        # Get updated data from the form and save it to the CSV file
        updated_data = request.form.to_dict(flat=False)
        df = pd.DataFrame(updated_data)
        save_data(df)

        # Regenerate all charts asynchronously in the background
        regenerate_charts_in_background()

        return jsonify({"status": "success", "message": "Data updated successfully, charts regenerating!"})
    except Exception as e:
        # If there's an error while saving data or triggering chart regeneration
        logging.error(f"Error during data update: {e}")
        return jsonify({"status": "error", "message": str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
