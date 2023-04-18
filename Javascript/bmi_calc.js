function bmi(weight, height) {
    var fat = weight / (height**2)
    if (fat <= 18.5) {
      return "Underweight"
    } else if (fat <= 25.0) {
      return "Normal"
    } else if (fat <= 30) {
      return "Overweight"
    } else {
      return "Obese"
    }
  }