from resume_agent.agents.screening_question_agent import (
    ScreeningQuestionAgent
)

agent = (

    ScreeningQuestionAgent()

)

question = (

    "Describe your experience with Generative AI."
)

answer = (

    agent.answer_question(

        question

    )

)

print()

print(

    answer

)