from IPython.display import display, Javascript

def hide():
    display(Javascript("""
        $("#floatingbottom").remove();
    """))

def show():
    hide()
    display(Javascript("""
        $("body").css("position", "relative");
        $("body").append('<div id="floatingbottom"><div id="floatinginternal">Teste</div></div>');

        $("#floatingbottom").css("position", "absolute");
        $("#floatingbottom").css("bottom", "0");
        $("#floatinginternal").html($("#slidepagination").parent().parent().html());
        $("#floatinginternal").css("background-color", "white");
        $("#floatinginternal").css("margin", "auto");
        $("#floatinginternal").css("width", "70%");
        $("#floatinginternal").css("padding", "2px 5px");
        $("#floatinginternal").css("border-radius", "15px 15px 0 0");
        $("#floatinginternal").css("border", "1px solid black");
        $("#floatinginternal").css("z-index", "1000");
        $("#floatingbottom").css("margin", "0");
        $("#floatingbottom").css("width", "100%");
        $("#floatingbottom").css("text-align", "center");

        $("#floatingbottom").css("z-index", "1000");
    """))
show()
display(Javascript("""
$('div#header-container').hide();
$('div#maintoolbar').hide();
"""))
