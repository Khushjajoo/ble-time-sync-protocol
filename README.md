# BLE Time Synchronization Protocol using ESP32s

This project implements a custom time synchronization protocol over Bluetooth Low Energy (BLE) using three ESP32 boards—two clients and one server. It aims to measure and correct clock drift and network latency between distributed embedded devices. The server broadcasts its timestamp to the clients, which compare it to their local clocks to estimate drift and delay. The adjust.py script helps fine-tune synchronization offset calculations, while com_serial.py provides a quick way to visualize serial outputs from the ESP32 boards. This setup was designed to demonstrate efficient, low-latency communication and time alignment across multiple nodes in a BLE network.

