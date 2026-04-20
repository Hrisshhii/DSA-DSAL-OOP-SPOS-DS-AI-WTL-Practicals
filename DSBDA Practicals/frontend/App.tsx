/* eslint-disable @typescript-eslint/no-explicit-any */
import { useState } from "react";
import Card from "./components/Card";
import RecentMovies from "./components/RecentMovies";
import HighestRated from "./components/HighestRated";
import MovieModal from "./components/MovieModal";
import TrendingMovies from "./components/TrendingMovies";

type Movie = {
  title: string;
  poster: string;
  overview: string;
  rating?: number;
  year?: string;
};

function App() {
  const [movie,setMovie]=useState("");
  const [loading,setLoading]=useState(false);
  const [error,setError]=useState("");
  const [results, setResults] = useState<Movie[]>([]);
  const [selectedMovie, setSelectedMovie] = useState<Movie | null>(null);

  const getRecommendations=async ()=>{
    if (!movie) return;

    setLoading(true);
    setError("");
    setResults([]);

    try{
      const res=await fetch(`http://127.0.0.1:5000/recommend?movie=${movie}`);
      const data=await res.json();

      if (data.error){
        setError(data.error);
      }else{
        setResults(data.recommendations);
      }
    }catch(err){
      setError("Server error. Is backend running?");
      console.error(err);
    }

    setLoading(false);
  };

  const onkeydown=(e:any)=>{
    if(e.key==="Enter") getRecommendations();
  }

  return(
    <div className="min-h-screen bg-linear-to-br from-black via-gray-900 to-black text-white p-10">
      <div className="mx-auto">
        <h1 className="text-5xl md:text-6xl font-extrabold mb-10 text-center tracking-tight bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">
          🎬 Movie Recommender
        </h1>

        {/* Input Section */}
        <div className="flex justify-center gap-3 mb-12">
          <input type="text" placeholder="Search movies..." value={movie} onKeyDown={onkeydown} onChange={(e) => setMovie(e.target.value)}
            className="px-5 py-3 w-72 md:w-96 rounded-xl bg-gray-900/70 backdrop-blur border border-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
          />

          <button onClick={getRecommendations} className="bg-blue-500 px-6 py-3 rounded-xl hover:bg-blue-600 transition transform hover:scale-105">
            Recommend
          </button>
        </div>

        {loading && <p className="text-gray-400">Loading...</p>}
        {error && <p className="text-red-400">{error}</p>}

        {/* Results */}
        <div className="grid grid-cols-2 md:grid-cols-8 gap-6 mt-6">
          {results.map((movie, index) => (
            <Card key={index} movie={movie} onClick={()=>setSelectedMovie(movie)}/>
          ))}
        </div>

        <TrendingMovies onSelect={setSelectedMovie}/>
        <RecentMovies onSelect={setSelectedMovie}/>
        <HighestRated onSelect={setSelectedMovie}/>
      </div>
      

      <MovieModal movie={selectedMovie} onClose={()=>setSelectedMovie(null)}/>
    </div>
  );
}

export default App;
