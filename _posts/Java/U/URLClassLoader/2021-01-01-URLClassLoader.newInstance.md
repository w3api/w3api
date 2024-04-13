---
title: URLClassLoader.newInstance()
permalink: /Java/URLClassLoader/newInstance/
date: 2021-01-11
key: Java.U.URLClassLoader
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLClassLoader.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static URLClassLoader newInstance(URL[] urls)
public static URLClassLoader newInstance(URL[] urls, ClassLoader parent)
~~~

## Parámetros
* **URL[] urls**,  {% include w3api/param_description.html metodo=_dato parametro="URL[] urls" %}
* **ClassLoader parent**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader parent" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
