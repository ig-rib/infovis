<template>
    <v-card
        min-width="350px !important"
        min-height="300px"
        max-width="400px !important"
        class="week-card" @click="goTo(link)">
        <v-layout class="title-description-layout" column>
            <v-list-item two-line>
              <v-list-item-content class="pa-0"> 
                <div class="week-card-title headline mb-1">{{ titletext }}</div>
                <div class="week-card-description">{{ description }}</div>
              </v-list-item-content>
            </v-list-item>
          </v-layout>
        <v-layout pt-5 px-4 class="image-layout">
            {{imageSrc}}
            <v-img class="week-image" :src="require('@/assets/' + img)">
            </v-img>
        </v-layout>
    </v-card>    
</template>

<script>
export default {
    props: {
        link: {
            type: String,
            default: 'home'
        },
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
    .week-card {
        border-radius: 10px !important;
        -webkit-user-select: none; /* Safari */        
        -moz-user-select: none; /* Firefox */
        -ms-user-select: none; /* IE10+/Edge */
        user-select: none; /* Standard */
        .v-ripple__container {
            .v-ripple__animation.v-ripple__animation--visible.v-ripple__animation--in {
                border-radius: 10px !important;
            }
        opacity: 0.1 !important;
        border-radius: 10px !important;
        }
        display: flex;
        padding: 3% 5% 4% 3%;
        flex-direction: column;
        &, &:before {
            border-radius: 10px !important;
        }
    }
    .title-description-layout {
        flex-grow: 0;
    }
    .snippet-title {
        font-weight: 400;
    }
    .snippet-description {
        font-weight: 300;
        margin-bottom: 2%;
        max-width: 100%;
    }
    .image-layout {
        flex-grow: 1;
    }
    .week-image {
        border-radius: 10px;
    }
</style>
