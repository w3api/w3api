---
title: URLClassLoader.newInstance()
permalink: Java/URLClassLoader/newInstance
date: 2021-01-04
key: JavaJava.U.URLClassLoader
category: java
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
* **ClassLoader parent**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader parent" %}
* **URL[] urls**,  {% include w3api/param_description.html metodo=_data parametro="URL[] urls" %}

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
{%- for _ldc in site.data.Java.U.URLClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
