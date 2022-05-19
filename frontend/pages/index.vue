<template>
  <div>
    <input
      ref="file"
      hidden
      class="mt-2"
      small
      type="file"
      @change="chooseFile($event)"
    >

    <v-btn
      class="button mt-3"
      outlined
      x-small
      color="grey darken-1"
      :loading="uploading"
      @click="$refs.file.click()"
    >
      Upload Files
      <v-icon x-small right>
        mdi-cloud-upload
      </v-icon>
    </v-btn>
    <div v-if="result">
      {{ result }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexItem',
  data: () => ({
    newFile: null,
    result: ''
  }),
  methods: {
    chooseFile (e) {
      const files = e.target.files || e.dataTransfer.files
      this.newFile = files[0]
      this.uploadFile()
    },
    async uploadFile () {
      const data = new FormData()
      data.append('image', this.newFile)
      try {
        this.result = await this.$axios.$post('/api/user/file-upload', data)
      } catch (error) {
        this.result = error
        console.log(error)
      } finally {
      }
    }
  }
}
</script>
