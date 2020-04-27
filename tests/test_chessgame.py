from unittest import TestCase

import chess

from chess_server import chessgame


class TestLanToSpeech(TestCase):
    def test_lan_to_speech_pawn_move(self):

        lan = "e2-e4"
        expected = "Pawn from e2 to e4"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_pawn_move_check(self):

        lan = "e4-e5+"
        expected = "Pawn from e4 to e5 check"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_pawn_capture(self):

        lan = "e4xd5"
        expected = "Pawn from e4 captures d5"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_pawn_capture_check(self):

        lan = "e6xd7+"
        expected = "Pawn from e6 captures d7 check"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_piece_move(self):

        lan = "Ng1-f3"
        expected = "Knight from g1 to f3"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_piece_move_check(self):

        lan = "Bf1-c4+"
        expected = "Bishop from f1 to c4 check"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_piece_capture(self):

        lan = "Rh1xh8"
        expected = "Rook from h1 captures h8"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_piece_capture_check(self):

        lan = "Qd1xa4+"
        expected = "Queen from d1 captures a4 check"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_piece_move_checkmate(self):

        lan = "Ke6-d6#"
        expected = "King from e6 to d6 check"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_short_castle(self):

        lan = "O-O"
        expected = "Short castle"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_short_castle_check(self):

        lan = "O-O+"
        expected = "Short castle check"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_long_castle(self):

        lan = "O-O-O"
        expected = "Long castle"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)

    def test_lan_to_speech_long_castle_checkmate(self):

        lan = "O-O-O#"
        expected = "Long castle check"

        self.assertEqual(chessgame.lan_to_speech(lan), expected)


