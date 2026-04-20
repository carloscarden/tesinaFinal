
const value = JSON.parse(document.getElementById('diagram-data').textContent);
console.log(value);

var $ = go.GraphObject.make;

function textStyle() {
    return {
        font: "bold 11pt Lato, Helvetica, Arial, sans-serif",
        stroke: "black"
    }
}

function nodeStyle() {
    return [
        // The Node.location comes from the "loc" property of the node data,
        // converted by the Point.parse static method.
        // If the Node.location is changed, it updates the "loc" property of the node data,
        // converting back using the Point.stringify static method.
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(go.Point.stringify),
        {
            // the Node.location is at the center of each node
            locationSpot: go.Spot.Center
        }
    ];
}

// SD is a global variable, to avoid polluting global namespace and to make the global
// nature of the individual variables obvious.
var SD = {
    // adding a new link respectively.
    itemType: "linkNormal",    // Set when user clicks on a node or link button.
    nodeCounter: { stock: 0, cloud: 0, variable: 0, valve: 0 }
};

// Diagram: View
var myDiagram =
    new go.Diagram("myDiagramDiv",  // create a Diagram for the HTML Div element
        {
            "undoManager.isEnabled": true,
            // override the link creation process
            "linkingTool.insertLink": function (fromnode, fromport, tonode, toport) {  // method override must be function, not =>
                // to control what kind of Link is created,
                // change the LinkingTool.archetypeLinkData's category
                console.log(SD.itemType);
                myDiagram.model.setCategoryForLinkData(this.archetypeLinkData, SD.itemType);
                // Whenever a new Link is drawn by the LinkingTool, it also adds a node data object
                // that acts as the label node for the link, to allow links to be drawn to/from the link.
                // also change the text indicating the condition, which the user can edit
                this.archetypeLinkData.text = SD.itemType;
                return go.LinkingTool.prototype.insertLink.call(this, fromnode, fromport, tonode, toport);
            }

        },


    );  // enable undo & redo


myDiagram.nodeTemplateMap.add("Hecho",  // the default category
    $(go.Node, "Auto", nodeStyle(),

        { portId: "", fromLinkable: true, toLinkable: true, cursor: "pointer" },
        $(go.Shape, { fill: "white", stroke: "black", strokeWidth: 3.5 }),
        $(go.Panel, "Table",

            // HEADER 
            { desiredSize: new go.Size(150, 90) },
            $(go.TextBlock,
                { row: 0, column: 0, columnSpan: 3, alignment: go.Spot.Center, editable: true },
                textStyle(),
                new go.Binding("text", "key")),
            // drawn before row 1:
            $(go.RowColumnDefinition,
                { row: 1, separatorStrokeWidth: 2, separatorStroke: "black" }),

            // PROPERTIES
            $(go.TextBlock, textStyle(), { row: 1, column: 2, editable: true },
                new go.Binding("text", "prop1")),
        )
    )
);

myDiagram.nodeTemplateMap.add("NodoNormal",

    $(go.Node, "Vertical", nodeStyle(),
        $(go.TextBlock, textStyle(), { row: 1, column: 2, editable: true }, new go.Binding("text", "key")),
        $(go.Panel, "Auto",
            $(go.Shape, "Circle",
                {
                    name: "SHAPE", width: 20,
                    height: 20, fill: "white", stroke: "black", strokeWidth: 3.5
                }),
            $(go.Shape, "Circle",
                { width: 16, height: 16, strokeWidth: 0, fill: "white" },
                { portId: "", fromLinkable: true, toLinkable: true, cursor: "pointer" },
            )
        )
    )
);


myDiagram.nodeTemplateMap.add("Level",
    $(go.Node, "Vertical", nodeStyle(),
        $(go.TextBlock, textStyle(), new go.Binding("text", "key")),
        $(go.Panel, "Auto",
            $(go.Shape, "Circle", { name: "SHAPE", width: 20, height: 20, fill: "white" }),
            $(go.Shape, "Circle", { width: 16, height: 16, strokeWidth: 3.5 })
        )
    )
);

myDiagram.nodeTemplateMap.add("Medida",
    $(go.Node, "Vertical", nodeStyle(),
        $(go.TextBlock, textStyle(), { row: 1, column: 2, editable: true }, new go.Binding("text", "key")),
        $(go.Shape, "LineH", { name: "SHAPE", width: 80, height: 5, strokeWidth: 3, stroke: "black" }),
        $(go.Panel, "Auto",
            $(go.Shape, "LineH",
                { name: "SHAPE", width: 80, height: 5, strokeWidth: 3, stroke: "black" },
                { portId: "", fromLinkable: true, toLinkable: true, cursor: "pointer" }
            )
        )
    )
);

// Link templates

myDiagram.linkTemplateMap.add("linkNormal",
    $(go.Link,
        $(go.Shape, { strokeWidth: 3, stroke: "black" })
    )
);

myDiagram.linkTemplateMap.add("linkOpcional",
    $(go.Link,
        $(go.Shape, { strokeWidth: 3, stroke: "black" }),
        $(go.Panel, "Auto",
            $(go.Shape, "LineH", { strokeWidth: 3, width: 30, stroke: "black" })
        )
    )
);



function setMode(mode, itemType) {
    myDiagram.startTransaction();
    SD.itemType = itemType;
    myDiagram.commitTransaction("mode changed");
}



// initialize the Palette that is on the left side of the page
myPalette =
    new go.Palette("myPaletteDiv",  // must name or refer to the DIV HTML element
        {
            layout: $(go.GridLayout, { alignment: go.GridLayout.Location }),
            nodeTemplateMap: myDiagram.nodeTemplateMap,  // share the templates used by myDiagram
            model: new go.GraphLinksModel([  // specify the contents of the Palette
                { category: "Hecho", key: "VERBO", prop1: "propiedad" },
                { category: "NodoNormal", key: "PROPIEDAD" },
                { category: "Medida", key: "MEDIDA" },
            ],)
        });
// Diagram.model: MODEL
// create the model data that will be represented by Nodes and Links
myDiagram.model = new go.GraphLinksModel(value.objetosDelDiagrama, value.linksDelDiagrama);
