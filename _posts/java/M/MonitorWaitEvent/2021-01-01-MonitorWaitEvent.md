---
title: MonitorWaitEvent
permalink: Java/MonitorWaitEvent
date: 2021-01-11
key: JavaJava.M.MonitorWaitEvent
category: java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorWaitEvent.description }}

## Sintaxis
~~~java
public interface MonitorWaitEvent extends LocatableEvent
~~~

## Métodos
* [monitor()](/Java/MonitorWaitEvent/monitor)
* [thread()](/Java/MonitorWaitEvent/thread)
* [timeout()](/Java/MonitorWaitEvent/timeout)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorWaitEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorWaitEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
