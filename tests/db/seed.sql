INSERT INTO users (uuid, username) VALUES ( '1963f7eff71e4a0c944d62628a5bb070','username' );

INSERT INTO seasons (created_at, updated_at, start_day, end_day, season_name, game_format, code, user_id, uuid)
VALUES (
    CURRENT_TIMESTAMP, -- created_at
    CURRENT_TIMESTAMP, -- updated_at
    '2022-07-01 00:00:00', -- start_day
    '2022-07-31 23:59:59', -- end_day
    'Summer 2022', -- season_name
    'Game Format Example', -- game_format
    'S2022_001', -- code
    '1963f7eff71e4a0c944d62628a5bb070', -- user_id
    '89650f78c57247039d385b57aa59db34' -- uuid
);

INSERT INTO teams (created_at, updated_at, name, code, director, coach, trainer, doctor, user_id, season_id, uuid)
VALUES
(
    CURRENT_TIMESTAMP, -- created_at
    CURRENT_TIMESTAMP, -- updated_at
    'Team 1', -- name
    'T1', -- code
    'Director 1', -- director
    'Coach 1', -- coach
    'Trainer 1', -- trainer
    'Doctor 1', -- doctor
    '1963f7eff71e4a0c944d62628a5bb070', -- user_id
    '89650f78c57247039d385b57aa59db34', -- season_id
    'edf400dc06c641cfbec67d8d4ba82e3f' -- uuid
),
(
    CURRENT_TIMESTAMP, -- created_at
    CURRENT_TIMESTAMP, -- updated_at
    'Team 2', -- name
    'T2', -- code
    'Director 2', -- director
    'Coach 2', -- coach
    'Trainer 2', -- trainer
    'Doctor 2', -- doctor
    '1963f7eff71e4a0c944d62628a5bb070', -- user_id
    '89650f78c57247039d385b57aa59db34', -- season_id
    '329a1c1570c543cc8750386b961a1df6' -- uuid
);


