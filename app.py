from flask import Flask, render_template, request, jsonify
import pandas as pd
import subprocess
import logging

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

    for chart in charts:
        try:
            logging.info(f"Starting chart generation: {chart}")
            # Run each chart generation script with a timeout of 60 seconds
            result = subprocess.run(
                ['python', chart],
                check=True, 
                capture_output=True, 
                text=True, 
                timeout=60  # Timeout for 60 seconds
            )
            
            # Log stdout and stderr to capture more details
            logging.info(f"Stdout for {chart}: {result.stdout}")
            logging.error(f"Stderr for {chart}: {result.stderr}")

            logging.info(f"Successfully generated chart: {chart}")
        
        except subprocess.CalledProcessError as e:
            # If chart generation fails, log the error and skip the chart
            logging.error(f"Error generating chart {chart}: {e}")
            continue  # Skip this chart and proceed with the next one
        
        except subprocess.TimeoutExpired as e:
            # If subprocess times out, log and skip the chart
            logging.error(f"Timeout expired while generating chart {chart}: {e}")
            continue  # Skip this chart and proceed with the next one
        
        except Exception as e:
            # Log any unexpected errors
            logging.error(f"Unexpected error in chart generation {chart}: {e}")
            raise e  # Reraise the error if it's unexpected

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

        # Regenerate all charts after saving data
        regenerate_all_charts()

        return jsonify({"status": "success", "message": "Data updated successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
