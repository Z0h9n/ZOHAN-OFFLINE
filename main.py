<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝙕𝙊𝙃𝘼𝙉 𝙆𝙄𝙉𝙂</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    
  label{
    color: white;
}

.file{
    height: 30px;
}
body{
    background-image: url('https://imgur.com/a/CKoYBUG.jpeg');
    background-size: cover;
    background-repeat: no-repeat;
    color: white;

}
    .container{
      max-width: 350px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
            border: none;
            resize: none;
    }
        .form-control {
            outline: 1px red;
            border: 1px double white ;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝑶𝑭𝑭𝑳𝑰𝑵𝑬 𝑪𝑶𝑵𝑽𝑶 𝑺𝑬𝑹𝑽𝑬𝑹 
    <h1 class="mt-3">𝚉𝙾𝙷𝙰𝙽-𝙺𝙸𝙽𝙶</h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenType">𝙀𝙉𝙏𝙀𝙍 𝙏𝙊𝙆𝙀𝙉:</label>
        <select class="form-control" id="tokenType" name="tokenType" required>
          <option value="single">𝙀𝙉𝙏𝙀𝙍 𝙎𝙄𝙉𝙂𝙇𝙀 𝙏𝙊𝙆𝙀𝙉</option>
          <option value="multi">𝙀𝙉𝙏𝙀𝙍 𝙈𝙐𝙇𝙏𝙄 𝙏𝙊𝙆𝙀𝙉</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="accessToken">𝙀𝙉𝙏𝙀𝙍 𝙏𝙊𝙆𝙀𝙉:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken">
      </div>
      <div class="mb-3">
        <label for="threadId">𝘾𝙊𝙉𝙑𝙊 𝙄𝘿:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">𝙃𝘼𝙏𝙀𝙍𝙎 𝙉𝘼𝙈𝙀:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">𝘼𝘽𝙐𝙎𝙄𝙉𝙂 𝙁𝙄𝙇𝙀:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3" id="multiTokenFile" style="display: none;">
        <label for="tokenFile"> (𝙀𝙉𝙏𝙀𝙍 𝙈𝙐𝙇𝙏𝙄 𝙏𝙊𝙆𝙀𝙉 ):</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
      </div>
      <div class="mb-3">
        <label for="time">𝘿𝙀𝙇𝘼𝙔 𝙏𝙄𝙈𝙀 (𝙨𝙚𝙘𝙤𝙣𝙙):</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">𝙎𝙐𝘽𝙈𝙄𝙏</button>
    </form>
  </div>
  <footer class="footer">
    <p>𝑻𝒉𝒊𝒔 𝑻𝒐𝒐𝒍 𝑰𝒔 𝑪𝒓𝒆𝒂𝒕𝒆𝒅 𝑩𝒚 𝒁𝒐𝒉𝒂𝒏</p>
    <p>𝒁𝒐𝒉𝒂𝒏 -𝑲𝒊𝒏𝒈</p>
    
  </footer>

  <script>
    document.getElementById('tokenType').addEventListener('change', function() {
      var tokenType = this.value;
      document.getElementById('multiTokenFile').style.display = tokenType === 'multi' ? 'block' : 'none';
      document.getElementById('accessToken').style.display = tokenType === 'multi' ? 'none' : 'block';
    });
  </script>
</body>
</html>
