# EZPark
About The Parking Ticket Prediction Tool predicts the likelihood of receiving a parking ticket at a specific location based on historical violation data, using BFS and Dijkstra's algorithms to compare efficiency in analyzing the data. Only works in Washington DC.
## Getting Started

### Prerequisites

Before you begin, make sure that on your local system you have all of these set up:

- Python 3.x installed on your local machine
- Flask and other required Python packages installed (listed in `requirements.txt`)

### Installation

1. **Clone the Repository**: Clone the repository to your local machine.
   ```sh
   git clone https://github.com/joel13samuel/EZPark.git
   cd EZPark

2. **Install Dependencies**: Install the required Python packages.
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Flask Application**: Start the Flask development server.
    ```sh
    python app.py
    ```

## Usage

1. **Open the Application**: Open your  browser and go to `http://127.0.0.1:5000/`.
2. **Input Location**: Enter the latitude and longitude of the location you want to check.
3. **Select Algorithm**: Choose between BFS and Dijkstra's algorithm and click "Predict".
4. **View Results**: View the prediction results, including the probability of getting a ticket, execution time, total violations found, and a map displaying nearby violations.
