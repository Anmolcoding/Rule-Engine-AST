# MongoDB Setup for Rule Engine

1. **Local MongoDB Setup:**
   - Download and install MongoDB from [here](https://www.mongodb.com/try/download/community).
   - Start MongoDB with the `mongod` command.
   - Connect using `mongo` shell or through your application.

2. **MongoDB Atlas (Cloud) Setup:**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
   - Create a free cluster.
   - Get the connection URI and replace it in `app.py`.

3. **MongoDB Collection:**
   - Database: `rule_engine_db`
   - Collection: `rules`
