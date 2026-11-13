# from pydantic_settings import BaseSettings, SettingsConfigDict
# # 配置类，用于读取环境变量中的配置信息
# class Settings(BaseSettings):
#     openai_api_key: str
#     openai_base_url: str | None = None
#     model_name: str
#     database_url: str
# # 默认配置值，可在 .env 文件中覆盖
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         env_file_encoding="utf-8",
#         extra="ignore",
#     )
    
#     openai_api_key: str = "sk-64f65693845b4f5bba0cc41abb9fd742"
#     openai_base_url: str | None = "https://api.deepseek.com"
#     model_name: str = "deepseek-flash"
#     database_url: str = ""
#     # 实例化配置类，读取环境变量中的配置信息
# settings = Settings()


from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    openai_api_key: str = "sk-64f65693845b4f5bba0cc41abb9fd742"
    openai_base_url: str | None = "https://api.deepseek.com"
    model_name: str = "deepseek-flash"
    database_url: str = ""
    model_config = SettingsConfigDict(env_file='.env',env_file_encoding='utf-8')  

settings = Settings()