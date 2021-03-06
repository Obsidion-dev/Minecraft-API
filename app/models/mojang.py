from pydantic import BaseModel, Field


class MojangStatus(BaseModel):
    https_www_minecraft_net: str = Field(
        default="green", alias="https://www.minecraft.net"
    )
    https_account_mojang_com: str = Field(
        default="green", alias="https://account.mojang.com"
    )
    https_authserver_mojang_com: str = Field(
        default="green", alias="https://authserver.mojang.com"
    )
    https_api_mojang_com: str = Field(default="green", alias="https://api.mojang.com")
    https_textures_minecraft_net: str = Field(
        default="green", alias="https://textures.minecraft.net"
    )

    class Config:
        schema_extra = {
            "example": {
                "https://www.minecraft.net": "green",
                "https://account.mojang.com": "green",
                "https://authserver.mojang.com": "green",
                "https://api.mojang.com": "green",
                "https://textures.minecraft.net": "green",
            }
        }
