from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, computed_field

from app.config import settings


class FileAttachmentBase(BaseModel):
    original_filename: Annotated[str, Field(max_length=255)]
    mime_type: Annotated[str, Field(max_length=100)]
    file_size: int


class FileAttachmentResponse(FileAttachmentBase):
    id: int
    s3_key: str
    uploaded_at: datetime

    @computed_field
    def file_url(self) -> str:
        return f"{settings.s3_bucket_url}/{self.s3_key}"

    @computed_field
    def file_id(self) -> int:
        return self.id

    model_config = ConfigDict(from_attributes=True)


class FileDownloadResponse(BaseModel):
    file_id: int
    original_filename: str
    download_url: str
    expires_in: int  # seconds
