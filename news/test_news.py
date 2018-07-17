import news

def test_get_sources():
	srcs = news.get_sources()
	assert(srcs['status'] == 'ok')
