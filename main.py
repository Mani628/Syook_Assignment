import asyncio
from bleak import BleakScanner
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Store packets for analysis
collected_packets = []

def analyze_packets(packets):
    """Analyze movement from collected accelerometer packets"""
    try:
        # Extract x, y, z values from all packets
        x_vals = []
        y_vals = []
        z_vals = []
        
        for packet_hex in packets:
            x = int(packet_hex[24:28], 16)
            y = int(packet_hex[28:32], 16)
            z = int(packet_hex[32:36], 16)
            
            # Convert to signed values
            x = (x - 65536) if x > 32767 else x
            y = (y - 65536) if y > 32767 else y
            z = (z - 65536) if z > 32767 else z
            
            x_vals.append(x)
            y_vals.append(y)
            z_vals.append(z)
        
        # Calculate statistics
        x_std = np.std(x_vals)
        y_std = np.std(y_vals)
        z_std = np.std(z_vals)
        
        # Calculate total variation
        total_variation = np.sqrt(x_std**2 + y_std**2 + z_std**2)
        
        # Movement threshold
        threshold = 2.0
        
        # Print results
        logger.info(f"Total variation: {total_variation}")
        logger.info("Status: " + ("Moving" if total_variation > threshold else "Stationary"))
        
    except Exception as e:
        logger.error(f"Error analyzing packets: {e}")

async def main():
    logger.info("Starting BLE Scanner...")

    def callback(device, advertising_data):
        """Callback for each BLE advertisement received"""
        if device.address:  # Check if device exists
            # Get manufacturer data
            raw_data = advertising_data.manufacturer_data
            if raw_data:
                # Convert manufacturer data to hex string
                hex_data = ''.join([f'{x:02x}' for x in next(iter(raw_data.values()))])
                
                # Check if it's an accelerometer packet
                if "0201060303E1FF" in hex_data:
                    logger.info(f"Accelerometer packet received: {hex_data}")
                    collected_packets.append(hex_data)
                    
                    # Analyze after collecting 3 packets
                    if len(collected_packets) >= 3:
                        logger.info("\nAnalyzing collected packets:")
                        analyze_packets(collected_packets)
                        collected_packets.clear()  # Clear for next batch

    try:
        while True:
            # Create and start scanner
            scanner = BleakScanner(detection_callback=callback)
            await scanner.start()
            logger.info("Scanning for BLE packets...")
            await asyncio.sleep(5)  # Scan for 5 seconds
            await scanner.stop()
    except KeyboardInterrupt:
        logger.info("Scanning stopped by user")
    except Exception as e:
        logger.error(f"Error in scanning: {e}")

if __name__ == "__main__":
    # First install required packages:
    # pip install bleak numpy
    asyncio.run(main())