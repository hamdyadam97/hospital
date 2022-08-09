import React from "react";
class Tips extends React.Component{
    render(){
        return(
        <>
        <div class="work-steps" id="work-steps">
      <div class="container">
        <img src="assets/imgs/work-steps.png" alt="" class="image" />
        <div class="info">
          <div class="box">
            <img src="imgs/work-steps-1.png" alt="" />
            <div class="text">
              <h3>Eat a healthy diet</h3>
              <p>
              Eat a combination of different foods, including fruit, vegetables, legumes, nuts and whole grains. Adults should eat at least five portions (400g) of fruit and vegetables per day
              </p>
            </div>
          </div>
          <div class="box">
            <img src="imgs/work-steps-2.png" alt="" />
            <div class="text">
              <h3>Consume less salt and sugar</h3>
              <p>
              consuming excessive amounts of sugars increases the risk of tooth decay and unhealthy weight gain
              </p>
            </div>
          </div>
          <div class="box">
            <img src="imgs/work-steps-3.png" alt="" />
            <div class="text">
              <h3>Reduce intake of harmful fats</h3>
              <p>
              Fats consumed should be less than 30% of your total energy intake. This will help prevent unhealthy weight gain and NCDs.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="work-steps" id="work-steps">
      <div class="container">
        <img src="assets/imgs/work-steps2.png" alt="" class="image" />
        <div class="info">
          <div class="box">
            <img src="imgs/work-steps-1.png" alt="" />
            <div class="text">
              <h3>Avoid harmful use of alcohol</h3>
              <p>
              There is no safe level for drinking alcohol. Consuming alcohol can lead to health problems such as mental and behavioural disorders
              </p>
            </div>
          </div>
          <div class="box">
            <img src="imgs/work-steps-2.png" alt="" />
            <div class="text">
              <h3>Don’t smoke</h3>
              <p>
              Smoking tobacco causes NCDs such as lung disease, heart disease and stroke. Tobacco kills not only the direct smokers but even non-smokers through second-hand exposure
              </p>
            </div>
          </div>
          <div class="box">
            <img src="imgs/work-steps-3.png" alt="" />
            <div class="text">
              <h3> Be active</h3>
              <p>
              Physical activity is defined as any bodily movement produced by skeletal muscles that requires energy expenditure.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
        </>)
    }
}

export default Tips;