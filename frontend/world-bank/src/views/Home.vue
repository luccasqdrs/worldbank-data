<template>
  <div class="home">
    <h1>World Bank Countries Data</h1>
    <p>
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Iusto obcaecati perferendis perspiciatis soluta cumque aspernatur nesciunt nobis necessitatibus id est, repellendus quam. Perferendis necessitatibus cum ratione recusandae minus tenetur error! Lorem ipsum dolor sit, amet consectetur adipisicing elit. Id, quibusdam deserunt.
      Similique, eligendi nostrum neque reprehenderit porro et voluptas ea quod nisi assumenda, ab magni, nemo possimus doloribus. Libero, delectus.
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Odio optio esse qui fuga nemo dolorum, repellat non fugiat omnis harum consequuntur tempora asperiores ad laboriosam, maxime distinctio sit debitis quas?
      </p>
    <Table></Table>
  </div>
</template>

<script>
// @ is an alias to /src
import Table from '@/components/Table.vue'

export default {
  name: 'home',
  components: {
    Table
  }
}
</script>

<style lang="less" scoped>
.home{
  padding-top: 2em
}
</style>
