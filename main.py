from booking.booking import  Booking


with Booking() as bot:
    bot.land_first_page()
    bot.close_pop()
    bot.close_google_signup_popup()
   # bot.choose_currency()
    bot.select_place_to_go('New York')
    bot.select_dates('2024-11-23','2024-12-23')
    bot.number_persons_room(3)
    bot.search_item()
    bot.apply_filtrations()



