from direct. showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def _init_(self):
        ShowBase._init_(self)

        # Load the environment model
        self.scene = self.loader. loadModel("models/environment")
        # Reparent the model to render.
        self.scene. reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene. setPos(-8, 42, 0)

app=MyApp()
app.run()


