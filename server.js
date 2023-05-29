const express = require('express');
const app = express();
require('dotenv').config();


const mongodburl = process.env.MONGODB_URL+"blogging";
const mongoose = require('mongoose');

mongoose.connect(mongodburl, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB!'))
  .catch(err => console.error('Something went wrong', err));

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

const blogSchema = new mongoose.Schema({
    id: String,
  title: String,
  content: String,
  creator: String,
});

const userSchema = new mongoose.Schema({
    id: String,
  name: String,
  email: String,
  password: String
});

const Blog = mongoose.model('Blog', blogSchema);
const User = mongoose.model('User', userSchema);

app.use(express.json());

app.get('/blogs', async (req, res) => {
    try {
        const blogs = await Blog.find();
        // console.log(blogs);
        res.json(
            blogs.map(blog => {
                return {
                    id: blog.id,
                    title: blog.title,
                    content: blog.content,
                    creator: blog.creator
                }
            })
        )
    }
    catch (error) {
        console.error('Error fetching blogs:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.get('/users', async (req, res) => {
  try {
    const users = await User.find();
    res.json(
        users.map(user => {
            return {
                id: user.id,
                name: user.name,
                email: user.email,
                password: user.password
            }
        })
    );
  } catch (error) {
    console.error('Error fetching users:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

const port = 3000;
app.listen(port, () => console.log(`App listening on port ${port}!`));