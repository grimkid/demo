use crate::api::handler;
use crate::db::con;
use crate::db::crud_studenti;
use axum::{routing::get, routing::post, Extension, Router};
// use std::sync::Arc;

fn catalog_routes() -> Router {
    Router::new()
        .nest("/student", studenti_routes())

}

fn studenti_routes() -> Router {
    Router::new()
        .route("/", get(crud_studenti::listing_studenti))
        .route("/", post(crud_studenti::create_student))

}

fn hello_world_routes() -> Router {
    Router::new()
        .route("/", get(handler::root_get))
        .route("/", post(handler::root_post))
        .route("/users", post(handler::root_post_json))
        .route("/headers", get(handler::root_get_header))
}
pub(crate) async fn init() {
    let pool = con::get_db_pool().await;
    let app = Router::new()
        .nest("/helloworld", hello_world_routes())
        .nest("/catalog", catalog_routes())
        .layer(Extension(pool));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}




