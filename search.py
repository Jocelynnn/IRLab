import json
import time
import metapy
import os
import sys


if __name__ == '__main__':
    if len(sys.argv) != 4 :
        print("Usage: python {} config.toml query ranker_id".format(sys.argv[0]))
        sys.exit(1)

    _cfg = sys.argv[1]
    _query = sys.argv[2]
    _ranker_id = sys.argv[3]

    # metapy.log_to_stderr()
    idx = metapy.index.make_inverted_index(_cfg)

    start = time.time()
    query = metapy.index.Document()
    query.content(_query)
    ranker_id = _ranker_id
    try:
        ranker = getattr(metapy.index, ranker_id)()
    except:
        print("Couldn't make '{}' ranker, using default.".format(ranker_id))
        ranker = metapy.index.OkapiBM25()
    response = {'query': _query, 'results': []}
    top_docs = ranker.score(idx, query, num_results=10)

    for num, (d_id, score) in enumerate(top_docs):
        content = idx.metadata(d_id).get('content')
        path = idx.metadata(d_id).get('path')
        # print(content)
        f_content = "{}.{}...\n".format(num + 1,content[0:50])
        response['results'].append({
            'score': float(score),
            'content': content[0:50],
            'path': path,
        })
    response['elapsed_time'] = time.time() - start
    print(json.dumps(response, indent=2))
