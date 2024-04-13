---
title: LocatableEvent
permalink: /Java/LocatableEvent/
date: 2021-01-11
key: Java.L.LocatableEvent
category: Java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LocatableEvent.description }}

## Sintaxis
~~~java
public interface LocatableEvent extends Event, Locatable
~~~

## Métodos
* [thread()](/Java/LocatableEvent/thread/)

## Ejemplo
~~~java
{{ site.data.Java.L.LocatableEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocatableEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
