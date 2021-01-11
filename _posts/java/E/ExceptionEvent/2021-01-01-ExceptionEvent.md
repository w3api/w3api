---
title: ExceptionEvent
permalink: Java/ExceptionEvent
date: 2021-01-11
key: JavaJava.E.ExceptionEvent
category: java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExceptionEvent.description }}

## Sintaxis
~~~java
public interface ExceptionEvent extends LocatableEvent
~~~

## Métodos
* [catchLocation()](/Java/ExceptionEvent/catchLocation)
* [exception()](/Java/ExceptionEvent/exception)

## Ejemplo
~~~java
{{ site.data.Java.E.ExceptionEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExceptionEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