class TestTwoSquaresAndPieceToLan(TestCase):
    """
    Reference Game Used: 

    [Event "Live Chess"]
    [Site "Chess.com"]
    [Date "2020.04.25"]
    [Round "?"]
    [White "AbishMathew"]
    [Black "TheVish"]
    [Result "0-1"]
    [ECO "D00"]
    [WhiteElo "974"]
    [BlackElo "2600"]
    [TimeControl "600"]
    [EndTime "6:00:37 PDT"]
    [Termination "TheVish won on time"]

    1. d4 {[%clk 0:09:39.2]} 1... d5 {[%clk 0:09:54.6]} 2. b4 {[%clk 0:09:21.3]}
    2... a5 {[%clk 0:09:51.2]} 3. Bb2 {[%clk 0:09:13.5]} 3... e6 {[%clk 0:09:42.5]}
    4. bxa5 {[%clk 0:09:04.6]} 4... Nf6 {[%clk 0:09:34.9]} 5. Nf3 {[%clk 0:08:54.4]}
    5... c5 {[%clk 0:09:26]} 6. dxc5 {[%clk 0:08:43.7]} 6... Qxa5+ {[%clk
    0:09:21.1]} 7. c3 {[%clk 0:08:25.5]} 7... Bxc5 {[%clk 0:09:08.2]} 8. Ba3 {[%clk
    0:08:04.7]} 8... Bxa3 {[%clk 0:09:00.9]} 9. Nxa3 {[%clk 0:08:00.4]} 9... Nc6
    {[%clk 0:08:46.7]} 10. Nb5 {[%clk 0:07:15.6]} 10... Qxb5 {[%clk 0:08:40.2]} 11.
    Rb1 {[%clk 0:06:42.5]} 11... Qc5 {[%clk 0:08:19.2]} 12. Qd4 {[%clk 0:06:04.5]}
    12... b6 {[%clk 0:08:08.2]} 13. Ne5 {[%clk 0:05:43.5]} 13... Nxe5 {[%clk
    0:08:03.1]} 14. Qxe5 {[%clk 0:05:34.7]} 14... Qxf2+ {[%clk 0:07:46.3]} 15. Kxf2
    {[%clk 0:05:11.4]} 15... Ng4+ {[%clk 0:07:32.4]} 16. Kf3 {[%clk 0:04:54.6]}
    16... Nxe5+ {[%clk 0:07:28.1]} 17. Kf4 {[%clk 0:04:42.2]} 17... f6 {[%clk
    0:07:13.9]} 18. Rxb6 {[%clk 0:04:33.6]} 18... Ke7 {[%clk 0:07:04.4]} 19. Rc6
    {[%clk 0:03:46.5]} 19... Ra4+ {[%clk 0:06:39]} 20. c4 {[%clk 0:03:35.2]} 20...
    Nxc6 {[%clk 0:06:28.8]} 21. e4 {[%clk 0:03:18.8]} 21... e5+ {[%clk 0:06:22.2]}
    22. Kf3 {[%clk 0:03:07.9]} 22... Nd4+ {[%clk 0:06:17.3]} 23. Ke3 {[%clk
    0:02:56.3]} 23... Ra3+ {[%clk 0:06:00.7]} 24. Kd2 {[%clk 0:02:41.7]} 24... Bd7
    {[%clk 0:05:43.4]} 25. c5 {[%clk 0:02:30.7]} 25... Rb8 {[%clk 0:05:29.1]} 26.
    exd5 {[%clk 0:02:17.7]} 26... Rb2+ {[%clk 0:05:04.2]} 27. Kc1 {[%clk 0:02:09.6]}
    27... Rf2 {[%clk 0:04:58.9]} 28. Bb5 {[%clk 0:01:52.5]} 28... Kd8 {[%clk
    0:04:46.6]} 29. Rg1 {[%clk 0:01:41.9]} 29... Raxa2 {[%clk 0:04:39.4]} 30. Rd1
    {[%clk 0:01:34.2]} 30... Rxg2 {[%clk 0:04:28.4]} 31. Rxd4 {[%clk 0:01:32.3]}
    31... exd4 {[%clk 0:04:19.2]} 32. Bc4 {[%clk 0:01:24.9]} 32... Rxh2 {[%clk
    0:04:13.3]} 33. Bxa2 {[%clk 0:01:20]} 33... h5 {[%clk 0:04:03.1]} 34. d6 {[%clk
    0:01:11.1]} 34... h4 {[%clk 0:03:55.6]} 35. c6 {[%clk 0:00:52.1]} 35... Rxa2
    {[%clk 0:03:32.3]} 36. c7+ {[%clk 0:00:43.3]} 36... Ke8 {[%clk 0:03:28.7]} 37.
    c8=Q+ {[%clk 0:00:38]} 37... Bxc8 {[%clk 0:03:13]} 38. d7+ {[%clk 0:00:30.7]}
    38... Kf7 {[%clk 0:02:40.4]} 39. d8=Q {[%clk 0:00:24.8]} 39... d3 {[%clk
    0:02:19.3]} 40. Qxc8 {[%clk 0:00:11.2]} 40... Rc2+ {[%clk 0:02:13.3]} 41. Kd1
    {[%clk 0:00:02.2]} 41... Rxc8 {[%clk 0:02:08.4]} 42. Kd2 {[%clk 0:00:00.1]}
    42... Rd8 {[%clk 0:01:34.4]} 0-1
    """

    def test_two_squares_and_piece_to_lan_pawn_move(self):

        board = chess.Board(
            "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        )  # Starting position

        squares = ["d2", "d4"]
        expected = "d2-d4"
        result = chessgame.two_squares_and_piece_to_lan(board, squares)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_piece_move(self):

        board = chess.Board(
            "rnbqkbnr/1pp1pppp/8/p2p4/1P1P4/8/P1P1PPPP/RNBQKBNR w KQkq a6 0 3"
        )  # Before Move 3

        squares = ["c1", "b2"]
        expected = "Bc1-b2"
        result = chessgame.two_squares_and_piece_to_lan(board, squares)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_pawn_capture(self):

        board = chess.Board(
            "rnbqkbnr/1pp2ppp/4p3/p2p4/1P1P4/8/PBP1PPPP/RN1QKBNR w KQkq - 0 4"
        )  # Before move 4

        squares = ["b4", "a5"]
        expected = "b4xa5"
        result = chessgame.two_squares_and_piece_to_lan(board, squares)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_piece_capture_check(self):

        board = chess.Board(
            "rnbqkb1r/1p3ppp/4pn2/P1Pp4/8/5N2/PBP1PPPP/RN1QKB1R b KQkq - 0 6"
        )  # Black's sixth move

        squares = ["d8", "a5"]  # 6... Qxa5
        expected = "Qd8xa5+"
        result = chessgame.two_squares_and_piece_to_lan(board, squares)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_piece_capture(self):

        board = chess.Board(
            "rnb1kb1r/1p3ppp/4pn2/q1Pp4/8/2P2N2/PB2PPPP/RN1QKB1R b KQkq - 0 7"
        )

        squares = ["f8", "c5"]
        expected = "Bf8xc5"
        result = chessgame.two_squares_and_piece_to_lan(
            board, squares, piece="Rook"
        )  # Trying out with random noise for piece

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_piece_move_check(self):

        board = chess.Board("r1b1k2r/5ppp/1p2pn2/3pQ3/8/2P5/P3PKPP/1R3B1R b kq - 0 15")

        squares = ["f6", "g4"]
        expected = "Nf6-g4+"
        result = chessgame.two_squares_and_piece_to_lan(board, squares, piece="queen")

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_king_move(self):

        board = chess.Board("r1b1k2r/6pp/1R2pp2/3pn3/5K2/2P5/P3P1PP/5B1R b kq - 0 18")

        squares = ["e8", "e7"]
        expected = "Ke8-e7"
        result = chessgame.two_squares_and_piece_to_lan(board, squares)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_pawn_move_check(self):

        board = chess.Board("2b4r/4k1pp/2n1pp2/3p4/r1P1PK2/8/P5PP/5B1R b - e3 0 21")

        squares = ["e6", "e5"]
        expected = "e6-e5+"
        result = chessgame.two_squares_and_piece_to_lan(board, squares, piece="queen")

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_pawn_promotion_check(self):

        board = chess.Board("4k3/2Pb2p1/3P1p2/8/3p3p/8/r7/2K5 w - - 1 37")

        squares = ["c7", "c8"]
        piece = "queen"
        expected = "c7-c8=Q+"
        result = chessgame.two_squares_and_piece_to_lan(board, squares, piece)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_pawn_promotion(self):

        board = chess.Board("2b5/3P1kp1/5p2/8/3p3p/8/r7/2K5 w - - 1 39")

        squares = ["d7", "d8"]
        piece = "queen"
        expected = "d7-d8=Q"
        result = chessgame.two_squares_and_piece_to_lan(board, squares, piece)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_pawn_promotion_underpromotion(self):

        board = chess.Board(
            "2b5/3P1kp1/5p2/8/3p3p/8/r7/2K5 w - - 1 39"
        )  # Same position as before

        squares = ["d7", "d8"]
        piece = "knight"  # Deviating from game
        expected = "d7-d8=N+"  # Is a check
        result = chessgame.two_squares_and_piece_to_lan(board, squares, piece)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_pawn_promotion_to_king_error(self):

        board = chess.Board("2b5/3P1kp1/5p2/8/3p3p/8/r7/2K5 w - - 1 39")

        squares = ["d7", "d8"]
        piece = "king"
        expected = "illegal move"  # Special flag
        result = chessgame.two_squares_and_piece_to_lan(board, squares, piece)

        self.assertEqual(result, expected)

    def test_two_squares_and_piece_to_lan_illegal_move(self):

        board = chess.Board("2Q5/5kp1/5p2/8/7p/3p4/r7/2K5 b - - 0 40")

        squares = ["a2", "c3"]
        expected = "illegal move"
        result = chessgame.two_squares_and_piece_to_lan(board, squares)

        self.assertEqual(result, expected)


class TestProcessCastleByQueryText(TestCase):
    def test_process_castle_by_querytext_short(self):

        # Game used: tanmaybhat2 vs AbishMathew, from chess.com: https://www.chess.com/live/game/4769180825

        board = chess.Board(
            "rnbqk2r/ppppp1bp/6pn/5p2/3P1P1P/2P2N2/PP2P1P1/RNBQKB1R b KQkq - 0 5"
        )

        queryText = "Castle short"
        expected = "O-O"
        result = chessgame.process_castle_by_querytext(board, queryText)

        self.assertEqual(result, expected)

    def test_process_castle_by_querytext_kingside(self):

        # Game used: tanmaybhat2 vs AbishMathew, from chess.com: https://www.chess.com/live/game/4769180825

        board = chess.Board(
            "2r2rk1/2p1q1b1/p1Qpp1p1/5p2/1PNP1Pn1/B1P2NP1/P3P1B1/R3K2R w KQ - 1 22"
        )

        queryText = "castle kingside"
        expected = "O-O"
        result = chessgame.process_castle_by_querytext(board, queryText)

        self.assertEqual(result, expected)

    def test_process_castle_by_querytext_long(self):

        # Game used: AbishMathew vs biswakalyan_rath, from chess.com: https://www.chess.com/live/game/4665388093

        board = chess.Board(
            "r3k2r/ppp2ppp/8/1q2p3/4n1b1/3P1NP1/PPP1Kb1P/R1BQ3R b kq - 2 13"
        )

        queryText = "castle long"
        expected = "O-O-O"
        result = chessgame.process_castle_by_querytext(board, queryText)

        self.assertEqual(result, expected)

    def test_process_castle_by_querytext_long_check(self):

        # Game borrowed from: https://www.chess.com/forum/view/game-showcase/o-oo-o-o

        board = chess.Board(
            "2bk1b1r/p4ppp/5n2/2n4P/4pBP1/5P2/prP1BN2/R3K2R w KQ - 0 17"
        )

        queryText = "long castles check"
        expected = "O-O-O+"
        result = chessgame.process_castle_by_querytext(board, queryText)

        self.assertEqual(result, expected)

    def test_process_castle_by_querytext_short_check(self):

        # Game borrowed from: https://www.chess.com/forum/view/game-showcase/o-oo-o-o

        board = chess.Board(
            "rnbq1kn1/ppp1r3/3p4/8/3P3Q/2N3P1/PPP1N1BP/3RK2R w K - 5 15"
        )

        queryText = "short castle"
        expected = "O-O+"
        result = chessgame.process_castle_by_querytext(board, queryText)

        self.assertEqual(result, expected)