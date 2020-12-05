def split(people):
    # Get total owed for each person
    tot_owed = 0.0
    for person, value in people:
        tot_owed += value
    tot_owed /= len(people)

    # Who should send to who
    send_to_who = []

    # Mark start and end in list
    start = 0
    end = len(people)-1

    owed = tot_owed-people[start][1]
    diff = people[end][1]-tot_owed

    # Pay off everyone
    while(start < end):
        # Need to keep paying off end but start is paid off
        if(diff-owed >= 0):
            send_to_who.append(
                (people[start][0], people[end][0], owed)
            )
            diff -= owed
            start += 1
            owed = tot_owed-people[start][1]
        # End is payed off but still have money at start
        else:
            send_to_who.append(
                (people[start][0], people[end][0], diff)
            )
            owed -= diff
            end -= 1
            diff = people[end][1]-tot_owed
    return send_to_who


def start(people):
    # Sort based on val
    people = sorted(people, key=lambda val: val[1])

    # Get how much each person should pay
    return split(people)
