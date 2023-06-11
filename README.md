# Mongo
Mongo is a Python application that demonstrates how to interact with MongoDB, a popular NoSQL database. It provides examples of basic CRUD operations (Create, Read, Update, Delete) using the PyMongo library.

## Prerequisites
Before running this application, make sure you have the following installed:

Python (version 3.6 or higher)
MongoDB (running locally or accessible via a connection string)

## Installation
- Clone the repository:
``` bash
git clone https://github.com/eYasarbas/Mongo.git
```
- Change to the project directory:
``` bash
cd Mongo
```
- Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Configuration
Open the config.py file and update the MongoDB connection details based on your setup:
```python
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'mydatabase'
```
## Usage
The application provides a command-line interface (CLI) for performing various MongoDB operations. Here are the available commands:

- python main.py create - Create a new document in the database.
- python main.py read - Read and display documents from the database.
- python main.py update - Update an existing document in the database.
- python main.py delete - Delete a document from the database.

For example, to create a new document:
```bash
python main.py create
```
Follow the prompts to enter the necessary details for creating the document.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contact
For any questions or inquiries, feel free to reach out to the project maintainer:

## References
MongoDB: https://www.mongodb.com/
PyMongo Documentation: https://pymongo.readthedocs.io/
