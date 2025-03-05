<script setup>
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex'
import { useRouter, useRoute } from 'vue-router'
import CreatePostDialog from '@/components/dialogs/CreatePostDialog.vue'

const store = useStore()
const router = useRouter()
const route = useRoute()

const isLoggedIn = computed(() => store.state.user.isLoggedIn)

// 当前选中的板块
const currentSection = ref('all')

// 所有板块的配置
const sections = [
  // 筛选类板块（使用默认颜色）
  {
    id: 'all',
    name: '全部主题',
    icon: 'mdi mdi-format-list-bulleted',
    isFilter: true
  },
  // {
  //   id: 'history',
  //   name: '历史话题',
  //   icon: 'mdi mdi-history',
  //   isFilter: true
  // },
  // {
  //   id: 'following',
  //   name: '我的关注',
  //   icon: 'mdi mdi-star-outline',
  //   isFilter: true,
  //   requireLogin: true
  // },
  // 特色板块（使用自定义颜色）
  {
    id: 'announcement',
    name: '公告',
    icon: 'mdi mdi-bullhorn-outline',
    color: '#FF4D4F',
  },
  {
    id: 'featured',
    name: '精华',
    icon: 'mdi mdi-crown-outline',
    color: '#722ED1',
  },
  {
    id: 'study',
    name: '学习',
    icon: 'mdi mdi-school-outline',
    color: '#FADB14',
  },
  {
    id: 'life',
    name: '生活',
    icon: 'mdi mdi-coffee-outline',
    color: '#52C41A',
  },
  {
    id: 'lost',
    name: '拾遗',
    icon: 'mdi mdi-package-variant',
    color: '#13C2C2',
  },
  {
    id: 'confession',
    name: '表白墙',
    icon: 'mdi mdi-heart-outline',
    color: '#FF85C0',
  }
]

// 处理板块点击
async function handleSectionClick (sectionId) {
  const section = sections.find(s => s.id === sectionId)
  if (section?.requireLogin && !isLoggedIn.value) {
    alert('请先登录')
    return
  }

  // 更新 Vuex 中的 currentSection
  await store.dispatch('section/updateCurrentSection', sectionId);

  currentSection.value = sectionId
  
  router.push({ 
    query: { section: sectionId }
  })
  
  if (section?.isFilter) {
    // 筛选类板块使用默认主题色和描述
    store.commit('theme/setThemeColor', '#1890FF')
    store.commit('theme/setWelcomeMessage', '欢迎来到论坛')
    store.commit('theme/setSectionDescription', '在这里，你可以与同学们交流、分享和探讨各种话题')
  } else if (section) {
    // 特色板块使用自定义颜色和描述
    store.commit('theme/setThemeColor', section.color)
    store.commit('theme/setWelcomeMessage', `欢迎来到${section.name}板块`)
    
    // 根据不同板块设置不同的描述文字
    let description = '在这里，你可以与同学们交流、分享和探讨各种话题'
    switch(section.id) {
      case 'confession':
        description = '在这里，你可以向同学们表达自己的心意'
        break
      case 'study':
        description = '在这里，你可以与同学们交流学习经验、分享学习资料'
        break
      case 'life':
        description = '在这里，你可以分享校园生活、结交志同道合的朋友'
        break
      case 'lost':
        description = '在这里，你可以发布寻物启事、帮助失主找回失物'
        break
      case 'announcement':
        description = '在这里，你可以了解学校的最新通知和重要信息'
        break
      case 'featured':
        description = '在这里，你可以浏览精选的优质内容和热门话题'
        break
    }
    store.commit('theme/setSectionDescription', description)
  }
}

const handleClick = () => {
  if (!isLoggedIn.value) {
    alert('请先登录后再发布主题。')
  }
}

// 组件挂载时初始化状态
onMounted(() => {
  handleSectionClick('all')
})

const isCreatePostDialogVisible = ref(false)

const showCreatePostDialog = () => {
  isCreatePostDialogVisible.value = true
}

const closeCreatePostDialog = () => {
  isCreatePostDialogVisible.value = false
}
</script>

<template>
  <aside class="sidebar">
    <!-- 发布主题按钮 -->
    <button v-if="isLoggedIn" class="new-topic-btn" @click="showCreatePostDialog">
      发布主题
    </button>
    <button v-else class="new-topic-btn" @click="handleClick">
      发布主题
    </button>

    <!-- 筛选导航 -->
    <nav class="sidebar-nav">
      <!-- <h3>筛选</h3> -->
      <ul>
        <li 
          v-for="section in sections.filter(s => s.isFilter)"
          :key="section.id"
          @click="handleSectionClick(section.id)"
        >
          <a 
            href="#" 
            :class="['section-link', { 
              'active': currentSection === section.id
            }]"
            :style="currentSection === section.id ? 
              { '--active-color': '#1890FF' } : {}"
          >
            <div class="section-icon">
              <i :class="section.icon" :style="{ color: '#666' }"></i>
            </div>
            <span>{{ section.name }}</span>
          </a>
        </li>
      </ul>
    </nav>

    <!-- 板块导航 -->
    <nav class="sidebar-nav">
      <!-- <h3>板块</h3> -->
      <ul>
        <li 
          v-for="section in sections.filter(s => !s.isFilter)"
          :key="section.id"
          @click="handleSectionClick(section.id)"
        >
          <a 
            href="#" 
            :class="['section-link', { 
              'active': currentSection === section.id
            }]"
            :style="currentSection === section.id ? 
              { '--active-color': section.color } : {}"
          >
            <div class="section-icon">
              <i :class="section.icon" :style="{ color: section.color }"></i>
            </div>
            <span>{{ section.name }}</span>
          </a>
        </li>
      </ul>
    </nav>
  </aside>

  <CreatePostDialog v-if="isCreatePostDialogVisible" @close="closeCreatePostDialog" />
</template>

<style scoped>
.sidebar {
  width: 200px;
  padding: 0 20px;
  background-color: #fff;
  flex-shrink: 0;
}

.new-topic-btn {
  width: 100%;
  padding: 10px;
  height: 40px;
  line-height: 20px;
  background-color: var(--primary-color);
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  margin: 20px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s;
}

.sidebar-nav h3 {
  font-size: 1rem;
  color: var(--text-color);
  margin-bottom: 10px;
}

.sidebar-nav ul {
  list-style-type: none;
  padding: 0;
}

.sidebar-nav li {
  margin-bottom: 10px;
}

.section-link {
  color: var(--text-color);
  text-decoration: none;
  display: flex;
  align-items: center;
  padding: 8px;
  border-radius: 6px;
  transition: all 0.3s;
}

.section-link:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.section-link.active {
  color: var(--active-color);
  background-color: rgba(var(--active-color-rgb), 0.1);
}

.section-link.active i {
  color: var(--active-color) !important;
}

.section-icon {
  position: relative;
  width: 24px;
  height: 24px;
  margin-right: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.section-icon i {
  font-size: 1.4em;
  transition: color 0.3s;
}

/* 为了视觉分隔，给第二个导航添加上边距 */
.sidebar-nav + .sidebar-nav {
  margin-top: 24px;
}
</style>
