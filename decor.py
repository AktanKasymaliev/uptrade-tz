import time
import functools
import logging

from django.db import connection, reset_queries


log = logging.getLogger("django")


def debug_db_queries(func):
    """
    Decorate a function to log all queries executed.
    logs:
        - Execution time
        - Number of queries
    We should forget about small efficiencies, say about 97% of the time:
    premature optimization is the root of all evil. Yet we should not pass
    up our opportunities in that critical 3%.
    - D. Knuth (justifying the use of GOTO statements, 1974)
    Will show the reducing number and execution time of total queries
        - select_related:
            When the object we are going to select is a single object,
            used on ForeignKey fields and OneToOne fields.
            Select related does an INNER JOIN on the related table in SQL.
            -> Model.objects.all().select_related('fk_field_name')  # order of filters is not important
            https://docs.djangoproject.com/en/dev/ref/models/querysets/#select-related
        - prefetch_related:
            When the object we are going to select is a list of objects,
            used on ManyToMany fields.
            Prefetch related does a seperate lookup for each relationship.
                1. 'normal' SELECT ..
                2. SELECT WHERE "related_model"."id" IN (<list of ids in the first query>)
            Then it performs the joining in Python.
            -> Model.objects.all().prefetch_related('m2m_field_name')
            https://docs.djangoproject.com/en/dev/ref/models/querysets/#prefetch-related
    Thanks to: https://betterprogramming.pub/django-select-related-and-prefetch-related-f23043fd635d
    Example usage ("emulating a template evaluation"):
        @debug_db_queries
        def get_items_select():
            queryset = Item.objects.all().select_related('owner', 'fk_relation')
            return [ {'id': item.id, 'fk': item.fk_relation, 'owner': item.owner} for item in queryset ]
    """

    @functools.wraps(func)
    def inner_func(*args, **kwargs):

        # reset all django.db.connection.queries
        reset_queries()

        start_queries = len(connection.queries)
        start_time = time.perf_counter()

        result = func(*args, **kwargs)
        # total_queries_execution_time => sum([float(q['time']) for q in connection.queries])

        end_time = time.perf_counter()
        end_queries = len(connection.queries)

        queries = end_queries - start_queries
        time_taken = end_time - start_time

        log.info(f">>> DEBUG QUERY - Function : {func.__name__}")
        log.info(f">>> DEBUG QUERY - Number of Queries : {queries}")
        log.info(f">>> DEBUG QUERY - Finished in : {(time_taken):.2f}s")
        return result

    return inner_func