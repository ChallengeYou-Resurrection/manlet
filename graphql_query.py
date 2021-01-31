
level_count = """
    query {
        levelCount
    }
"""

search_levels = """
    query searchLevels($query: String, $page: Int, $pageSize: Int) {
        searchLevels(query:$query, page:$page, pageSize:$pageSize) {
            title, author, plays
        } 
    }
"""

get_level = """
    query getLevel($gameNumber: Int) {
            getLevel(gameNumber:$gameNumber) {
                title, author, plays
        }
    }
"""