---
title: ClassLoader.getParent()
permalink: /Java/ClassLoader/getParent/
date: 2021-01-11
key: Java.C.ClassLoader
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="getParent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final ClassLoader getParent()
~~~

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

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
