---
title: URLClassLoader.findClass()
permalink: /Java/URLClassLoader/findClass/
date: 2021-01-11
key: Java.U.URLClassLoader
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLClassLoader.metodos valor="findClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Class<?> findClass(String name) throws ClassNotFoundException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URLClassLoader](/Java/URLClassLoader/)

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
