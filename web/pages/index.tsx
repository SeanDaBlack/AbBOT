import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Pro-choice Texas Today</title>
        <meta name="description" content="Fighting for Texas" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Welcome to Pro Choice Texas Today!</h1>

        <p className={styles.description}>
          Check out our{' '}
          <a href="https://github.com/SeanDaBlack/AbBOT" rel="noreferrer" target="_blank">
            Github
          </a>
        </p>
      </main>

      <footer className={styles.footer}></footer>
    </div>
  )
}

export default Home
