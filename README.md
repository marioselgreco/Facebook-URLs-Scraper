This script does the following:

Uses 50 threads for concurrent scraping.
Adds a pause of 1 second for each URL from the same domain.
Follows all internal URLs within the domain being scraped.
Scrapes from "facebook.com".
Scrapes only for external URLs.
Deletes duplicate URLs before importing them into the file.
Adds all URLs to the "urls.txt" file in the same directory as the script.
Writes URLs to the "urls.txt" file in batches of 1000 to prevent bottlenecks.
