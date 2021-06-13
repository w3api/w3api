---
title: ClassLoader.findResources()
permalink: /Java/ClassLoader/findResources/
date: 2021-01-11
key: Java.C.ClassLoader
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="findResources" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Enumeration<URL> findResources(String name) throws IOException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IOException](/Java/IOException/)

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
