def combine_name(strategy, details, backend, **kwargs):
    if "first_name" in details or "last_name" in details:
        details["name"] = f"{details.get('first_name', '')} {details.get('last_name', '')}".strip()
    return {"details": details}