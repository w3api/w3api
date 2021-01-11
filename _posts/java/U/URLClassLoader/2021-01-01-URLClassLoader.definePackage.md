---
title: URLClassLoader.definePackage()
permalink: Java/URLClassLoader/definePackage
date: 2021-01-11
key: JavaJava.U.URLClassLoader
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLClassLoader.metodos valor="definePackage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Package definePackage(String name, Manifest man, URL url)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **Manifest man**,  {% include w3api/param_description.html metodo=_dato parametro="Manifest man" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
