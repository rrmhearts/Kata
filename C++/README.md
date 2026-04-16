# C++ Katas & Experiments

This directory contains a collection of C++ projects, scripts, and katas. The contents cover a wide range of topics including low-level system interactions, networking, cryptography, message passing, and explorations of modern C++ language features.

## 📋 Table of Contents

1.  Detailed Contents
      - [Cryptography](cryptography)
      - [JSON Integration](json)
      - [Keylogger](keylogger)
      - [Learning & Language Features](learning)
      - [Messaging System](messaging)
      - [TCP Networking](tcp)
      - [Unordered Map/Set](unordered_mapset)

-----

## 🔍 Directory Overview

| Directory | General Information |
| :--- | :--- |
| **[`cryptography/`](./cryptography)** | C++ implementations of standard encryption and cryptographic algorithms. |
| **[`json/`](./json)** | Examples and configurations using the popular `nlohmann/json` library for C++. |
| **[`keylogger/`](./keylogger)** | Low-level system programming scripts focused on capturing keystrokes. |
| **[`learning/`](./learning)** | Exploratory scripts testing C++ memory layout, initialization, and modern language features. |
| **[`messaging/`](./messaging)** | A ZeroMQ-based producer-consumer messaging architecture system. |
| **[`tcp/`](./tcp)** | Socket programming examples, including basic TCP clients/servers and framed message passing. |
| **[`unordered_mapset/`](./unordered_mapset)** | Code utilizing and testing high-performance hash maps (specifically `ankerl::unordered_dense`). |

-----

## 📂 Detailed Contents

### Cryptography

Implementations of fundamental cryptographic algorithms.

  * **[`DES_encryption.cpp`](./cryptography/DES_encryption.cpp)**: Implementation or exploration of the Data Encryption Standard (DES).
  * **[`rsa.cpp`](./cryptography/rsa.cpp)**: C++ implementation of the RSA public-key cryptosystem.

### JSON Integration

Usage of JSON for Modern C++ (`nlohmann/json`).

  * **[`nlohmann.cpp`](./json/nlohmann.cpp)**: Implementation testing and demonstrating JSON parsing and serialization.
  * **[`nlohmann_config.md`](./json/nlohmann_config.md)**: Notes and configuration details for using the library.
  * **[`nlohmann/json.hpp`](./json/nlohmann/json.hpp)**: The single-header library dependency.

### Keylogger

Low-level system monitoring and input capture.

  * **[`keylogger.cpp`](./keylogger/keylogger.cpp)**: Core implementation of keystroke logging functionality.
  * **[`keylogger2.cpp`](./keylogger/keylogger2.cpp)**: Alternative implementation or iteration of the keylogging script.

### Learning & Language Features

Playground files dedicated to understanding C++ language mechanics, types, and standard library features.

  * **[`cpp_list.cpp`](./learning/cpp_list.cpp)**: Explorations into C++ list containers and iterators.
  * **[`initialization.cpp`](./learning/initialization.cpp)**: Testing different C++ variable initialization paradigms.
  * **[`initializer_list.cpp`](./learning/initializer_list.cpp)**: Usage of `std::initializer_list`.
  * **[`reinterpret_cast.cpp`](./learning/reinterpret_cast.cpp)**: Demonstrations of low-level memory casting and its consequences.
  * **[`string_view.cpp`](./learning/string_view.cpp)**: Utilizing `std::string_view` for efficient string handling.
  * **[`structs.cpp`](./learning/structs.cpp)**: Memory layout, padding, and usage of structs in C++.

### Messaging System

A complete ZeroMQ-based architecture for passing messages between distinct processes.

  * **[`Messaging System.md`](./messaging/Messaging%2520System.md)**: Documentation and architecture overview for the messaging system.
  * **[`producer.cpp`](./messaging/producer.cpp)**: The message publisher/sender component.
  * **[`consumer.cpp`](./messaging/consumer.cpp)**: The message subscriber/receiver component.
  * **[`schema.hpp`](./messaging/schema.hpp)**: Data structures defining the format of the transmitted messages.
  * **[`config.json`](./messaging/config.json)**: Configuration file (likely IP addresses, ports, or topic settings).
  * **[`zmq.hpp`](./messaging/zmq.hpp)**: The ZeroMQ C++ header dependency.

### TCP Networking

Raw socket programming spanning fundamental connections to framed application-level protocols.

  * **[`tcp_server.cpp`](./tcp/tcp_server.cpp)** & **[`tcp_client.cpp`](./tcp/tcp_client.cpp)**: Basic raw TCP socket server and client.
  * **[`tcp_copycat.cpp`](./tcp/tcp_copycat.cpp)**: An echo server or stream-copying implementation.
  * **[`framed_messages.cpp`](./tcp/framed_messages.cpp)**: Logic for prefixing TCP streams with length-headers (framing) to prevent message boundary issues.
  * **[`framed_client.cpp`](./tcp/framed_client.cpp)**: A client specifically built to handle framed TCP messages.

### Unordered Map/Set

Experiments with highly efficient, cache-friendly hash map and hash set implementations.

  * **[`unordered.cpp`](./unordered_mapset/unordered.cpp)**: Implementation utilizing fast hashing techniques.
  * **Dependencies (`ankerl` library)**:
      * **[`ankerl/unordered_dense.h`](./unordered_mapset/ankerl/unordered_dense.h)**: A fast, flat hash map implementation.
      * **[`ankerl/stl.h`](./unordered_mapset/ankerl/stl.h)**: Additional standard library compatibilities for the `ankerl` maps.