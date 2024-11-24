# BLE Accelerometer Movement Detection

A Python application that detects movement of a BLE tag by analyzing accelerometer data broadcast through Bluetooth Low Energy advertisements. This project is designed to ingest accelerometer data from a real BLE Tag and determine whether the tag is moving or stationary.

## Features

- Real-time BLE packet scanning
- Accelerometer data analysis (X, Y, Z axes)
- Movement detection based on statistical analysis
- Support for both accelerometer and iBeacon packet formats
- Comprehensive logging system


## Prerequisites

- Windows 10/11
- Bluetooth adapter
- Python 3.9+ 

## Project Structure

```
ble-scanner/
│── main.py                # BLE scanner implementation
│── requirements.txt      # Python dependencies
└── README.md            # Documentation
```

## Installation and Running

1. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python main.py
```

## Packet Format Support

The application supports two types of BLE packets:

1. Accelerometer Packets:
Example: `0x0201060303E1FF1216E1FFA10364FFF4000FFF003772A33F23AC`

2. iBeacon Packets:
Example: `0x0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8`

## Movement Detection Logic

The application:
1. Collects accelerometer data from BLE packets
2. Extracts X, Y, Z acceleration values
3. Calculates standard deviation for each axis
4. Computes total variation using 3D vector magnitude
5. Compares against a threshold to determine movement status

## Sample Output

```
2024-xx-xx xx:xx:xx - INFO - Starting BLE Scanner...
2024-xx-xx xx:xx:xx - INFO - Scanning for BLE packets...
2024-xx-xx xx:xx:xx - INFO - Accelerometer packet received: 0x0201060303E1FF...
2024-xx-xx xx:xx:xx - INFO - Analyzing collected packets:
2024-xx-xx xx:xx:xx - INFO - Total variation: 2.5
2024-xx-xx xx:xx:xx - INFO - Status: Moving
```
# BLE Accelerometer Movement Detection

A Python application that detects movement of a BLE tag by analyzing accelerometer data broadcast through Bluetooth Low Energy advertisements. This project is designed to ingest accelerometer data from a real BLE Tag and determine whether the tag is moving or stationary.

## Features

- Real-time BLE packet scanning
- Accelerometer data analysis (X, Y, Z axes)
- Movement detection based on statistical analysis
- Support for both accelerometer and iBeacon packet formats
- Comprehensive logging system


## Prerequisites

- Windows 10/11
- Bluetooth adapter
- Python 3.9+ 

## Project Structure

```
ble-scanner/
│── main.py                # BLE scanner implementation
│── requirements.txt      # Python dependencies
└── README.md            # Documentation
```

## Installation and Running

1. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python main.py
```

## Packet Format Support

The application supports two types of BLE packets:

1. Accelerometer Packets:
Example: `0x0201060303E1FF1216E1FFA10364FFF4000FFF003772A33F23AC`

2. iBeacon Packets:
Example: `0x0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8`

## Movement Detection Logic

The application:
1. Collects accelerometer data from BLE packets
2. Extracts X, Y, Z acceleration values
3. Calculates standard deviation for each axis
4. Computes total variation using 3D vector magnitude
5. Compares against a threshold to determine movement status

## Sample Output

```
2024-xx-xx xx:xx:xx - INFO - Starting BLE Scanner...
2024-xx-xx xx:xx:xx - INFO - Scanning for BLE packets...
2024-xx-xx xx:xx:xx - INFO - Accelerometer packet received: 0x0201060303E1FF...
2024-xx-xx xx:xx:xx - INFO - Analyzing collected packets:
2024-xx-xx xx:xx:xx - INFO - Total variation: 2.5
2024-xx-xx xx:xx:xx - INFO - Status: Moving
```

