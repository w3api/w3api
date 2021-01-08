---
title: FilenameFilter.accept()
permalink: Java/FilenameFilter/accept
date: 2021-01-04
key: JavaJava.F.FilenameFilter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FilenameFilter.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean accept(File dir, String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **File dir**,  {% include w3api/param_description.html metodo=_data parametro="File dir" %}

## Clase Padre
[FilenameFilter](/Java/FilenameFilter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FilenameFilter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
