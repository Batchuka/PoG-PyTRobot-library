
class {{cookiecutter.class_name}}:
    _connection_url = None
    _retry_attempts = 3
    _debug_mode = False
    _log_level = "info"
    # Adicione outras configurações relevantes aqui

    @classmethod
    def load_properties(cls):
        # Lógica para carregar configurações de um arquivo .properties (a ser implementada)
        pass

    @classmethod
    def get_connection_url(cls):
        return cls._connection_url

    @classmethod
    def set_connection_url(cls, value):
        # Adicione validações, se necessário
        cls._connection_url = value

    @classmethod
    def get_retry_attempts(cls):
        return cls._retry_attempts

    @classmethod
    def set_retry_attempts(cls, value):
        # Adicione validações, se necessário
        cls._retry_attempts = value

    @classmethod
    def get_debug_mode(cls):
        return cls._debug_mode

    @classmethod
    def set_debug_mode(cls, value):
        # Adicione validações, se necessário
        cls._debug_mode = value

    @classmethod
    def get_log_level(cls):
        return cls._log_level

    @classmethod
    def set_log_level(cls, value):
        # Adicione validações, se necessário
        cls._log_level = value


# Exemplo de uso e testes
if __name__ == '__main__':
    
    package_config_instance = {{cookiecutter.class_name}}()

    # Exemplo de uso das propriedades
    package_config_instance.connection_url = "https://example.com"
    package_config_instance.retry_attempts = 5
    package_config_instance.debug_mode = True
    package_config_instance.log_level = "debug"

    # Exemplo de uso da função load_properties (a ser implementada)
    package_config_instance.load_properties()

    # Exibindo configurações
    print(f"Connection URL: {package_config_instance.connection_url}")
    print(f"Retry Attempts: {package_config_instance.retry_attempts}")
    print(f"Debug Mode: {package_config_instance.debug_mode}")
    print(f"Log Level: {package_config_instance.log_level}")
