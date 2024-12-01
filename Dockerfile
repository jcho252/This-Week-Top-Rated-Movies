FROM python:3.11.5
WORKDIR /Users/justincho/Downloads/Team30Task3
COPY MovieDictionary.py IMDb_Data.py MovieDb_Data.py ./
RUN pip install requests
CMD python3 MovieDictionary.py 