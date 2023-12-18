from mrjob.job import MRJob
from mrjob.step import MRStep
import statistics

class MovieRatings(MRJob):
  def steps(self):
    return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_average_ratings)
    ]

  def mapper_get_ratings(self,_,line):
    (userID,movieID,rating,timestamp)=line.split('\t')
    yield movieID, int(rating)

  def reducer_average_ratings(self,key,values):
    yield key, statistics.mean(values)


if __name__ == '__main__':
  MovieRatings.run()
