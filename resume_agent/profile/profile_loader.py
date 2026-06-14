import yaml


class ProfileLoader:

    def load_yaml(self, path):

        with open(

            path,

            encoding="utf-8"

        ) as f:

            return yaml.safe_load(

                f

            )

    def get(self):

        profile = self.load_yaml(

            "resume_agent/profile/profile.yaml"

        )

        education = self.load_yaml(

            "resume_agent/profile/education.yaml"

        )

        experience = self.load_yaml(

            "resume_agent/profile/experience.yaml"

        )

        preferences = self.load_yaml(

            "resume_agent/profile/preferences.yaml"

        )

        return {

            **profile,

            **education,

            **experience,

            **preferences

        }