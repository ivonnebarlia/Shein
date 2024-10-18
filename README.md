# MyApp

## Description
MyApp is a Django-based application that provides an API for managing products and transactions.

## Features
- Manage products with name, description, and sale price.
- Track transactions related to products.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/josebarlia/myapp.git
    cd myapp
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage products and transactions.
- Use the API endpoints to interact with the application programmatically.

## API Endpoints
- List all products: `GET /api/products/`
- Retrieve a product: `GET /api/products/{id}/`
- Create a new product: `POST /api/products/`
- Update a product: `PUT /api/products/{id}/`
- Delete a product: `DELETE /api/products/{id}/`

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request.

## License
This project is licensed under the MIT License.