# Print second half of spell list
spell_list = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"]
mid = int(len(spell_list)/2)
end = len(spell_list)
for day in range(mid, end):
    print(spell_list[day])
