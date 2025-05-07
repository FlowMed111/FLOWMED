from flask import Flask, render_template, request

app = Flask(__name__)

flower_info = {
    "sunflower": {
        "name": "Sunflower",
        "description": "Sunflowers are tall annuals known for their large yellow blooms.",
        "diseases": [
            {"name": "Rust", "cause": "Puccinia helianthi fungus", "symptoms": "Rust-colored spots on leaves", "management": "Use resistant varieties, apply fungicides"},
            {"name": "Downy Mildew", "cause": "Plasmopara halstedii", "symptoms": "Yellowing of leaves and stunted growth", "management": "Seed treatment and crop rotation"},
            {"name": "Verticillium Wilt", "cause": "Verticillium dahliae", "symptoms": "Wilting and yellowing leaves", "management": "Use disease-free soil and rotate crops"}
        ]
    },
    "chrysanthemum": {
        "name": "Chrysanthemum",
        "description": "Popular ornamental flowers available in many colors and shapes.",
        "diseases": [
            {"name": "Leaf Spot", "cause": "Septoria or Alternaria fungi", "symptoms": "Dark spots on leaves", "management": "Remove affected leaves and apply fungicide"},
            {"name": "Powdery Mildew", "cause": "Fungal spores", "symptoms": "White powdery coating on leaves", "management": "Improve air circulation and apply fungicides"}
        ]
    },
    "orchid": {
        "name": "Orchid",
        "description": "Tropical flowers known for their exotic appearance and long-lasting blooms.",
        "diseases": [
            {"name": "Root Rot", "cause": "Overwatering and poor drainage", "symptoms": "Mushy, brown roots", "management": "Repot and trim affected roots"},
            {"name": "Botrytis", "cause": "Botrytis cinerea fungus", "symptoms": "Spots on flowers", "management": "Improve air flow and remove infected blooms"},
            {"name": "Leaf Spot", "cause": "Fungal or bacterial pathogens", "symptoms": "Spots on leaves", "management": "Isolate infected plants, use bactericides"},
            {"name": "Fusarium Wilt", "cause": "Fusarium oxysporum", "symptoms": "Yellowing leaves and plant collapse", "management": "Use sterilized tools and fungicides"}
        ]
    },
    "marigold": {
        "name": "Marigold",
        "description": "Known for their vibrant orange and yellow blooms.",
        "diseases": [
            {"name": "Alternaria Leaf Spot", "cause": "Alternaria fungi", "symptoms": "Dark spots on leaves", "management": "Remove infected leaves, apply fungicides"},
            {"name": "Aster Yellows", "cause": "Phytoplasma", "symptoms": "Yellowing and stunted growth", "management": "Control insect vectors and remove infected plants"}
        ]
    },
    "bougainvillea": {
        "name": "Bougainvillea",
        "description": "Vibrant flowering plant known for its colorful bracts.",
        "diseases": [
            {"name": "Anthracnose", "cause": "Colletotrichum fungi", "symptoms": "Dark lesions on leaves and stems", "management": "Prune infected branches and apply fungicide"}
        ]
    },
    "hibiscus": {
        "name": "Hibiscus",
        "description": "Tropical plants known for their large, showy flowers.",
        "diseases": [
            {"name": "Leaf Curl", "cause": "Aphids or whiteflies", "symptoms": "Curling and deformed leaves", "management": "Control insects with insecticidal soap"},
            {"name": "Blight", "cause": "Fungal pathogens", "symptoms": "Blackened and rotting leaves", "management": "Prune infected parts and apply fungicides"}
        ]
    },
    "gerbera": {
        "name": "Gerbera",
        "description": "Bright, daisy-like flowers that come in many colors.",
        "diseases": [
            {"name": "Crown Rot", "cause": "Fusarium or Pythium fungi", "symptoms": "Rotting at the base of the plant", "management": "Improve drainage and avoid overwatering"},
            {"name": "Leaf Spot", "cause": "Bacterial or fungal pathogens", "symptoms": "Spots on leaves", "management": "Remove affected leaves and apply appropriate fungicides"}
        ]
    },
    "lily": {
        "name": "Lily",
        "description": "Popular flower known for its large, fragrant blooms.",
        "diseases": [
            {"name": "Botrytis Blight", "cause": "Botrytis cinerea", "symptoms": "Gray mold on leaves and flowers", "management": "Remove infected plant parts and improve air circulation"},
            {"name": "Basal Rot", "cause": "Fusarium spp.", "symptoms": "Wilted and yellowing leaves", "management": "Plant in well-drained soil and rotate crops"}
        ]
    },
    "rose": {
        "name": "Rose",
        "description": "Classic flowering shrub with many varieties.",
        "diseases": [
            {"name": "Black Spot", "cause": "Diplocarpon rosae fungus", "symptoms": "Black spots with yellow halos on leaves", "management": "Remove affected leaves and apply fungicide"},
            {"name": "Powdery Mildew", "cause": "Erysiphe cichoracearum fungus", "symptoms": "White powdery coating on leaves", "management": "Increase air circulation and apply fungicides"},
            {"name": "Rust", "cause": "Puccinia spp.", "symptoms": "Orange pustules on the underside of leaves", "management": "Remove infected leaves and apply fungicides"}
        ]
    },
    "violet": {
        "name": "Violet",
        "description": "Small, colorful flowering plants.",
        "diseases": [
            {"name": "Crown Rot", "cause": "Fusarium or Pythium fungi", "symptoms": "Rotting base of the plant", "management": "Improve drainage and avoid overwatering"},
            {"name": "Powdery Mildew", "cause": "Erysiphe cichoracearum", "symptoms": "White powdery coating on leaves", "management": "Increase airflow and apply fungicides"}
        ]
    },
    "zinnia": {
        "name": "Zinnia",
        "description": "Bright and easy-to-grow flowers in many colors.",
        "diseases": [
            {"name": "Alternaria Blight", "cause": "Alternaria fungi", "symptoms": "Dark lesions on leaves", "management": "Remove affected leaves and apply fungicides"},
            {"name": "Powdery Mildew", "cause": "Erysiphe cichoracearum", "symptoms": "White powdery coating on leaves", "management": "Improve air circulation and apply fungicides"}
        ]
    }
    # Add more flowers as needed...
}

