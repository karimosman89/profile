"""
Professional Configuration Management for Karim Osman's Portfolio
Environment variables, settings, and application configuration
"""

import os
import json
from typing import Dict, Any, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DatabaseConfig:
    """Database configuration settings"""
    host: str = os.getenv('DB_HOST', 'localhost')
    port: int = int(os.getenv('DB_PORT', '5432'))
    name: str = os.getenv('DB_NAME', 'portfolio')
    user: str = os.getenv('DB_USER', 'portfolio_user')
    password: str = os.getenv('DB_PASSWORD', '')
    ssl_mode: str = os.getenv('DB_SSL_MODE', 'prefer')

@dataclass
class RedisConfig:
    """Redis cache configuration"""
    host: str = os.getenv('REDIS_HOST', 'localhost')
    port: int = int(os.getenv('REDIS_PORT', '6379'))
    password: str = os.getenv('REDIS_PASSWORD', '')
    db: int = int(os.getenv('REDIS_DB', '0'))
    ssl: bool = os.getenv('REDIS_SSL', 'false').lower() == 'true'

@dataclass
class EmailConfig:
    """Email service configuration"""
    smtp_server: str = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port: int = int(os.getenv('SMTP_PORT', '587'))
    username: str = os.getenv('EMAIL_USERNAME', '')
    password: str = os.getenv('EMAIL_PASSWORD', '')
    from_address: str = os.getenv('FROM_EMAIL', 'karim.osman.ai@gmail.com')
    use_tls: bool = os.getenv('EMAIL_USE_TLS', 'true').lower() == 'true'

@dataclass
class CloudConfig:
    """Cloud services configuration"""
    aws_access_key_id: str = os.getenv('AWS_ACCESS_KEY_ID', '')
    aws_secret_access_key: str = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    aws_region: str = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    s3_bucket: str = os.getenv('S3_BUCKET_NAME', '')

    gcp_project_id: str = os.getenv('GCP_PROJECT_ID', '')
    gcp_credentials_path: str = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', '')

    azure_storage_account: str = os.getenv('AZURE_STORAGE_ACCOUNT', '')
    azure_storage_key: str = os.getenv('AZURE_STORAGE_KEY', '')

@dataclass
class AnalyticsConfig:
    """Analytics and monitoring configuration"""
    google_analytics_id: str = os.getenv('GOOGLE_ANALYTICS_ID', '')
    sentry_dsn: str = os.getenv('SENTRY_DSN', '')
    hotjar_id: str = os.getenv('HOTJAR_ID', '')
    mixpanel_token: str = os.getenv('MIXPANEL_TOKEN', '')
    enable_tracking: bool = os.getenv('ENABLE_ANALYTICS', 'true').lower() == 'true'

@dataclass
class SecurityConfig:
    """Security and authentication configuration"""
    secret_key: str = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    jwt_algorithm: str = os.getenv('JWT_ALGORITHM', 'HS256')
    jwt_expiration_hours: int = int(os.getenv('JWT_EXPIRATION_HOURS', '24'))
    password_min_length: int = int(os.getenv('PASSWORD_MIN_LENGTH', '8'))
    max_login_attempts: int = int(os.getenv('MAX_LOGIN_ATTEMPTS', '5'))
    session_timeout_minutes: int = int(os.getenv('SESSION_TIMEOUT_MINUTES', '30'))