INSERT INTO players(uuid, name, player_number, code, postion, weight, height, user_id, team_id, season_id) VALUES
('68ef9a7adae2456f891c831b04901b8f', 'Player 1', 1, 'PL1', 'Wing Spiker', 75, 180, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b9f', 'Player 2', 2, 'PL2', 'Middle Blocker', 80, 185, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b1f', 'Player 3', 3, 'PL3', 'Setter', 70, 175, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b2f', 'Player 4', 4, 'PL4', 'Wing Spiker', 78, 182, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b3f', 'Player 5', 5, 'PL5', 'Middle Blocker', 81, 186, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b4f', 'Player 6', 6, 'PL6', 'Opposite', 77, 181, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b5f', 'Player 7', 7, 'PL7', 'Libero', 67, 172, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b6f', 'Player 8', 8, 'PL8', 'Wing Spiker', 76, 179, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b7f', 'Player 9', 9, 'PL9', 'Middle Blocker', 80, 184, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('18ef9a7adae2456f891c831b04901b8f', 'Player 10', 10, 'PL10', 'Setter', 72, 176, '1963f7eff71e4a0c944d62628a5bb070', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('28ef9a7adae2456f891c831b04901b8f', 'Player 11', 11, 'PL11', 'Wing Spiker', 74, 178, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('38ef9a7adae2456f891c831b04901b8f', 'Player 12', 12, 'PL12', 'Middle Blocker', 82, 186, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('48ef9a7adae2456f891c831b04901b8f', 'Player 13', 13, 'PL13', 'Opposite', 75, 180, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('58ef9a7adae2456f891c831b04901b8f', 'Player 14', 14, 'PL14', 'Libero', 69, 171, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b14901b8f', 'Player 15', 15, 'PL15', 'Wing Spiker', 73, 177, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('78ef9a7adae2456f891c831b04901b8f', 'Player 16', 16, 'PL16', 'Middle Blocker', 79, 183, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('88ef9a7adae2456f891c831b04901b8f', 'Player 17', 17, 'PL17', 'Setter', 72, 174, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('98ef9a7adae2456f891c831b04901b8f', 'Player 18', 18, 'PL18', 'Wing Spiker', 74, 177, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('61ef9a7adae2456f891c831b04901b8f', 'Player 19', 19, 'PL19', 'Middle Blocker', 80, 185, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('62ef9a7adae2456f891c831b04901b8f', 'Player 20', 20, 'PL20', 'Opposite', 78, 182, '1963f7eff71e4a0c944d62628a5bb070', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34');


INSERT INTO matchs (uuid, home_team_id, away_team_id, season_id, user_id) VALUES
('80ceca3f7f16496e9d769f42996fedbb', 'edf400dc06c641cfbec67d8d4ba82e3f', '329a1c1570c543cc8750386b961a1df6','89650f78c57247039d385b57aa59db34', '1963f7eff71e4a0c944d62628a5bb070');

INSERT INTO match_set_score (uuid, match_id, set_number, score_team_home, score_team_away) VALUES
('95e2d7a1aada42d0b674d850af9c6484', '80ceca3f7f16496e9d769f42996fedbb', 1, 0, 0);

INSERT INTO match_scores (uuid, home_team_score, away_team_score, match_set_score_id, score_team_id, sequence_number) VALUES
('858550cbcd2944bca573877cfd184b1e', 1, 0, '95e2d7a1aada42d0b674d850af9c6484', 'edf400dc06c641cfbec67d8d4ba82e3f', 1),
('40d13b151a824920a24333cc22971e3d', 2, 0, '95e2d7a1aada42d0b674d850af9c6484', 'edf400dc06c641cfbec67d8d4ba82e3f', 2),
('d285e47200824aa9a7d732cb98c95c79', 3, 0, '95e2d7a1aada42d0b674d850af9c6484', 'edf400dc06c641cfbec67d8d4ba82e3f', 3);


INSERT INTO playerMatchInfo (uuid, player_id, match_id, on_court, zone_code, libero) VALUES
('d65e3a61f779480fa9b8815c3cd114cc', '68ef9a7adae2456f891c831b04901b8f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z5', false),
('13f0c21b7f4248bca3292dd6173b6763', '68ef9a7adae2456f891c831b04901b9f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z6', true),
('3b45bf1293e44cefb80c4b32eb5f1f9f', '68ef9a7adae2456f891c831b04901b1f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z1', false),
('913f1db0a54249e7a6d00d60f0f90d4d', '68ef9a7adae2456f891c831b04901b2f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z2', true),
('0f07a9d1408e4c2592c832c7f844f0a9', '68ef9a7adae2456f891c831b04901b3f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z3', false),
('b3e01d547b5743d9924d6e6dfc80fbd4', '68ef9a7adae2456f891c831b04901b4f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z4', false),
('a9e88e0476014f7b8bdaae5f8d45d3c4', '68ef9a7adae2456f891c831b04901b5f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z5', true),
('49a7001d557a428c86a9d98a4b666aad', '68ef9a7adae2456f891c831b04901b6f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z6', false),
('f7c0986af9d94cdaa1cf192b3f4a016e', '18ef9a7adae2456f891c831b04901b8f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z2', true),
('55f5be62ecb54eb1b1dbdab7512f71b2', '28ef9a7adae2456f891c831b04901b8f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z3', false),
('722d1a52b6e64a1a89dca1d3a865c5e3', '38ef9a7adae2456f891c831b04901b8f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z4', false),
('4d429d6a11ea4625a1c01b7f7a3e9fc7', '48ef9a7adae2456f891c831b04901b8f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z5', true),
('4f059d74b1584d0b94645b7e4b5db6c1', '58ef9a7adae2456f891c831b04901b8f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z6', false),
('15b9b0f327804ea2b54a5c598b5e3aa7', '68ef9a7adae2456f891c831b04901b7f', '80ceca3f7f16496e9d769f42996fedbb', true, 'Z3', false);

INSERT INTO attacks ( uuid, home_team_score, away_team_score, attack_start_zone, attack_end_zone, attack_ball_type, attack_skill, attack_evaluation, user_id, match_id, team_id, player_id, away_team_set_score, home_team_set_score) VALUES (
    '306fc0dd7aaf4780a12932b429654ebb', -- uuid
    1, -- home_team_score
    0, -- away_team_score
    3, -- attack_start_zone
    4, -- attack_end_zone
    'high', -- attack_ball_type
    'headSpike', -- attack_skill
    'kill', -- attack_evaluation
    '1963f7eff71e4a0c944d62628a5bb070', -- user_id
    '80ceca3f7f16496e9d769f42996fedbb', -- match_id
    'edf400dc06c641cfbec67d8d4ba82e3f', -- team_id
    '18ef9a7adae2456f891c831b04901b8f', -- player_id
    0, -- away_team_set_score
    1 -- home_team_set_score
);
