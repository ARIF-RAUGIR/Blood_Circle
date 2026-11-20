# BloodCircle

A blood donation web platform that connects patients with nearby volunteer donors. Donors register once, and the site keeps track of who is available to give blood right now.

## Features

- **Account for everyone**: sign up with name, email, phone and password. Donor details are optional.
- **Become a donor any time**: add blood group, gender, location, last donation date and a photo. Edit the profile later.
- **Automatic availability**: after a donation a donor shows as unavailable for 3 months (4 months for women), then returns to the list on their own.
- **Donor search**: filter by blood group, district (all 64) and area.
- **Nearby donors**: use your current location to see how far each donor is, and limit results to a radius.
- **Location from address**: donors who skip the GPS button get a location from their address using OpenStreetMap, with checks that reject wrong matches.
- **Urgent blood requests**: logged-in users post a request that appears on the home page until it is marked fulfilled.
- **Privacy**: donor phone numbers are only shown to logged-in users, and exact coordinates are never displayed.
- **Responsive red and white UI** with scroll animations and toast notifications.

## Tech stack

| Area | Tools |
|------|-------|
| Backend | Python, Django, SQLite |
| Frontend | HTML, Tailwind CSS (CDN), JavaScript, Motion |
| Other | Browser Geolocation API, OpenStreetMap Nominatim, Pillow |
