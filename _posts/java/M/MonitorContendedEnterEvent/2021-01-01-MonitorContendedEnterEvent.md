---
title: MonitorContendedEnterEvent
permalink: Java/MonitorContendedEnterEvent
date: 2021-01-11
key: JavaJava.M.MonitorContendedEnterEvent
category: java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MonitorContendedEnterEvent.description }}

## Sintaxis
~~~java
public interface MonitorContendedEnterEvent extends LocatableEvent
~~~

## Métodos
* [monitor()](/Java/MonitorContendedEnterEvent/monitor)
* [thread()](/Java/MonitorContendedEnterEvent/thread)

## Ejemplo
~~~java
{{ site.data.Java.M.MonitorContendedEnterEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorContendedEnterEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
