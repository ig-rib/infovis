<template>
    <v-card
        max-width="400px !important"
        class="week-card" :href="hyperlink" target="_blank">
        <v-layout justify-center class="title-description-layout" column>
            <v-list-item two-line>
              <v-list-item-content class="pa-0"> 
                <div class="week-card-title headline mb-1">{{ titletext }}</div>
                <div class="week-card-description">{{ description }}</div>
              </v-list-item-content>
            </v-list-item>
          </v-layout>
        <v-layout justify-center pt-5 px-4 class="image-layout">
            <v-img class="week-image" :src="require('@/assets/' + img)">
            </v-img>
        </v-layout>
    </v-card>    
</template>

<script>
export default {
    props: {
        titletext: {
            type: String,
            default: 'Not An Assignment'
        },
        description: {
            type: String,
            default: ''
        },
        img: {
            type: String,
            default: ''
        },
        hyperlink: {
            type: String,
            default: ''
        }
    },
    methods: {
        goTo (name) {
            this.$router.push({
                name: name
            })
        }
    },
    computed: {
        // imageSrc () {
        //     const image = require.context('@/assets/', false, /\.png$/)
        //     return image('./' + )
        // }
    }
}
</script>

<style lang="scss">
    @import '@/styles/weekCard.scss';
    .week-card {
        padding: 1% !important;
    }
</style>
