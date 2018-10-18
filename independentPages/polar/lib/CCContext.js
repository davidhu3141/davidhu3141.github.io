var CCContext = function(cx, cy, kx, ky, ctx){ // Coordinated Canvas Context
                
    this.cx = cx;
    this.cy = cy;
    this.kx = kx;
    this.ky = ky;
    this.ctx = ctx;

    this._x = function(x, y){
        return this.cx + this.kx*x;
    };

    this._y = function(x, y){
        return this.cy - this.ky*y;
    };

    this.moveTo = function(x, y){
        this.ctx.moveTo(this._x(x, y), this._y(x, y));
    };

    this.lineTo = function(x, y){
        this.ctx.lineTo(this._x(x, y), this._y(x, y));
    };

    this.text = function(s, x, y){
        this.ctx.fillText(s, this._x(x, y), this._y(x, y));
    };

    this.omoveTo = function(o){
        this.ctx.moveTo(this._x(o.x, o.y), this._y(o.x, o.y));
    };

    this.olineTo = function(o){
        this.ctx.lineTo(this._x(o.x, o.y), this._y(o.x, o.y));
    };

    this.lineWidth = function(w){
        this.ctx.lineWidth = w;
    };

    this.strokeStyle = function(s){
        this.ctx.strokeStyle = s;
    };

    this.beginPath = function(){
        this.ctx.beginPath();
    };

    this.stroke = function(){
        this.ctx.stroke();
    };
    this.clear = function(){
        this.ctx.clearRect(0, 0, 800, 600);
    };

}