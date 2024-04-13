---
title: ClassPrepareEvent
permalink: /Java/ClassPrepareEvent/
date: 2021-01-11
key: Java.C.ClassPrepareEvent
category: Java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassPrepareEvent.description }}

## Sintaxis
~~~java
public interface ClassPrepareEvent extends Event
~~~

## Métodos
* [referenceType()](/Java/ClassPrepareEvent/referenceType/)
* [thread()](/Java/ClassPrepareEvent/thread/)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassPrepareEvent.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ClassPrepareEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
