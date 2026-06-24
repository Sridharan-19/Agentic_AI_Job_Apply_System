import yaml
from pathlib import Path


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

        base_dir = Path(__file__).parent

        profile = self.load_yaml(

            base_dir / "profile.yaml"

        )

        education = self.load_yaml(

            base_dir / "education.yaml"

        )

        experience = self.load_yaml(

            base_dir / "experience.yaml"

        )

        preferences = self.load_yaml(

            base_dir / "preferences.yaml"

        )

        return {

            **profile,

            **education,

            **experience,

            **preferences

        }