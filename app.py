from flask import Flask, render_template, request, jsonify
import pandas as pd
import subprocess
import logging
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

csv_path = './static/graph_gen/data/ai_universities_full_data.csv'

# Set up logging to track chart generation process
logging.basicConfig(filename='chart_generation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_data():
    return pd.read_csv(csv_path)

def save_data(df):
    df.to_csv(csv_path, index=False)

def regenerate_all_charts():
    charts = [
        './static/graph_gen/line_plot.py',
        './static/graph_gen/scatter_plot.py',
        './static/graph_gen/histogram.py',
        './static/graph_gen/density_contour.py',  # Focus on contour plot
        # Skipping geograph.py (geospatial chart) for now
        './static/graph_gen/text_anno.py',
        './static/graph_gen/three_dim.py',
        './static/graph_gen/visual_error.py'
    ]
    
    # Create a ThreadPoolExecutor to run the charts in parallel
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_chart = {executor.submit(run_chart, chart): chart for chart in charts}

        # Log status of each chart
        for future in future_to_chart:
            chart = future_to_chart[future]
            try:
                future.result()  # Wait for chart to complete
                logging.info(f"Successfully generated chart: {chart}")
            except Exception as e:
                logging.error(f"Error generating chart {chart}: {e}")

def run_chart(chart):
    """Helper function to run chart generation scripts."""
    try:
        logging.info(f"Starting chart generation: {chart}")
        result = subprocess.run(
            ['python', chart],
            check=True, 
            capture_output=True, 
            text=True, 
            timeout=120  # Timeout for 120 seconds
        )

        logging.info(f"Stdout for {chart}: {result.stdout}")
        logging.error(f"Stderr for {chart}: {result.stderr}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error generating chart {chart}: {e}")
    except subprocess.TimeoutExpired as e:
        logging.error(f"Timeout expired while generating chart {chart}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in chart generation {chart}: {e}")

@app.route('/')
def index():
    df = load_data()
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

@app.route('/edit', methods=['POST'])
def edit():
    try:
        updated_data = request.form.to_dict(flat=False)
        df = pd.DataFrame(updated_data)
        save_data(df)

        # Regenerate all charts asynchronously after saving data
        regenerate_all_charts()

        return jsonify({"status": "success", "message": "Data updated successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
