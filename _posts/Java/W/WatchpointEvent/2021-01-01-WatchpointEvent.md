---
title: WatchpointEvent
permalink: /Java/WatchpointEvent/
date: 2021-01-11
key: Java.W.WatchpointEvent
category: Java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WatchpointEvent.description }}

## Sintaxis
~~~java
public interface WatchpointEvent extends LocatableEvent
~~~

## Métodos
* [field()](/Java/WatchpointEvent/field/)
* [object()](/Java/WatchpointEvent/object/)
* [valueCurrent()](/Java/WatchpointEvent/valueCurrent/)

## Ejemplo
~~~java
{{ site.data.Java.W.WatchpointEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WatchpointEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
