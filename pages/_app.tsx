import '../styles/globals.css'
import { ChakraProvider, extendTheme } from '@chakra-ui/react'
import type { AppProps } from 'next/app'
import Nav from '../components/Nav'

const theme = extendTheme({})

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider theme={theme}>
      <Nav />

      <Component {...pageProps} />
    </ChakraProvider>
  )
}
export default MyApp