@dataclass
class AppConfig:
    """Main application configuration"""
    # Application Info
    name: str = os.getenv('APP_NAME', 'Karim Osman - AI/ML Portfolio')
    version: str = os.getenv('APP_VERSION', '2.0.0')
    description: str = os.getenv('APP_DESCRIPTION', 'Professional AI/ML Engineer Portfolio')

    # Environment
    environment: str = os.getenv('STREAMLIT_ENV', 'development')
    debug: bool = os.getenv('DEBUG', 'false').lower() == 'true'

    # Server Settings
    host: str = os.getenv('HOST', '0.0.0.0')
    port: int = int(os.getenv('PORT', '8501'))

    # Professional Information
    owner_name: str = os.getenv('OWNER_NAME', 'Karim Osman')
    owner_email: str = os.getenv('OWNER_EMAIL', 'karim.osman.ai@gmail.com')
    owner_phone: str = os.getenv('OWNER_PHONE', '+20 123 456 7890')
    owner_location: str = os.getenv('OWNER_LOCATION', 'Alexandria, Egypt')

    # Social Links
    linkedin_url: str = os.getenv('LINKEDIN_URL', 'https://linkedin.com/in/karim-osman')
    github_url: str = os.getenv('GITHUB_URL', 'https://github.com/karimosman89')
    twitter_url: str = os.getenv('TWITTER_URL', 'https://twitter.com/karim_ai')
    website_url: str = os.getenv('WEBSITE_URL', 'https://kosman.streamlit.app')

    # Performance Settings
    cache_ttl: int = int(os.getenv('CACHE_TTL', '3600'))
    max_upload_size: int = int(os.getenv('MAX_UPLOAD_SIZE', '50'))  # MB
    rate_limit_per_minute: int = int(os.getenv('RATE_LIMIT_PER_MINUTE', '100'))

    # Feature Flags
    enable_contact_form: bool = os.getenv('ENABLE_CONTACT_FORM', 'true').lower() == 'true'
    enable_analytics: bool = os.getenv('ENABLE_ANALYTICS', 'true').lower() == 'true'
    enable_seo: bool = os.getenv('ENABLE_SEO', 'true').lower() == 'true'
    enable_dark_mode: bool = os.getenv('ENABLE_DARK_MODE', 'true').lower() == 'true'

    # Content Settings
    projects_per_page: int = int(os.getenv('PROJECTS_PER_PAGE', '6'))
    blog_posts_per_page: int = int(os.getenv('BLOG_POSTS_PER_PAGE', '5'))
    testimonials_per_page: int = int(os.getenv('TESTIMONIALS_PER_PAGE', '3'))

