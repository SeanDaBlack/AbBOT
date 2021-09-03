// Copyright (c) 2019 Edwin Pratt
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

class Markov {
  constructor (type = 'text') {
    // The type of values
    if (type === 'text') {
      this.type = type
    } else if (type === 'numeric') {
      this.type = type
    } else {
      throw new Error(
        'The Markov Chain can only accept the following types: numeric or text'
      )
    }

    // This is an array that will hold all of our states
    this.states = []

    // This is an object which will contain a list of each possible outcome
    this.possibilities = {}

    // This variable holds the order
    this.order = 3

    if (this.type === 'text') {
      // This array will keep track of all the possible ways to start a sentence
      this.start = []
    }
  }

  // Add a single state or states
  addStates (state) {
    if (Array.isArray(state)) {
      this.states = Array.from(state)
    } else {
      this.states.push(state)
    }
  }

  // Clear the Markov Chain completely
  clearChain () {
    this.states = []

    if (this.type === 'text') {
      this.start = []
    }

    this.possibilities = {}
    this.order = 3
  }

  // Clear the states
  clearState () {
    this.states = []

    if (this.type === 'text') {
      this.start = []
    }
  }

  // Clear the possibilities
  clearPossibilities () {
    this.possibilities = {}
  }

  // Get the states
  getStates () {
    return this.states
  }

  // Set the order
  setOrder (order = 3) {
    if (typeof order !== 'number') {
      console.error('Markov.setOrder: Order is not a number. Defaulting to 3.')
      order = 3
    }

    if (order <= 0) {
      console.error(
        'Markov.setOrder: Order is not a positive number. Defaulting to 3.'
      )
    }

    if (this.type === 'numeric') {
      console.warn(
        'The Markov Chain only accepts numerical data. Therefore, the order does not get used.\nThe order may be used by you to simulate an ID for the Markov Chain if required'
      )
    }

    this.order = order
  }

  // Get the order
  getOrder () {
    if (this.type === 'numeric') {
      console.warn(
        'The Markov Chain only accepts numerical data. Therefore, the order does not get used.\nThe order may be used by you to simulate an ID for the Markov Chain if required'
      )
    }

    return this.order
  }

  // Get the whole list of possibilities or a single possibility
  getPossibilities (possibility) {
    if (possibility) {
      if (this.possibilities[possibility] !== undefined) {
        return this.possibilities[possibility]
      } else {
        throw new Error('There is no such possibility called ' + possibility)
      }
    } else {
      return this.possibilities
    }
  }

  // Train the markov chain
  train (order) {
    this.clearPossibilities()

    if (order) {
      this.order = order
    }

    if (this.type === 'text') {
      for (let i = 0; i < this.states.length; i++) {
        this.start.push(this.states[i].substring(0, this.order))

        for (let j = 0; j <= this.states[i].length - this.order; j++) {
          const gram = this.states[i].substring(j, j + this.order)

          if (!this.possibilities[gram]) {
            this.possibilities[gram] = []
          }

          this.possibilities[gram].push(this.states[i].charAt(j + this.order))
        }
      }
    } else if (this.type === 'numeric') {
      for (let i = 0; i < this.states.length; i++) {
        const { state, predictions } = this.states[i]

        if (!this.possibilities[state]) {
          this.possibilities[state] = []
        }

        this.possibilities[state].push(...predictions)
      }
    }
  }

  // Generate output
  generateRandom (chars = 15) {
    if (this.type === 'text') {
      const startingState = this.random(this.start, 'array')
      let result = startingState
      let current = startingState
      let next = ''

      for (let i = 0; i < chars - this.order; i++) {
        next = this.random(this.possibilities[current], 'array')

        if (!next) {
          break
        }

        result += next
        current = result.substring(result.length - this.order, result.length)
      }

      return result
    } else if (this.type === 'numeric') {
      const possibilities = []

      for (let i = 0; i < chars; ++i) {
        const key = this.random(this.possibilities, 'object')

        if (Math.random() < 0.5) {
          possibilities.push(parseInt(key))
        } else {
          possibilities.push(parseInt(this.predict(key)))
        }
      }

      return possibilities
    }
  }

  // Generate a random value
  random (obj, type) {
    if (Array.isArray(obj) && type === 'array') {
      const index = Math.floor(Math.random() * obj.length)

      return obj[index]
    }

    if (typeof obj === 'object' && type === 'object') {
      const keys = Object.keys(obj)
      const index = Math.floor(Math.random() * keys.length)

      return keys[index]
    }
  }

  // Predict outcome - numeric only (might be a TODO)
  predict (value) {
    if (this.type === 'numeric') {
      if (this.possibilities[value]) {
        return this.random(this.possibilities[value], 'array')
      } else {
        console.error('The markov chain could not find a possibility')
      }
    } else {
      throw new Error(
        'The predict function only works with numerical values - for now'
      )
    }
  }

  getType () {
    return this.type
  }

  setType (type = 'text') {
    if (type === 'text' || type === 'numeric') {
      this.clearChain()
      this.type = type
    } else {
      throw new Error('Invalid type: ' + type)
    }
  }
}

export default Markov;