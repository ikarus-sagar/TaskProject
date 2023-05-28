import React, { useState, useEffect } from 'react';
import './App.css';
function App() {
  const [users, setUsers] = useState([
    { id: 1, name: 'Loading...', email: 'Loading...' },
  ]);
  const [blogs, setBlogs] = useState([
    { id: 1, title: 'Loading...', content: 'Loading...' },
  ]);

  useEffect(() => {
    fetch('/user')
      .then(response => response.json())
      .then(data => setUsers(data));
    fetch('/blog')
      .then(response => response.json())
      .then(data => setBlogs(data));
  }, []);

  return (
    <div className='App'>
      <div className='main'>
        <h1 className='heads'>Users</h1>
          {users.map(user => (
            <div className='content' key={user.id}>
              <div>Name : {user.name}</div>
              <div>Email : {user.email}</div>
            </div>
          ))}
      </div>
      <div className='main'>
        <h1 className='heads'>Blogs</h1>
          {blogs.map(blog => (
            <div className='content' key={blog.id}>
              <div>Title : {blog.title}</div>
              <div>Content : {blog.content}</div>
              <div>Author : {blog.creator}</div>
            </div>
          ))}
      </div>
    </div>
  );
}

export default App;
