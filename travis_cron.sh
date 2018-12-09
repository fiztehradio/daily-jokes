git checkout master

# Take random like from jokes file
sort --random-sort daily_jokes.txt | head -1 | cat> joke.txt
git add .
git commit -m "refresh joke"
git push --force --quiet "https://$GITHUB_TOKEN@github.com/fiztehradio/daily-jokes.git" master:master
