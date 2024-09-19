def get_path_avatar_for_user(instance, filname):
    return f'profiles/avatars/{instance.email}/{filname}'