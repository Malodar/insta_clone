import {useState, useEffect} from 'react';
import './App.css';

const BASE_URL = 'http://localhost:8000/'

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch(BASE_URL + 'post/all').then(
      response => {
        const js = response.json();
        console.log(js);
        if (response.ok) {
          return js;
        }
        throw response
      }).then(data => {
      setPosts(data)
    })
    .catch(error => {
      console.log(error);
      alert(error)
    })
  }, [])
  

  return (
    posts
  );
}

export default App;
