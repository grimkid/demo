#![deny(warnings)]
use crate::api::handler;
use crate::db::crud_studenti;
use axum::{routing::get, routing::post, Router};

async fn catalog_routes() -> Router {
    Router::new()
        .nest("/student", studenti_routes().await)

}

async fn studenti_routes() -> Router {
    Router::new()
        .route("/", get(crud_studenti::listing_studenti))
        .route("/",
               post(handler::create_student))
}

fn hello_world_routes() -> Router {
    Router::new()
        .route("/", get(handler::root_get))
        .route("/", post(handler::root_post))
        .route("/users", post(handler::root_post_json))
        .route("/headers", get(handler::root_get_header))
}
pub(crate) async fn init() {
    // let pool = con::get_db_pool().await;
    let app = Router::new()
        .nest("/helloworld", hello_world_routes())
        .nest("/catalog", catalog_routes().await);
    // let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    // axum::serve(listener, app).await.unwrap();
    let addr = std::net::SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("Listening on {}", addr);

    let listener = tokio::net::TcpListener::bind(&addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}




