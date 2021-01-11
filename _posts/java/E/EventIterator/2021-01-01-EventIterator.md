---
title: EventIterator
permalink: Java/EventIterator
date: 2021-01-11
key: JavaJava.E.EventIterator
category: java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EventIterator.description }}

## Sintaxis
~~~java
public interface EventIterator extends Iterator<Event>
~~~

## Métodos
* [nextEvent()](/Java/EventIterator/nextEvent)

## Ejemplo
~~~java
{{ site.data.Java.E.EventIterator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventIterator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
