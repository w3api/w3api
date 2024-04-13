---
title: DirectoryStream.Filter.accept()
permalink: /Java/DirectoryStream/Filter/accept/
date: 2021-01-11
key: Java.D.DirectoryStream.Filter
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectoryStream.Filter.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean accept(T entry) throws IOException
~~~

## Parámetros
* **T entry**,  {% include w3api/param_description.html metodo=_dato parametro="T entry" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[DirectoryStream.Filter](/Java/DirectoryStream/Filter/)

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