flower_names = list(flower_info.keys())  # List of flower names to help with navigation

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/selection', methods=['GET', 'POST'])
def selection():
    if request.method == 'POST':
        selected_plant = request.form['plant']
        return render_template('result.html', plant=selected_plant, active_page='detection')
    return render_template('selection.html', active_page='detection')

@app.route('/flower/<flower_name>')
def flower_details(flower_name):
    flower_data = flower_info.get(flower_name.lower())
    
    if flower_data:
        # Get the index of the current flower in the flower_names list
        flower_index = flower_names.index(flower_name.lower())
        
        # Get the next and previous flower names
        next_flower = flower_names[(flower_index + 1) % len(flower_names)]
        prev_flower = flower_names[(flower_index - 1) % len(flower_names)]
        
        return render_template('flower_details.html', flower_data=flower_data, next_flower=next_flower, prev_flower=prev_flower, active_page=None)
    else:
        return f"<h2>Details for '{flower_name}' not found.</h2>", 404

@app.route('/result')
def result():
    return render_template('result.html', active_page='detection')

if __name__ == '__main__':from flask import Flask, render_template, request

app = Flask(__name__)

flower_info = {
    # Your flower info dictionary...
}

flower_names = list(flower_info.keys())  # List of flower names to help with navigation

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/flower/<flower_name>')
def flower_details(flower_name):
    flower_data = flower_info.get(flower_name.lower())
    
    if flower_data:
        # Get the index of the current flower in the flower_names list
        flower_index = flower_names.index(flower_name.lower())
        
        # Get the next and previous flower names
        next_flower = flower_names[(flower_index + 1) % len(flower_names)]
        prev_flower = flower_names[(flower_index - 1) % len(flower_names)]
        
        return render_template('flower_details.html', flower_data=flower_data, next_flower=next_flower, prev_flower=prev_flower, active_page=None)
    else:
        return f"<h2>Details for '{flower_name}' not found.</h2>", 404

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)
