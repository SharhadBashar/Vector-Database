def print_query(query, data):
    return {'input': data.title(),
            'match 1': '{} || Score: {}'.format(query['matches'][0]['id'].title(), round(query['matches'][0]['score'], 2)),
            'match 2': '{} || Score: {}'.format(query['matches'][1]['id'].title(), round(query['matches'][1]['score'], 2)),
            'match 3': '{} || Score: {}'.format(query['matches'][2]['id'].title(), round(query['matches'][2]['score'], 2)),
            'match 4': '{} || Score: {}'.format(query['matches'][3]['id'].title(), round(query['matches'][3]['score'], 2)),
            'match 5': '{} || Score: {}'.format(query['matches'][4]['id'].title(), round(query['matches'][4]['score'], 2)),
        }