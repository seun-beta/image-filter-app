from urllib import request
from flask import Blueprint, jsonify, request

from flasgger import swag_from


from src.constants.http_status_codes import (
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from src.util.util import process_image_url

image_filter_bp = Blueprint(
    "image_filter", __name__, url_prefix="/api/v1/image-filter"
)


@image_filter_bp.get("/")
@swag_from("../docs/image/image.yaml")
def filter_image() -> str:

    image_url = request.args.get("image_url")

    try:
        filtered_image = process_image_url(image_url=image_url)
    except:
        return jsonify(
            {"data": filtered_image}, HTTP_500_INTERNAL_SERVER_ERROR
        )

    return jsonify({"data": filtered_image}, HTTP_200_OK)
