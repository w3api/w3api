---
title: ClassUnloadEvent.classSignature()
permalink: /Java/ClassUnloadEvent/classSignature/
date: 2021-01-11
key: Java.C.ClassUnloadEvent
category: Java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassUnloadEvent.metodos valor="classSignature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String classSignature()
~~~

## Clase Padre
[ClassUnloadEvent](/Java/ClassUnloadEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
