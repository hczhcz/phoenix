Phoenix
=======

Project Database System for Science Education

Put data under `data/` and edit `redo.py`

Example data (from Intel ISEF) see the committing history

Init

    redo.InitDatabase()

Query

    q = tool_read.Query()

    q.SelectByStr('data["Field"] == "CS"')
    # ID Field Title IsTeam Member School Abstract Keyword
    # IsRelated Related IsAwarded Award
    q.SelectByStr('data["???"] == ???')

    print q.Count()
    print q.PrintToString()
    q.PrintToFile('result.txt')

    # More ...
    q.EvalByStr('???')
    q.IterateByStr('???')
    q.SplitByStr('???')

    mq = tool_read.MultiQuery()

    mq.SelectByStr('data["???"] == ???')
    # IsAwarded CoveredAward CoveredMember MemberChanged FieldChanged
    mq.SelectByStr('summary["???"] == ???')
