from resume_agent.profile.profile_loader import (
    ProfileLoader
)

profile = (

    ProfileLoader()

    .get()

)

for k, v in profile.items():

    print()

    print(

        k

    )

    print(

        v

    )