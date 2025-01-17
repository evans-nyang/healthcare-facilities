resource "aws_s3_bucket" "healthcare_facilities_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = var.bucket_name
    Environment = var.environment
  }
}

resource "aws_s3_bucket_ownership_controls" "healthcare_facilities_bucket" {
  bucket = aws_s3_bucket.healthcare_facilities_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "healthcare_facilities_bucket" {
  depends_on = [aws_s3_bucket_ownership_controls.healthcare_facilities_bucket]

  bucket = aws_s3_bucket.healthcare_facilities_bucket.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "versioning_healthcare_facilities_bucket" {
  bucket = aws_s3_bucket.healthcare_facilities_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
