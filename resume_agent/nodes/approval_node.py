def approval_node(state):
   
    approved_jobs = []

    for job, score in state[

            "ranked_jobs"

    ]:

        print()

        print(

            "="*80

        )

        print(

            job.company

        )

        print(

            job.title

        )

        print(

            round(

                score,

                3

            )

        )

        answer = input(

            "Apply? (y/n): "

        )

        if answer.lower() == "y":

            approved_jobs.append(

                (

                    job,

                    score

                )

            )

    return {

        "approved_jobs":

        approved_jobs

    }