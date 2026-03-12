
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # -------------------------
    # Azure Blob Storage
    # -------------------------
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsimages296696'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'FqSMzuz5NMqYxuB7s9w4FfUtmrsSEZAotVIiP5UaEilUJn8fSJhlwfiIIu2w+7U4eCo2aFrsbWSx+AStzDWmcg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # -------------------------
    # Azure SQL Database
    # -------------------------
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsserver296696.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'

    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD +
        '@' + SQL_SERVER + ':1433/' + SQL_DATABASE +
        '?driver=ODBC+Driver+17+for+SQL+Server'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -------------------------
    # Microsoft Entra ID (OAuth)
    # -------------------------
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'gfD8Q~gXnTF6grgO1VJNechsI02eyF5ItvbYJaP7'
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'b7203e7b-faab-4c3e-a29e-501109881b42'

    AUTHORITY = "https://login.microsoftonline.com/common"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
