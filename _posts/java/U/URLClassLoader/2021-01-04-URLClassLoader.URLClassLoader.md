---
title: URLClassLoader.URLClassLoader()
permalink: Java/URLClassLoader/URLClassLoader
date: 2021-01-04
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
* **ClassLoader parent**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader parent" %}
* **URLStreamHandlerFactory factory**,  {% include w3api/param_description.html metodo=_data parametro="URLStreamHandlerFactory factory" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **URL[] urls**,  {% include w3api/param_description.html metodo=_data parametro="URL[] urls" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[URLClassLoader](/Java/URLClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.URLClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
