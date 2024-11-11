from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import subprocess

app = Flask(__name__)

csv_path = './static/graph_gen/data/ai_universities_full_data.csv'

def load_data():
    return pd.read_csv(csv_path)

def save_data(df):
    df.to_csv(csv_path, index=False)

def regenerate_all_charts():
    # Run each chart generation script
    subprocess.run(['python', './static/graph_gen/line_plot.py'])
    subprocess.run(['python', './static/graph_gen/scatter_plot.py'])
    subprocess.run(['python', './static/graph_gen/histogram.py'])
    subprocess.run(['python', './static/graph_gen/density_contour.py'])
    subprocess.run(['python', './static/graph_gen/geograph.py'])
    subprocess.run(['python', './static/graph_gen/text_anno.py'])
    subprocess.run(['python', './static/graph_gen/three_dim.py'])
    subprocess.run(['python', './static/graph_gen/visual_error.py'])

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
