import yaml

from pathlib import Path

class ProfileBuilder:

    def __init__(

            self,

            yaml_path=None

    ):
        if yaml_path is None:
            yaml_path = Path(__file__).parent / "profile.yaml"

        with open(

                yaml_path,

                encoding="utf-8"

        ) as f:

            self.profile = yaml.safe_load(f)

    def build_profile_text(

            self

    ):

        text = []

        text.append(

            self.profile.get(

                "current_role",

                ""

            )

        )

        text.append(

            self.profile.get(

                "experience_years",

                ""

            )

        )

        text.extend(

            self.profile.get(

                "preferred_roles",

                []

            )

        )

        text.extend(

            self.profile.get(

                "skills",

                []

            )

        )

        text.extend(

            self.profile.get(

                "frameworks",

                []

            )

        )

        text.extend(

            self.profile.get(

                "current_projects",

                []

            )

        )

        return "\n".join(

            map(

                str,

                text

            )

        )