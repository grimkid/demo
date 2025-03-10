#![deny(warnings)]
use axum::{extract, Json};
use serde::{Deserialize};
use sqlx::FromRow;

#[derive(Deserialize)]
#[derive(Debug)]
pub(crate) struct CreateUser {
    email: String,
    password: String
}
pub(crate) async fn root_post_json(extract::Json(payload): extract::Json<CreateUser>)  {
    println!("{:?}:{:?}", payload.email, payload.password);
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

#[derive(Debug, serde::Deserialize)]
pub(crate) struct StudentRequest {
    pub(crate) id: String,
    pub(crate) nume: String,
}

#[derive(Debug, serde::Serialize, FromRow)]
pub(crate) struct StudentResponse {
    id: String,
    nume: String,
}

pub async fn create_student(
    Json(payload): Json<StudentRequest>,
) -> Json<StudentResponse> {
    let student = crate::db::crud_studenti::create_student(payload).await;
    Json(student)
}
