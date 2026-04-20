import { useEffect, useState } from "react";
import Card from "./Card";

type Movie = {
  title: string;
  poster: string;
  overview: string;
  rating?: number;
  year?: string;
};

type Props = {
  onSelect: (movie: Movie) => void;
};

export default function RecentMovies({ onSelect }: Props) {
  const [movies, setMovies] = useState<Movie[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/recent")
      .then((res) => res.json())
      .then((data) => setMovies(data));
  }, []);

  return (
    <div className="mt-12 w-full">
      <h2 className="text-2xl font-bold mb-4">🔥 Recent Movies</h2>

      <div className="flex gap-4 overflow-x-auto pb-4">
        {movies.map((movie, index) => (
          <div key={index} className="min-w-55">
            <Card movie={movie} onClick={()=>onSelect(movie)} />
          </div>
        ))}
      </div>
    </div>
  );
}