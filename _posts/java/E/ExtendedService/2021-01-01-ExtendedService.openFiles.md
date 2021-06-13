---
title: ExtendedService.openFiles()
permalink: /Java/ExtendedService/openFiles/
date: 2021-01-11
key: Java.E.ExtendedService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExtendedService.metodos valor="openFiles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
FileContents[] openFiles(File[] files) throws IOException
~~~

## Parámetros
* **File[] files**,  {% include w3api/param_description.html metodo=_dato parametro="File[] files" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ExtendedService](/Java/ExtendedService/)

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
