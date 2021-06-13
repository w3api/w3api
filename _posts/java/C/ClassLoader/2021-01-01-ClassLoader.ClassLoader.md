---
title: ClassLoader.ClassLoader()
permalink: /Java/ClassLoader/ClassLoader/
date: 2021-01-11
key: Java.C.ClassLoader
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.constructores valor="ClassLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ClassLoader()
protected ClassLoader(ClassLoader parent)
protected ClassLoader(String name, ClassLoader parent)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ClassLoader parent**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader parent" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
