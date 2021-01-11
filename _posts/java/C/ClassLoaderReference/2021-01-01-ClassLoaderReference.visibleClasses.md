---
title: ClassLoaderReference.visibleClasses()
permalink: Java/ClassLoaderReference/visibleClasses
date: 2021-01-11
key: JavaJava.C.ClassLoaderReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoaderReference.metodos valor="visibleClasses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<ReferenceType> visibleClasses()
~~~

## Clase Padre
[ClassLoaderReference](/Java/ClassLoaderReference/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
