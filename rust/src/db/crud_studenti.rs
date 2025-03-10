use std::sync::Arc;
use axum::{extract::Extension};
use sqlx::{PgPool};
use crate::api::handler::{StudentRequest, StudentResponse};


pub(crate) async fn create_student(
    student: StudentRequest,

) -> StudentResponse {
    let sql = "INSERT INTO Studenti (id, nume) VALUES ($1, $2) RETURNING id, nume";

    let pool = crate::db::con::get_db_pool().await;
    sqlx::query_as::<_, StudentResponse>(sql)
        .bind(&student.id)
        .bind(&student.nume)
        .fetch_one(&*pool).await.unwrap()
}

pub(crate) async fn listing_studenti(Extension(pool): Extension<Arc<PgPool>>) -> () {
    sqlx::query("SELECT * FROM Studenti")
        .fetch_all(&*pool).await.unwrap();
}