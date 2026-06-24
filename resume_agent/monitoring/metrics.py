from prometheus_client import Counter, Histogram, Summary, start_http_server

# Counters for tracking events
JOBS_SEARCHED = Counter(
    'resume_agent_jobs_searched_total',
    'Total number of jobs searched',
    ['source']
)

JOBS_APPLIED = Counter(
    'resume_agent_jobs_applied_total',
    'Total number of jobs applied to',
    ['source', 'status']
)

# Histograms for tracking duration
PROCESSING_TIME = Histogram(
    'resume_agent_processing_seconds',
    'Time spent processing a job',
    ['stage']
)

# Summary for tracking latency
LLM_LATENCY = Summary(
    'resume_agent_llm_latency_seconds',
    'Latency of LLM calls'
)

def start_metrics_server(port=8000):
    """Starts the Prometheus metrics server."""
    try:
        start_http_server(port)
        return True
    except Exception:
        return False
