---
title: EventRequestManager
permalink: Java/EventRequestManager
date: 2021-01-11
key: JavaJava.E.EventRequestManager
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EventRequestManager.description }}

## Sintaxis
~~~java
public interface EventRequestManager extends Mirror
~~~

## Métodos
* [accessWatchpointRequests()](/Java/EventRequestManager/accessWatchpointRequests)
* [breakpointRequests()](/Java/EventRequestManager/breakpointRequests)
* [classPrepareRequests()](/Java/EventRequestManager/classPrepareRequests)
* [classUnloadRequests()](/Java/EventRequestManager/classUnloadRequests)
* [createAccessWatchpointRequest()](/Java/EventRequestManager/createAccessWatchpointRequest)
* [createBreakpointRequest()](/Java/EventRequestManager/createBreakpointRequest)
* [createClassPrepareRequest()](/Java/EventRequestManager/createClassPrepareRequest)
* [createClassUnloadRequest()](/Java/EventRequestManager/createClassUnloadRequest)
* [createExceptionRequest()](/Java/EventRequestManager/createExceptionRequest)
* [createMethodEntryRequest()](/Java/EventRequestManager/createMethodEntryRequest)
* [createMethodExitRequest()](/Java/EventRequestManager/createMethodExitRequest)
* [createModificationWatchpointRequest()](/Java/EventRequestManager/createModificationWatchpointRequest)
* [createMonitorContendedEnteredRequest()](/Java/EventRequestManager/createMonitorContendedEnteredRequest)
* [createMonitorContendedEnterRequest()](/Java/EventRequestManager/createMonitorContendedEnterRequest)
* [createMonitorWaitedRequest()](/Java/EventRequestManager/createMonitorWaitedRequest)
* [createMonitorWaitRequest()](/Java/EventRequestManager/createMonitorWaitRequest)
* [createStepRequest()](/Java/EventRequestManager/createStepRequest)
* [createThreadDeathRequest()](/Java/EventRequestManager/createThreadDeathRequest)
* [createThreadStartRequest()](/Java/EventRequestManager/createThreadStartRequest)
* [createVMDeathRequest()](/Java/EventRequestManager/createVMDeathRequest)
* [deleteAllBreakpoints()](/Java/EventRequestManager/deleteAllBreakpoints)
* [deleteEventRequest()](/Java/EventRequestManager/deleteEventRequest)
* [deleteEventRequests()](/Java/EventRequestManager/deleteEventRequests)
* [exceptionRequests()](/Java/EventRequestManager/exceptionRequests)
* [methodEntryRequests()](/Java/EventRequestManager/methodEntryRequests)
* [methodExitRequests()](/Java/EventRequestManager/methodExitRequests)
* [modificationWatchpointRequests()](/Java/EventRequestManager/modificationWatchpointRequests)
* [monitorContendedEnteredRequests()](/Java/EventRequestManager/monitorContendedEnteredRequests)
* [monitorContendedEnterRequests()](/Java/EventRequestManager/monitorContendedEnterRequests)
* [monitorWaitedRequests()](/Java/EventRequestManager/monitorWaitedRequests)
* [monitorWaitRequests()](/Java/EventRequestManager/monitorWaitRequests)
* [stepRequests()](/Java/EventRequestManager/stepRequests)
* [threadDeathRequests()](/Java/EventRequestManager/threadDeathRequests)
* [threadStartRequests()](/Java/EventRequestManager/threadStartRequests)
* [vmDeathRequests()](/Java/EventRequestManager/vmDeathRequests)

## Ejemplo
~~~java
{{ site.data.Java.E.EventRequestManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventRequestManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
