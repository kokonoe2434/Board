function getZip() {
    let zipcode = document.getElementById('zip').value;
    // zipcloudAPIの呼び出し
    let el = document.createElement('script');
    el.type = 'text/javascript';
    el.src = 'http://zipcloud.ibsnet.co.jp/api/search?zipcode=' + zipcode + '&callback=writeAddressByZipcloud';
    document.body.appendChild(el);
};

function writeAddressByZipcloud(response) {
	let el = document.getElementById('address1');
	el.value = '';
	// エラー発生時は、アラートを出して終了
	if(response.status != 200) {
		alert(response.message);
		return false;
	}
	// 検索結果がなかった場合も、アラートを出して終了
	if(!response.results) {
		alert('該当する住所が見つかりませんでした');
		return false;
	}
	// 住所文字列の作成
	var address = response.results[0].address1 + response.results[0].address2;
	// 結果が１つの場合は、町域名まで含める
	if(response.results.length == 1) {
		address += response.results[0].address3;
	}
	el.value = address;
};