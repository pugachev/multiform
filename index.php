<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
use PHPMailer\PHPMailer\SMTP;

// 設置した場所のパスを指定する
require('PHPMailer/src/PHPMailer.php');
require('PHPMailer/src/Exception.php');
require('PHPMailer/src/SMTP.php');

// 文字エンコードを指定
mb_language('uni');
mb_internal_encoding('UTF-8');

// インスタンスを生成（true指定で例外を有効化）
$mail = new PHPMailer(true);

// 文字エンコードを指定
$mail->CharSet = 'utf-8';

try {
  // デバッグ設定
  $mail->SMTPDebug = 2; // デバッグ出力を有効化（レベルを指定）
  // $mail->Debugoutput = function($str, $level) {echo "debug level $level; message: $str<br>";};

  // SMTPサーバの設定
  $mail->isSMTP();                          // SMTPの使用宣言
  $mail->Host       = 'sv13004.xserver.jp';   // SMTPサーバーを指定
  $mail->SMTPAuth   = true;                 // SMTP authenticationを有効化
  $mail->Username   = 'mailtest@ikefukuro40.tech';   // SMTPサーバーのユーザ名
  $mail->Password   = 'Manabu2010';           // SMTPサーバーのパスワード
  $mail->SMTPSecure = tls;  // 暗号化を有効（tls or ssl）無効の場合はfalse
  $mail->Port       = 465; // TCPポートを指定（tlsの場合は465や587）
  
  //$tgt=['apimaster2018@gmail.com','mtaketani37@gmail.com'];

  // 送受信先設定（第二引数は省略可）
  $mail->setFrom('mailtest@ikefukuro40.tech', '差出人名'); // 送信者
  $mail->addAddress('apimaster2018@gmail.com', '受信者名');   // 宛先
  $mail->addAddress('mtaketani37@gmail.com', '受信者名');   // 宛先
  //$mail->addReplyTo('mailtest@ikefukuro40.tech', 'お問い合わせ'); // 返信先
  $mail->addCC('pugachev2011@gmail.com', '受信者名'); // CC宛先
  $mail->Sender = 'mailtest@ikefukuro40.tech'; // Return-path

  // 送信内容設定
  $mail->Subject = 'これはテストです'; 
  $mail->Body    = 'これはボディですね。cc入ってるかな？';  

  // 送信
  $mail->send();
} catch (Exception $e) {
  // エラーの場合
  echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
?>

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8" />
    <title>MailTest</title>
</head>
<body>
	<h3>MailTest body</h3>
</body>
</html>