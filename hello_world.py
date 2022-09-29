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

        # Add the spinCameraTask procedure to the task manager.
        self. task.Mgr. add(self. spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/ panda-model",
                                {"walk": "models/panda-walk4"})
        self. pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task) :
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self. camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app=MyApp()
app.run()


