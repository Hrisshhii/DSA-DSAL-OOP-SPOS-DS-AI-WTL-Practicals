type Movie={
  title: string;
  poster: string;
  overview: string;
};

type Props={
  movie: Movie | null;
  onClose: () => void;
};

const IMAGE_BASE = "https://image.tmdb.org/t/p/w500";

export default function MovieModal({ movie, onClose }: Props) {
  if (!movie) return null;

  return (
    <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex justify-center items-center z-50">
      <div className="bg-gray-900/80 backdrop-blur-xl p-6 rounded-2xl max-w-lg w-full relative shadow-2xl animate-fadeIn">
        <button onClick={onClose} className="absolute top-1 right-2 text-gray-700 hover:text-gray-500 text-5xl cursor-pointer">
          &times;
        </button>
        <img src={IMAGE_BASE + movie.poster} className="w-full h-full object-cover rounded-lg mb-4" />
        <h2 className="text-2xl font-bold mb-2">{movie.title}</h2>
        <p className="text-gray-300 text-sm">
          {movie.overview}
        </p>
      </div>
    </div>
  );
}