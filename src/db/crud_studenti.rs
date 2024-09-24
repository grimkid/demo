use std::sync::Arc;
use axum::{Json, extract::Extension, response::IntoResponse};
use axum::response::Response;
use http::StatusCode;
use serde_json::json;
use sqlx::{PgPool, FromRow};
use serde::Serialize;

pub(crate) async fn create_student(
    Json(payload): Json<CreateRequestStudenti>,
    Extension(pool): Extension<Arc<PgPool>>
) -> Result<Json<serde_json::Value>, Response> {
   let result = sqlx::query_as::<_, Student>(
        "INSERT INTO Studenti (nume, id) VALUES ($1, $2) RETURNING id")
        .bind(&payload.nume)
        .bind(&payload.id)
        .fetch_one(&*pool)
        .await;
    match result {
        Ok(record) => Ok(Json(json!({ "student": record }))),
        Err(_) => Err((StatusCode::INTERNAL_SERVER_ERROR, Json(json!({"error": "Internal Server Error"}))).into_response())
    }
}
#[derive(serde::Deserialize, Debug)]
struct CreateRequestStudenti {
    nume: String,
    id: String
}

#[derive(Serialize, FromRow, Debug)]
struct Student {
    id: String,
    nume: String,
}

pub(crate) async fn listing_studenti(Extension(pool): Extension<Arc<PgPool>>) {
    sqlx::query("SELECT * FROM Studenti")
        .fetch_all(&*pool).await.expect("TODO: panic message");
}