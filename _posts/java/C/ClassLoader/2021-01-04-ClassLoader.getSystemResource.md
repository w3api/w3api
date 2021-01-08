---
title: ClassLoader.getSystemResource()
permalink: Java/ClassLoader/getSystemResource
date: 2021-01-04
key: JavaJava.C.ClassLoader
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="getSystemResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static URL getSystemResource(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
