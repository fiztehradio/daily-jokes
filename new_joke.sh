git pull
sort --random-sort daily_jokes.txt | head -1 | cat> joke.txt
git add .
git commit -m "refresh joke"
git push
