def validate_poll_data(attrs):
    if "title" in attrs and len(attrs.get("title")) < 1:
        return "title field is required"
    elif "body" in attrs and len(attrs["body"]) < 0:
        return "Must be body more than two field is required"
    else:
        return True