class ConfigManager:
    """Professional configuration manager with environment support"""

    def __init__(self, config_file: Optional[str] = None):
        self.config_file = config_file or self._find_config_file()
        self.app = AppConfig()
        self.database = DatabaseConfig()
        self.redis = RedisConfig()
        self.email = EmailConfig()
        self.cloud = CloudConfig()
        self.analytics = AnalyticsConfig()
        self.security = SecurityConfig()

        # Load additional configuration from file if exists
        if self.config_file and Path(self.config_file).exists():
            self._load_config_file()

    def _find_config_file(self) -> str:
        """Find configuration file in common locations"""
        possible_locations = [
            'config.json',
            'config/config.json',
            '.config/portfolio.json',
            os.path.expanduser('~/.portfolio/config.json')
        ]

        for location in possible_locations:
            if Path(location).exists():
                return location

        return 'config.json'  # Default

    def _load_config_file(self):
        """Load configuration from JSON file"""
        try:
            with open(self.config_file, 'r') as f:
                config_data = json.load(f)

            # Update configurations based on file content
            for section, data in config_data.items():
                if hasattr(self, section):
                    config_obj = getattr(self, section)
                    for key, value in data.items():
                        if hasattr(config_obj, key):
                            setattr(config_obj, key, value)

        except Exception as e:
            print(f"Warning: Could not load config file {self.config_file}: {e}")

    def get_streamlit_config(self) -> Dict[str, Any]:
        """Get Streamlit-specific configuration"""
        return {
            'page_title': self.app.name,
            'page_icon': '🚀',
            'layout': 'wide',
            'initial_sidebar_state': 'collapsed',
            'menu_items': {
                'Get Help': self.app.linkedin_url,
                'Report a bug': f'mailto:{self.app.owner_email}',
                'About': f"""
                # {self.app.owner_name} - AI/ML Engineer

                **Professional Portfolio & Showcase**

                Version: {self.app.version}
                Environment: {self.app.environment.title()}

                **Connect with me:**
                - 🌐 [LinkedIn]({self.app.linkedin_url})
                - 💻 [GitHub]({self.app.github_url})
                - ✉️ [Email](mailto:{self.app.owner_email})
                - 🐦 [Twitter]({self.app.twitter_url})

                ---
                *Transforming ideas into intelligent solutions*
                """
            }
        }

    def get_database_url(self) -> str:
        """Get formatted database connection URL"""
        if self.database.password:
            return (f"postgresql://{self.database.user}:{self.database.password}"
                   f"@{self.database.host}:{self.database.port}/{self.database.name}")
        else:
            return (f"postgresql://{self.database.user}"
                   f"@{self.database.host}:{self.database.port}/{self.database.name}")

    def get_redis_url(self) -> str:
        """Get formatted Redis connection URL"""
        protocol = 'rediss' if self.redis.ssl else 'redis'
        if self.redis.password:
            return f"{protocol}://:{self.redis.password}@{self.redis.host}:{self.redis.port}/{self.redis.db}"
        else:
            return f"{protocol}://{self.redis.host}:{self.redis.port}/{self.redis.db}"

    def is_production(self) -> bool:
        """Check if running in production environment"""
        return self.app.environment.lower() == 'production'

    def is_development(self) -> bool:
        """Check if running in development environment"""
        return self.app.environment.lower() == 'development'

    def get_professional_info(self) -> Dict[str, str]:
        """Get professional contact information"""
        return {
            'name': self.app.owner_name,
            'email': self.app.owner_email,
            'phone': self.app.owner_phone,
            'location': self.app.owner_location,
            'linkedin': self.app.linkedin_url,
            'github': self.app.github_url,
            'twitter': self.app.twitter_url,
            'website': self.app.website_url
        }

    def save_config(self, filename: Optional[str] = None):
        """Save current configuration to file"""
        filename = filename or self.config_file

        config_data = {
            'app': self.app.__dict__,
            'database': self.database.__dict__,
            'redis': self.redis.__dict__,
            'email': self.email.__dict__,
            'cloud': self.cloud.__dict__,
            'analytics': self.analytics.__dict__,
            'security': self.security.__dict__
        }

        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w') as f:
                json.dump(config_data, f, indent=2)
            print(f"Configuration saved to {filename}")
        except Exception as e:
            print(f"Error saving configuration: {e}")

# Professional Theme Configuration
class ThemeConfig:
    """Professional color theme and styling configuration"""

    PRIMARY_COLORS = {
        'blue': '#2E86AB',
        'blue_dark': '#1E5A73',
        'blue_light': '#4A9BC7',
        'orange': '#F24236',
        'orange_dark': '#D63327',
        'green': '#A23B72',
        'purple': '#6C5CE7'
    }

    NEUTRAL_COLORS = {
        'white': '#FFFFFF',
        'light_gray': '#F8F9FA',
        'medium_gray': '#6C757D',
        'dark_gray': '#343A40',
        'black': '#000000'
    }

    SEMANTIC_COLORS = {
        'success': '#28a745',
        'warning': '#ffc107',
        'error': '#dc3545',
        'info': '#17a2b8'
    }

    @classmethod
    def get_color_palette(cls) -> Dict[str, str]:
        """Get complete color palette for the application"""
        return {
            **cls.PRIMARY_COLORS,
            **cls.NEUTRAL_COLORS,
            **cls.SEMANTIC_COLORS
        }

# Global Configuration Instance
config = ConfigManager()

# Environment-specific settings
if config.is_production():
    # Production optimizations
    config.app.debug = False
    config.app.cache_ttl = 7200  # 2 hours
elif config.is_development():
    # Development settings
    config.app.debug = True
    config.app.cache_ttl = 60  # 1 minute

# Export configuration objects
__all__ = [
    'config',
    'AppConfig',
    'DatabaseConfig',
    'RedisConfig',
    'EmailConfig',
    'CloudConfig',
    'AnalyticsConfig',
    'SecurityConfig',
    'ConfigManager',
    'ThemeConfig'
]
