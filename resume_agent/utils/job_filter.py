HIGH_PRIORITY = [
"data scientist",
"senior data scientist",
"applied scientist",
"research scientist",

"machine learning engineer",
"ml engineer",

"ai engineer",
"genai engineer",
"llm engineer",

"generative ai",
"agentic ai"
]

MEDIUM_PRIORITY = [

"rag",
"langchain",
"langgraph",

"pytorch",
"transformers",

"nlp",
"semantic search",

"computer vision",
"yolo",

"huggingface"

]

NEGATIVE_KEYWORDS = [

"frontend",

"react",

"rails",

"ruby",

"ios",

"android",

"mobile",

"php",

"wordpress",

"devops",

"qa",

"test automation",

"video editor",

"writing specialist",

"customer operations"
]

def filter_jobs(jobs):

    filtered = []

    for job in jobs:

        text = (

            f"{job.title} "

            f"{job.jd}"

        ).lower()

        if any(

                word in text

                for word in NEGATIVE_KEYWORDS

        ):

            continue

        score = 0

        for keyword in HIGH_PRIORITY:

            if keyword in text:

                score += 5

        for keyword in MEDIUM_PRIORITY:

            if keyword in text:

                score += 2

        if score >= 5:

            filtered.append(

                job

            )

    return filtered