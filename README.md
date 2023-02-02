# Youtube-Video-Scrapper
Scrapes youtube links off of youtube homepage in array and randomly opens a link fromt he array in brower. 

# Motivation
- Over the summer of 2022, as a side to my formal internship responsibilities, I along with a group of 3 other interns were tasked with proposing a product which would directly address workplace mental wellness. We decided that we would code an application which reminds workers to take frequent breaks between there task in order to boost their efficiency and prevent burnout

# Scrapper
- My task was to create function which opened a random youtube link from a specified youtube home page so that when the timer elapsed a pop-up would mention to the worker to take a break and a relaxing video would pop up in his browser
- My intuition was that the link to a youtube video has to be stored somewhere on a youtube page, as us users are able to click the video thumbnail to be routed to a link
- Knowing that web-pages are typically in the HTML language, I used the BeutifulSoup library to parse the web-page information, specifically search for identifiers which preceded the youtube links
- Per each link I found on the youtube webpage, I stored the link in an aray and randoml opened one of the links after all the links had been compiled


# Constraints
- Our team had one month to complete this project
- Each person was only allowed to work 16 hours for the entire project (including wrapping up there modules and presentation preparation)
