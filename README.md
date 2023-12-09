## Attendance Monitoring

### Requirements
1. Python 3.10.12+
2. Ubuntu or any Linux-based distribution (for facial recognition)

### Installation

To install the required dependencies and set up the environment, follow these steps:

1. **Install Python dependencies**: Run the following command to install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

2. **Create a local .env file**: Copy the `.env.example` file to create a local `.env` file:

   ```
   cp .env.example .env
   ```

3. **Migrate the database**: Execute the following command to migrate the database:

   ```
   flask db upgrade
   ```

4. **Create an admin account**: Use the `flask create-superuser` command to create an admin account:

   ```
   flask create-superuser
   ```

5. **Run the server**: Start the server with the `flask run --debug` command:

   ```
   flask run --debug
   ```
