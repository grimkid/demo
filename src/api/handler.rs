use axum::extract;
use serde::Deserialize;
#[derive(Deserialize)]
#[derive(Debug)]
pub(crate) struct CreateUser {
    email: String,
    password: String
}
pub(crate) async fn root_post_json(extract::Json(payload): extract::Json<CreateUser>)  {
    println!("{:?}", payload);
}
pub(crate) async fn root_get_header() {

}

pub(crate) async fn root_get()  {
    println!("Hello, world!");
    println!("Get");
}
pub(crate) async fn root_post() {
    println!("Hello, world!");
    println!("Post");
}