# QR Code Generator API Documentation

## Live Demo

You can try out the API live on [PythonAnywhere](https://nihadgurbanov.pythonanywhere.com/).

## Overview

The QR Code Generator API allows users to generate QR codes dynamically by providing a URL and selecting a color for the QR code.

## Base URL

The base URL for the API is `/qr-code`.

## Endpoints

### Generate QR Code

- **Endpoint:** `/qr-code`
- **Method:** `GET`
- **Description:** Generates a QR code based on the provided URL and color.
- **Parameters:**
  - **`url`** (required): The URL to be encoded in the QR code.
  - **`color`** (optional): The color of the QR code. If not provided, the default color is black.
- **Response:** If successful, returns the generated QR code image. If an error occurs, returns an error message along with the HTTP status code.

## Usage Example

### Request

```
GET /qr-code?url=https://example.com&color=#FF0000
```

### Response

- **HTTP Status Code:** 200 (OK)
- **Content-Type:** image/png
- **Body:** (QR code image)