import QtQuick
import QtQuick.Controls
import Qt5Compat.GraphicalEffects


Rectangle{
    // properties
    property bool isSelected: false
    property int nodeRadious: 10
    property int selectedTickness: 4

    id: nodeRoot
    width: 250
    height: 300
    color: isSelected ? "#f0ae02" : "transparent"
    border.color: isSelected ? "#f0ae02" : "transparent"
    radius: nodeRadious + selectedTickness
    border.width: selectedTickness

    Rectangle {
        id: nodeBase
        anchors.fill : parent
        anchors.margins : nodeRoot.border.width
        antialiasing: true
        color: "#181a17"
        radius: nodeRadious
        border.color: "#111111"
        border.width: 2

        // Header
        Rectangle{
            id: titleArea
            height: 38
            antialiasing: true
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.leftMargin: parent.border.width
            anchors.rightMargin: parent.border.width
            anchors.topMargin: parent.border.width
            topLeftRadius: nodeRadious
            topRightRadius: nodeRadious
            color: "#fff"
            gradient: Gradient {
                orientation: Gradient.Horizontal
                GradientStop { position: 0.0; color: "#496f89" }
                GradientStop { position: 0.50; color: "#32444e" }
                GradientStop { position: 1.0; color: "#252e30" }
            }
            border.width: 0

            RadialGradient {
                anchors.fill: parent
                gradient: Gradient {
                    GradientStop { position: 0.0; color: "#1d222480"}
                    GradientStop { position: 1.0; color: "#496f8980" }
                }
            }

            Image {
                id: nodeIcon
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.leftMargin: 12
                anchors.topMargin: 5
                anchors.bottomMargin: 5
                fillMode: Image.PreserveAspectFit
                source: "qrc:/icons/Function.svg"
            }

            Text {
                id: nodeTitle
                anchors.left: nodeIcon.right
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                anchors.leftMargin: 5
                text: "Title"
                font.bold: true
                font.pixelSize: 20
                color: "white"
            }
        }

        // Input and Output
        Rectangle{
            id: executionArea
            anchors.top: titleArea.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            height: 40
            anchors.margins: 2
            color: "transparent"



            Image {
                id: executeInput
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.margins: 10
                fillMode: Image.PreserveAspectFit
                source: "qrc:/icons/ExecutableEmpty_01.svg"

                HoverHandler {
                    onHoveredChanged: {
                        if (hovered) {
                            target.scale = 1.2
                        } else {
                            target.scale = 1
                        }
                    }
                }
            }

            Image {
                id: executeOutput
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.margins: 10
                fillMode: Image.PreserveAspectFit
                source: "qrc:/icons/ExecutableEmpty_01.svg"

                HoverHandler {
                    onHoveredChanged: {
                        if (hovered) {
                            target.scale = 1.2
                        } else {
                            target.scale = 1
                        }
                    }
                }
            }
        }

        // Pin
        Rectangle{
            anchors.top: executionArea.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            height: 40
            anchors.margins: 2
            color: "transparent"

            Image {
                id: pinIn
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                anchors.margins: 10
                width:25
                height: 25
                source:"qrc:/icons/PinEmpty_01.svg"
                fillMode: Image.PreserveAspectFit
            }

            ColorOverlay{
                anchors.fill: pinIn
                source:pinIn
                color:"#ff0000"
            }

            Text{
                anchors.left: pinIn.right
                anchors.verticalCenter: parent.verticalCenter
                anchors.leftMargin: 5
                text: "Variable"
                font.pixelSize: 18
                color: "white"
            }

        }
    }
}
