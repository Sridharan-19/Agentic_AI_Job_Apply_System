import yaml

class ProfileBuilder:

    def __init__(

            self,

            yaml_path=

            "resume_agent/profile/profile.yaml"

    ):

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