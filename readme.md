# Portfolio Generator

### Setup
```
$ git clone https://github.com/khanh2907/portfolio_generator.git
$ sudo pip install yattag
```

### Generate portfolio
In the `portfolio.yml` file enter your details and projects. Use the following format.

```
Projects:
  <project id>:
    name: <string>
    friendly_name: <string>
    organisation: <string>
    type: <work|uni|personal|hackathon>
    descriptions:
      - <string>
      - ...
      - - <string>
    technologies:
      - <string>
      - ...
      - - <string>
    urls:
      - <string url>
      - ...
      - - <string url>
    images:
      - <path/to/image>
      - ...
      - <path/to/image>
    video_embed: <video embed html>
```

Then run:
```
$ python portfolio.py > index.html
```

Your portfolio should be generated in `index.html`. Note that the paths are relative, you'll have to match any resources(images, css, etc) appropriately.

###Example Configuration YAML
```
Projects:
  0:
    name: Intersect DIVER / HIEv
    friendly_name: dc21
    organisation: Intersect Australia
    type: work
    descriptions:
      - "Intersect DIVER (Data Is Vital for Empirical Research) is a general purpose open source research data capture and sharing application. When deployed as part of an Intersect 'AAAA' data management implementation project, Intersect DIVER provides a full lifecycle research data management solution out-of-the-box."
      - "Intersect has begun reusing software based on the DC21 (HIEv) project developed for the University of Western Sydney (UWS). DIVER (Data Is Valuable for Empirical Research), is using the DC21 (HIEv) software for Macquarie University's Faculty of Business and Economics."
      - "I have been apart of the DC21 project for a long time starting as a tester(QA). When I became a developer, I was put on this project. I did a variety of things from front-end or back-end to automated tests."
    technologies:
      - Ruby on Rails
      - PostgreSQL
      - Redis
      - Resque
      - Rspec
      - Capybara
      - Cucumber
      - Selenium
      - Ansible
      - jQuery
    urls:
      - 'https://github.com/IntersectAustralia/dc21'
      - 'http://intersect.org.au/content/intersect-diver'

  1:
    name: RICS LEASA
    friendly_name: rics
    organisation: Intersect Australia
    type: work
    descriptions:
      - "The Leasa App has a number of tools which help office tenants to make decisions about their existing office space and the spaces they may wish to lease."
    technologies:
      - Ruby on Rails
      - PostgreSQL
      - iOS
      - Android
      - jQuery
      - Twitter Bootstrap 2
      - Rspec
      - Capybara
      - Cucumber
      - Selenium
      - jQuery
    urls:
      - 'http://www.rics.org/au/footer/choosing-and-managing-an-energy-efficient-space/'
      - 'https://itunes.apple.com/au/app/leasa/id647127739?mt=8'
      - 'https://leasa.rics.org/'
      - 'https://play.google.com/store/apps/details?id=au.org.rics.leasa.android'
    images:
      - 'images/leasa1.png'
      - 'images/leasa2.png'
      - 'images/leasa3.png'
```
