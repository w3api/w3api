---
title: MonitorContendedEnteredEvent
permalink: /Java/MonitorContendedEnteredEvent/
date: 2021-01-11
key: Java.M.MonitorContendedEnteredEvent
category: Java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorContendedEnteredEvent.description }}

## Sintaxis
~~~java
public interface MonitorContendedEnteredEvent extends LocatableEvent
~~~

## Métodos
* [monitor()](/Java/MonitorContendedEnteredEvent/monitor)
* [thread()](/Java/MonitorContendedEnteredEvent/thread)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorContendedEnteredEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorContendedEnteredEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
