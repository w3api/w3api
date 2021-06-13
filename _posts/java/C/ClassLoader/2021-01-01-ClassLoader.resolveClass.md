---
title: ClassLoader.resolveClass()
permalink: /Java/ClassLoader/resolveClass/
date: 2021-01-11
key: Java.C.ClassLoader
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="resolveClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void resolveClass(Class<?> c)
~~~

## Parámetros
* **Class&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> c" %}

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
