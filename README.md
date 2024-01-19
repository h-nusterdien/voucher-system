# Voucher System

The Voucher System is a Django-based application designed to create and manage vouchers with various features, including a management interface for staff and superusers and a redemption interface for any user.

## Features

### Management Interface (voucher_management)

- **Authentication:** Accessible only to staff and superusers for configuring and managing vouchers.
- **Voucher Setup:** Configure and manage vouchers with features like redemption limits, expiration dates, etc.

### Redemption Interface (voucher_redemption)

- **Authentication:** Accessible to any user for redeeming vouchers.
- **Redemption Options:** Support single redemption, multiple redemption, and redemption up to a certain number of times.
- **Time Constraints:** Ability to redeem vouchers only before a specified point in time.

## Code Structure

The project follows a modular structure with the following Django apps:

1. **api:** Handles API endpoints and communication with client applications using Django Rest Framework.

2. **dashboard:**
   - **voucher_management:** Restricted to staff and superusers for configuring and managing vouchers.
   - **voucher_redemption:** Accessible to any user for redeeming vouchers.

3. **user_auth:** Handles user authentication and authorization, ensuring only authorized users access the voucher management interface.

4. **voucher_management:** Backend logic for voucher creation, configuration, and management.

5. **voucher_redemption:** Backend logic for voucher redemption.

## Design Choices

- **Framework:** Built using Django and Django Rest Framework for a robust and scalable web application.
- **Authentication:** Utilizes Django's built-in authentication system for secure user authentication.
- **Modularity:** Organized code into separate apps for clearer separation of concerns and maintainability.
- **Database:** Uses Django's ORM for database interactions, allowing easy database migrations and management.
- **RESTful API:** Implements a RESTful API using Django Rest Framework for communication with client applications.

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:hnusterdien/voucher-system.git
   ```
   
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source myenv/bin/activate  # On macOS and Linux
   myenv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Perform database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for Voucher Management dashboard access:
   ```bash
   python manage.py createsuperuser
   ```
   
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
   
7. Access the application in a web browser:
   
   [http://localhost:8000/](http://localhost:8000/)

## Configuration

- **Settings:** Check the settings file (`settings.py`) for any critical configurations specific to your deployment environment.
- **Environment Variables:** Ensure any necessary environment variables are set (if applicable).

## Contributing

Contributions to enhance this project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/fooBar`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some fooBar'`).
5. Push to the branch (`git push origin feature/fooBar`).
6. Create a pull request.

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing.

## License

This project is licensed under the MIT License. See the [License](LICENSE) file for details.
