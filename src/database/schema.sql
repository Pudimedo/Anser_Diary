-- Tabela de usuários
CREATE TABLE IF NOT EXISTS tb_usuario (
    usu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    usu_username VARCHAR(60) NOT NULL,
    usu_email VARCHAR(100) NOT NULL UNIQUE,
    usu_senha VARCHAR(255) NOT NULL,
    usu_profile_pic TEXT DEFAULT NULL, -- Caminho da foto de perfil do usuário
    usu_data_criacao DATETIME DEFAULT (DATETIME('now', 'localtime'))
);

-- Tabela de diários
CREATE TABLE IF NOT EXISTS tb_diarios (
    dia_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dia_usu_id INTEGER NOT NULL,
    dia_titulo VARCHAR(100) DEFAULT 'Novo Diário',
    dia_conteudo TEXT,
    dia_data_criacao DATETIME DEFAULT (DATETIME('now', 'localtime')),
    dia_publico BOOLEAN DEFAULT FALSE, -- 0 (FALSE) = privado e 1 (TRUE) = público 
    FOREIGN KEY (dia_usu_id) REFERENCES tb_usuario(usu_id) ON DELETE CASCADE -- "ON DELETE CASCADE" serve para se você apagar um usuário, todos os diários dele também serão apagados automaticamente. 
);