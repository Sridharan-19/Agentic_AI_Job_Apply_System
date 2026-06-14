from langgraph.graph import StateGraph

from resume_agent.state.career_state import (
CareerState
)

from resume_agent.nodes.search_node import (
search_node
)

from resume_agent.nodes.rank_node import (
rank_node
)

from resume_agent.nodes.approval_node import (
approval_node
)

from resume_agent.nodes.tailor_node import (
tailor_node
)

from resume_agent.nodes.apply_node import (
apply_node
)

from resume_agent.nodes.tracker_node import (
tracker_node)

builder = StateGraph(


CareerState


)

builder.add_node(


"search",

search_node


)

builder.add_node(


"rank",

rank_node


)

builder.add_node(


"approval",

approval_node


)

builder.add_node(


"tailor",

tailor_node


)

builder.add_node(


"apply",

apply_node


)

builder.add_node(


"tracker",

tracker_node


)

builder.set_entry_point(


"search"


)

builder.add_edge(


"search",

"rank"


)

builder.add_edge(


"rank",

"approval"


)

builder.add_edge(


"approval",

"tailor"


)

builder.add_edge(


"tailor",

"apply"


)

builder.add_edge(


"apply",

"tracker"


)

graph = builder.compile()
