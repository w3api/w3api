---
title: URLClassLoader.findResource()
permalink: Java/URLClassLoader/findResource
date: 2021-01-04
key: JavaJava.U.URLClassLoader
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLClassLoader.metodos valor="findResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public URL findResource(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

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
