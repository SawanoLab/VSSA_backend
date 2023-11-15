INSERT INTO users (uuid, username) VALUES ( '3be043a01d954ddb81ca5db72d7d40a3','username' );

INSERT INTO seasons (created_at, updated_at, start_day, end_day, season_name, game_format, code, user_id, uuid)
VALUES (
    CURRENT_TIMESTAMP, -- created_at
    CURRENT_TIMESTAMP, -- updated_at
    '2022-07-01 00:00:00', 
    -- start_day
    '2022-07-31 23:59:59', -- end_day
    'Summer 2022', -- season_name
    'Game Format Example', -- game_format
    'S2022_001', -- code
    '3be043a01d954ddb81ca5db72d7d40a3', -- user_id
    '89650f78c57247039d385b57aa59db34' -- uuid
);

INSERT INTO teams (created_at, updated_at,name, code, director, coach, trainer, doctor, user_id, season_id, uuid)
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
    '3be043a01d954ddb81ca5db72d7d40a3', -- user_id
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
    '3be043a01d954ddb81ca5db72d7d40a3', -- user_id
    '89650f78c57247039d385b57aa59db34', -- season_id
    '329a1c1570c543cc8750386b961a1df6' -- uuid
);


INSERT INTO players(uuid, name, player_number, code, postion, weight, height, user_id, team_id, season_id)
VALUES
('68ef9a7adae2456f891c831b04901b8f', 'Player 1', 1, 'PL1', 'Wing Spiker', 75, 180, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b9f', 'Player 2', 2, 'PL2', 'Middle Blocker', 80, 185, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b1f', 'Player 3', 3, 'PL3', 'Setter', 70, 175, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b2f', 'Player 4', 4, 'PL4', 'Wing Spiker', 78, 182, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b3f', 'Player 5', 5, 'PL5', 'Middle Blocker', 81, 186, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b4f', 'Player 6', 6, 'PL6', 'Opposite', 77, 181, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b5f', 'Player 7', 7, 'PL7', 'Libero', 67, 172, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b6f', 'Player 8', 8, 'PL8', 'Wing Spiker', 76, 179, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b04901b7f', 'Player 9', 9, 'PL9', 'Middle Blocker', 80, 184, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('18ef9a7adae2456f891c831b04901b8f', 'Player 10', 10, 'PL10', 'Setter', 72, 176, '3be043a01d954ddb81ca5db72d7d40a3', 'edf400dc06c641cfbec67d8d4ba82e3f', '89650f78c57247039d385b57aa59db34'),
('28ef9a7adae2456f891c831b04901b8f', 'Player 11', 11, 'PL11', 'Wing Spiker', 74, 178, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('38ef9a7adae2456f891c831b04901b8f', 'Player 12', 12, 'PL12', 'Middle Blocker', 82, 186, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('48ef9a7adae2456f891c831b04901b8f', 'Player 13', 13, 'PL13', 'Opposite', 75, 180, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('58ef9a7adae2456f891c831b04901b8f', 'Player 14', 14, 'PL14', 'Libero', 69, 171, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('68ef9a7adae2456f891c831b14901b8f', 'Player 15', 15, 'PL15', 'Wing Spiker', 73, 177, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('78ef9a7adae2456f891c831b04901b8f', 'Player 16', 16, 'PL16', 'Middle Blocker', 79, 183, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('88ef9a7adae2456f891c831b04901b8f', 'Player 17', 17, 'PL17', 'Setter', 72, 174, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('98ef9a7adae2456f891c831b04901b8f', 'Player 18', 18, 'PL18', 'Wing Spiker', 74, 177, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('61ef9a7adae2456f891c831b04901b8f', 'Player 19', 19, 'PL19', 'Middle Blocker', 80, 185, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34'),
('62ef9a7adae2456f891c831b04901b8f', 'Player 20', 20, 'PL20', 'Opposite', 78, 182, '3be043a01d954ddb81ca5db72d7d40a3', '329a1c1570c543cc8750386b961a1df6', '89650f78c57247039d385b57aa59db34');
