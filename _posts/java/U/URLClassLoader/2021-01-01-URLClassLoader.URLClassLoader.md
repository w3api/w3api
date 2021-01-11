---
title: URLClassLoader.URLClassLoader()
permalink: Java/URLClassLoader/URLClassLoader
date: 2021-01-11
key: JavaJava.U.URLClassLoader
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLClassLoader.constructores valor="URLClassLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public URLClassLoader(String name, URL[] urls, ClassLoader parent)
public URLClassLoader(String name, URL[] urls, ClassLoader parent, URLStreamHandlerFactory factory)
public URLClassLoader(URL[] urls)
public URLClassLoader(URL[] urls, ClassLoader parent)
public URLClassLoader(URL[] urls, ClassLoader parent, URLStreamHandlerFactory factory)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **URLStreamHandlerFactory factory**,  {% include w3api/param_description.html metodo=_dato parametro="URLStreamHandlerFactory factory" %}
* **ClassLoader parent**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader parent" %}
* **URL[] urls**,  {% include w3api/param_description.html metodo=_dato parametro="URL[] urls" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
