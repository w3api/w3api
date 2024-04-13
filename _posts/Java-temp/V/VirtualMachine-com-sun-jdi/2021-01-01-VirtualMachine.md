---
title: VirtualMachine
permalink: /Java/VirtualMachine-com-sun-jdi/
date: 2021-01-11
key: Java.V.VirtualMachine-com-sun-jdi
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.V.VirtualMachine-com-sun-jdi.description }}

## Sintaxis
~~~java
public interface VirtualMachine extends Mirror
~~~

## Campos
* [TRACE_ALL](/Java/VirtualMachine-com-sun-jdi/TRACE_ALL)
* [TRACE_EVENTS](/Java/VirtualMachine-com-sun-jdi/TRACE_EVENTS)
* [TRACE_NONE](/Java/VirtualMachine-com-sun-jdi/TRACE_NONE)
* [TRACE_OBJREFS](/Java/VirtualMachine-com-sun-jdi/TRACE_OBJREFS)
* [TRACE_RECEIVES](/Java/VirtualMachine-com-sun-jdi/TRACE_RECEIVES)
* [TRACE_REFTYPES](/Java/VirtualMachine-com-sun-jdi/TRACE_REFTYPES)
* [TRACE_SENDS](/Java/VirtualMachine-com-sun-jdi/TRACE_SENDS)

## Métodos
* [allClasses()](/Java/VirtualMachine-com-sun-jdi/allClasses)
* [allModules()](/Java/VirtualMachine-com-sun-jdi/allModules)
* [allThreads()](/Java/VirtualMachine-com-sun-jdi/allThreads)
* [canAddMethod()](/Java/VirtualMachine-com-sun-jdi/canAddMethod)
* [canBeModified()](/Java/VirtualMachine-com-sun-jdi/canBeModified)
* [canForceEarlyReturn()](/Java/VirtualMachine-com-sun-jdi/canForceEarlyReturn)
* [canGetBytecodes()](/Java/VirtualMachine-com-sun-jdi/canGetBytecodes)
* [canGetClassFileVersion()](/Java/VirtualMachine-com-sun-jdi/canGetClassFileVersion)
* [canGetConstantPool()](/Java/VirtualMachine-com-sun-jdi/canGetConstantPool)
* [canGetCurrentContendedMonitor()](/Java/VirtualMachine-com-sun-jdi/canGetCurrentContendedMonitor)
* [canGetInstanceInfo()](/Java/VirtualMachine-com-sun-jdi/canGetInstanceInfo)
* [canGetMethodReturnValues()](/Java/VirtualMachine-com-sun-jdi/canGetMethodReturnValues)
* [canGetModuleInfo()](/Java/VirtualMachine-com-sun-jdi/canGetModuleInfo)
* [canGetMonitorFrameInfo()](/Java/VirtualMachine-com-sun-jdi/canGetMonitorFrameInfo)
* [canGetMonitorInfo()](/Java/VirtualMachine-com-sun-jdi/canGetMonitorInfo)
* [canGetOwnedMonitorInfo()](/Java/VirtualMachine-com-sun-jdi/canGetOwnedMonitorInfo)
* [canGetSourceDebugExtension()](/Java/VirtualMachine-com-sun-jdi/canGetSourceDebugExtension)
* [canGetSyntheticAttribute()](/Java/VirtualMachine-com-sun-jdi/canGetSyntheticAttribute)
* [canPopFrames()](/Java/VirtualMachine-com-sun-jdi/canPopFrames)
* [canRedefineClasses()](/Java/VirtualMachine-com-sun-jdi/canRedefineClasses)
* [canRequestMonitorEvents()](/Java/VirtualMachine-com-sun-jdi/canRequestMonitorEvents)
* [canRequestVMDeathEvent()](/Java/VirtualMachine-com-sun-jdi/canRequestVMDeathEvent)
* [canUnrestrictedlyRedefineClasses()](/Java/VirtualMachine-com-sun-jdi/canUnrestrictedlyRedefineClasses)
* [canUseInstanceFilters()](/Java/VirtualMachine-com-sun-jdi/canUseInstanceFilters)
* [canUseSourceNameFilters()](/Java/VirtualMachine-com-sun-jdi/canUseSourceNameFilters)
* [canWatchFieldAccess()](/Java/VirtualMachine-com-sun-jdi/canWatchFieldAccess)
* [canWatchFieldModification()](/Java/VirtualMachine-com-sun-jdi/canWatchFieldModification)
* [classesByName()](/Java/VirtualMachine-com-sun-jdi/classesByName)
* [description()](/Java/VirtualMachine-com-sun-jdi/description)
* [dispose()](/Java/VirtualMachine-com-sun-jdi/dispose)
* [eventQueue()](/Java/VirtualMachine-com-sun-jdi/eventQueue)
* [eventRequestManager()](/Java/VirtualMachine-com-sun-jdi/eventRequestManager)
* [exit()](/Java/VirtualMachine-com-sun-jdi/exit)
* [getDefaultStratum()](/Java/VirtualMachine-com-sun-jdi/getDefaultStratum)
* [instanceCounts()](/Java/VirtualMachine-com-sun-jdi/instanceCounts)
* [mirrorOf()](/Java/VirtualMachine-com-sun-jdi/mirrorOf)
* [mirrorOfVoid()](/Java/VirtualMachine-com-sun-jdi/mirrorOfVoid)
* [name()](/Java/VirtualMachine-com-sun-jdi/name)
* [process()](/Java/VirtualMachine-com-sun-jdi/process)
* [redefineClasses()](/Java/VirtualMachine-com-sun-jdi/redefineClasses)
* [resume()](/Java/VirtualMachine-com-sun-jdi/resume)
* [setDebugTraceMode()](/Java/VirtualMachine-com-sun-jdi/setDebugTraceMode)
* [setDefaultStratum()](/Java/VirtualMachine-com-sun-jdi/setDefaultStratum)
* [suspend()](/Java/VirtualMachine-com-sun-jdi/suspend)
* [topLevelThreadGroups()](/Java/VirtualMachine-com-sun-jdi/topLevelThreadGroups)
* [version()](/Java/VirtualMachine-com-sun-jdi/version)

## Ejemplo
~~~java
{{ site.data.Java.V.VirtualMachine-com-sun-jdi.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VirtualMachine-com-sun-jdi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
