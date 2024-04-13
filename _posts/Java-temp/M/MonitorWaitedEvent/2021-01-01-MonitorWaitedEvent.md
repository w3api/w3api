---
title: MonitorWaitedEvent
permalink: /Java/MonitorWaitedEvent/
date: 2021-01-11
key: Java.M.MonitorWaitedEvent
category: Java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorWaitedEvent.description }}

## Sintaxis
~~~java
public interface MonitorWaitedEvent extends LocatableEvent
~~~

## Métodos
* [monitor()](/Java/MonitorWaitedEvent/monitor)
* [thread()](/Java/MonitorWaitedEvent/thread)
* [timedout()](/Java/MonitorWaitedEvent/timedout)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorWaitedEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorWaitedEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
