---
title: ClassUnloadEvent
permalink: Java/ClassUnloadEvent
date: 2021-01-04
key: JavaJava.C.ClassUnloadEvent
category: java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassUnloadEvent.description }}

## Sintaxis
~~~java
public interface ClassUnloadEvent extends Event
~~~

## Métodos
* [className()](/Java/ClassUnloadEvent/className)
* [classSignature()](/Java/ClassUnloadEvent/classSignature)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassUnloadEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassUnloadEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
