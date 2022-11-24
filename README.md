# SeleniumTestTask

How to start tests:

  1. install requirements
  
          pip3 install -r /path/to/requirements.txt

  2. get container with selenium and browser inside 

     + get container for mac M1 (arm)

            docker pull seleniarm/standalone-chromium

     + get container for x64arch

            docker pull selenium/standalone-chrome

  3. start docker container

          docker run -d -p 4444:4444 -v /dev/shm:/dev/shm <container_name>

  4. start tests!

          python3 -m pytest /path/to/tests
 
