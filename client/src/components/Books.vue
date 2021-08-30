<template>
    <div class="container">
         <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Book</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{book.title}}</td>
              <td>{{book.author}}</td>
              <td>
                  <span v-if="book.read">Yes</span>
                  <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    </div>
</template>


<script>
 import axios from 'axios'

export default {
   data() {
       return {
           books: [],
           addBookForm: {
               title: '',
               author: '',
               read:[],
           }
       };
   },
   methods: {
       getBooks() {
           const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
       },
       addBook(payload) {
        const path = 'http://localhost:5000/books';
        axios.post(path, payload)
        .then(() => {
          //bad practice
          this.getBooks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
       },
       initForm() {
           this.addBookForm.title = ''
           this.addBookForm.author = ''
           this.addBookForm.read = []
       },
       onSubmit(event) {
           event.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
       },
       onReset(evt) {
        evt.preventDefault();
        this.$refs.addBookModal.hide();
        this.initForm();
       }
   },
   created() {
       this.getBooks()
   }
}

</script>


<style lang="">
    
</style>