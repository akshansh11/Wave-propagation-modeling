# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def wave():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(100.0, 100.0))
    p = mdb.models['Model-1'].Part(name='plate', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['plate']
    p.BaseSolidExtrude(sketch=s, depth=1.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['plate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['plate']
    p.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=10.0)
    p = mdb.models['Model-1'].parts['plate']
    p.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=90.0)
    p = mdb.models['Model-1'].parts['plate']
    p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=10.0)
    p = mdb.models['Model-1'].parts['plate']
    p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=90.0)
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    p = mdb.models['Model-1'].parts['plate']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[2], cells=pickedCells)
    p = mdb.models['Model-1'].parts['plate']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[5], cells=pickedCells)
    p = mdb.models['Model-1'].parts['plate']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[3], cells=pickedCells)
    p = mdb.models['Model-1'].parts['plate']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#2c ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[4], cells=pickedCells)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['plate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models['Model-1'].Material(name='Aluminium')
    mdb.models['Model-1'].materials['Aluminium'].Density(table=((2.5e-09, ), ))
    mdb.models['Model-1'].materials['Aluminium'].Elastic(table=((62000.0, 0.33), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='aluminium', 
        material='Aluminium', thickness=None)
    p = mdb.models['Model-1'].parts['plate']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1ff ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Model-1'].parts['plate']
    p.SectionAssignment(region=region, sectionName='aluminium', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['plate']
    a.Instance(name='plate-1', part=p, dependent=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
        timePeriod=0.0001, maxIncrement=1e-07, improvedDtMethod=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=239.43, 
        farPlane=399.803, width=177.997, height=78.0299, viewOffsetX=2.38273, 
        viewOffsetY=-5.1888)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=246.259, 
        farPlane=398.45, width=183.074, height=80.2555, cameraPosition=(
        -12.3666, -241.943, 122.155), cameraUpVector=(-0.666628, 0.661599, 
        0.343356), cameraTarget=(50.6184, 46.3154, -0.705273), 
        viewOffsetX=2.45069, viewOffsetY=-5.3368)
    session.viewports['Viewport: 1'].view.setValues(width=168.137, height=73.7076, 
        viewOffsetX=4.43493, viewOffsetY=-6.43799)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=240.438, 
        farPlane=404.582, width=168.022, height=73.657, cameraUpVector=(
        -0.23942, 0.563587, 0.790599), cameraTarget=(57.8361, 46.3081, 9.1784), 
        viewOffsetX=4.43189, viewOffsetY=-6.43357)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=249.681, 
        farPlane=414.344, width=174.481, height=76.4885, cameraPosition=(
        140.168, 369.434, -14.3996), cameraUpVector=(0.0653265, -0.32164, 
        0.944606), cameraTarget=(63.6955, 59.4634, 5.7859), 
        viewOffsetX=4.60225, viewOffsetY=-6.68088)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=257.428, 
        farPlane=399.252, width=179.894, height=78.8617, cameraPosition=(
        -276.421, 62.9346, 34.7476), cameraUpVector=(0.437775, 0.267045, 
        0.85851), cameraTarget=(42.1827, 57.6625, 6.44467), 
        viewOffsetX=4.74504, viewOffsetY=-6.88816)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['plate-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#5050048 #fa ]', ), )
    region = a.Set(faces=faces1, name='Set-1')
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', 
        region=region, u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    a = mdb.models['Model-1'].rootAssembly
    a.DatumPointByCoordinate(coords=(10.0, 90.0, 1.0))
    a = mdb.models['Model-1'].rootAssembly
    a.DatumPointByCoordinate(coords=(90.0, 10.0, 1.0))
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['plate-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#1000 ]', ), )
    a.Set(vertices=verts1, name='front')
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['plate-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#10 ]', ), )
    a.Set(vertices=verts1, name='sensor')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (2e-06, -1.0), (4e-06, 1.0), (
        6e-06, -1.0), (8e-06, 1.0), (1e-05, 0.0)))
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['front']
    mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
        region=region, cf3=1.0, amplitude='Amp-1', distributionType=UNIFORM, 
        field='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].FieldOutputRequest(name='F-Output-2', 
        createStepName='Step-1', variables=('U', ), numIntervals=100)
    regionDef=mdb.models['Model-1'].rootAssembly.sets['sensor']
    mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-2', 
        createStepName='Step-1', variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 
        'UR3'), frequency=1, region=regionDef, sectionPoints=DEFAULT, 
        rebar=EXCLUDE)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
        adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['plate-1'], )
    a.seedPartInstance(regions=partInstances, size=1.0, deviationFactor=0.1, 
        minSizeFactor=0.1)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['plate-1'], )
    a.generateMesh(regions=partInstances)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['plate-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1ff ]', ), )
    pickedRegions =(cells1, )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=234.03, 
        farPlane=405.203, width=236.468, height=103.924, 
        viewOffsetX=-3.8147e-06, viewOffsetY=-7.62939e-06)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, explicitPrecision=DOUBLE, 
        nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
        contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
        resultsFormat=ODB, numDomains=1, activateLoadBalancing=False, 
        numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, numCpus=1)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='Y:/Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        visibleEdges=FEATURE)
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.mdbData.summary()
    session.viewports['Viewport: 1'].setValues(
        displayedObject=session.odbs['Y:/Job-1.odb'])
    o3 = session.openOdb(name='Y:/Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=210.844, 
        farPlane=370.277, width=236.445, height=99.6042, viewOffsetX=1.3509, 
        viewOffsetY=0.0390314)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        UNDEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        UNDEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        SYMBOLS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
        'Magnitude'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), 
        )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
        'Magnitude'), )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=11 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=12 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=13 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=14 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=15 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=16 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=17 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=18 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=19 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=20 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=21 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=22 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=23 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=24 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=25 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=26 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=27 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=28 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=29 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=30 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=31 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=32 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=33 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=34 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=35 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=36 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=37 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=38 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=39 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=40 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=41 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=42 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=43 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=44 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=45 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=46 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=47 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=48 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=49 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=50 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=51 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=52 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=53 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=54 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=55 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=56 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=57 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=58 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=59 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=60 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=61 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=62 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=63 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=64 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=65 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=66 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=67 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=68 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=69 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=70 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=71 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=72 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=73 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=74 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=75 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=76 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=77 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=78 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=79 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=80 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=81 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=82 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=83 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=84 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=85 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=86 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=87 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=88 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=89 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=90 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=91 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=92 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=93 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=94 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=95 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=96 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=97 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=98 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=99 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
    session.Viewport(name='Viewport: 2', origin=(6.625, 5.10185146331787), 
        width=391.703125, height=178.564804077148)
    session.viewports['Viewport: 2'].makeCurrent()
    session.viewports['Viewport: 2'].maximize()
    session.viewports['Viewport: 1'].restore()
    session.viewports['Viewport: 2'].restore()
    session.viewports['Viewport: 1'].setValues(origin=(0.0, 5.10185241699219), 
        width=219.453109741211, height=185.009246826172)
    session.viewports['Viewport: 2'].setValues(origin=(219.453109741211, 
        5.10185241699219), width=219.453109741211, height=185.009246826172)
    session.viewports['Viewport: 2'].odbDisplay.setFrame(step=0, frame=0 )
    session.Viewport(name='Viewport: 3', origin=(13.25, 5.10185146331787), 
        width=391.703125, height=172.120361328125)
    session.viewports['Viewport: 3'].makeCurrent()
    session.viewports['Viewport: 1'].setValues(width=146.30207824707)
    session.viewports['Viewport: 2'].setValues(origin=(146.30207824707, 
        5.10185241699219), width=146.30207824707)
    session.viewports['Viewport: 3'].setValues(origin=(292.604156494141, 
        5.10185241699219), width=146.30207824707, height=185.009246826172)
    session.viewports['Viewport: 3'].odbDisplay.setFrame(step=0, frame=0 )
    session.Viewport(name='Viewport: 4', origin=(19.875, 5.10185146331787), 
        width=391.703125, height=165.675918579102)
    session.viewports['Viewport: 4'].makeCurrent()
    session.viewports['Viewport: 1'].setValues(origin=(0.0, 97.7407302856445), 
        width=219.453109741211, height=92.3703689575195)
    session.viewports['Viewport: 2'].setValues(origin=(219.453109741211, 
        97.7407302856445), width=219.453109741211, height=92.3703689575195)
    session.viewports['Viewport: 3'].setValues(origin=(0.0, 5.37036895751953), 
        width=219.453109741211, height=92.3703689575195)
    session.viewports['Viewport: 4'].setValues(origin=(219.453109741211, 
        5.37036895751953), width=219.453109741211, height=92.3703689575195)
    session.viewports['Viewport: 4'].odbDisplay.setFrame(step=0, frame=0 )
    session.viewports['Viewport: 1'].makeCurrent()
    session. linkedViewportCommands.setValues(linkViewports=True)
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendFont='-*-verdana-medium-r-normal-*-*-80-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        titleFont='-*-verdana-medium-r-normal-*-*-80-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session. linkedViewportCommands.setValues(linkViewports=False)
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=11 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=12 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=13 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=14 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=15 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=16 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=17 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=18 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=19 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=20 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=21 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=22 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=23 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=24 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=25 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=26 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=27 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=28 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=29 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=30 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=31 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=32 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=33 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=34 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=35 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=36 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=37 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=38 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=39 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=40 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=41 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=42 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=43 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=44 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=45 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=46 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=47 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=48 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=49 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=50 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=51 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=52 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=53 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=54 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=55 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=56 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=57 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=58 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=59 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=60 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=61 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=62 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=63 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=64 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=65 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=66 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=67 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=68 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=69 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=70 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=71 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=72 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=73 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=74 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=75 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=76 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=77 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=78 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=79 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=80 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=81 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=82 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=83 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=84 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=85 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=86 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=87 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=88 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=89 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=90 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=91 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=92 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=93 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=94 )


