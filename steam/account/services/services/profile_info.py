from account.models import Profile, ProfileComment


def get_profile(input_data):
    output_data = Profile.objects.filter(profile_id=input_data)
    output_data += ProfileComment.objects.filter(profile_id=input_data)
    return output_data
