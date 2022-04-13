"""Main class will execute the methods"""
import repository_operations
import s3_upload


if __name__ == "__main__":
    CLONE_RESPONSE = repository_operations.clone_repository()
    if CLONE_RESPONSE:
        ZIP_RESPONSE = repository_operations.zip_file()
        if ZIP_RESPONSE:
            UPLOAD_S3_RESPONSE = s3_upload.upload_file()
            if UPLOAD_S3_RESPONSE:
                repository_operations.delete_local_files()
