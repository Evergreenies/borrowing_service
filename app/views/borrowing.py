from config import borrowing_app, logger


@borrowing_app.route("/borrowings", methods=["GET"])
def list_borrowings():
    return "OK", 200
