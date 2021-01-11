---
title: ClassLoader.findLibrary()
permalink: Java/ClassLoader/findLibrary
date: 2021-01-11
key: JavaJava.C.ClassLoader
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="findLibrary" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected String findLibrary(String libname)
~~~

## Parámetros
* **String libname**,  {% include w3api/param_description.html metodo=_dato parametro="String libname" %}

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
