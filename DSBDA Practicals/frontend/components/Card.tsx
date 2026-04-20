type Movie = {
  title: string;
  poster: string;
  overview: string;
  rating?: number;
  year?: string;
};

type Props = {
  movie: Movie;
  onClick: () => void;
};

const IMAGE_BASE = "https://image.tmdb.org/t/p/w500";

export default function Card({ movie, onClick }: Props) {
  return (
    <div onClick={onClick} className="cursor-pointer bg-gray-800 rounded-xl overflow-hidden shadow-lg hover:scale-105 transition">
      <img src={IMAGE_BASE + movie.poster} alt={movie.title} className="w-full object-cover"/>

      <div className="p-3">
        <h2 className="text-sm font-semibold text-center">
          {movie.title}
        </h2>
      </div>
    </div>
  );
}
