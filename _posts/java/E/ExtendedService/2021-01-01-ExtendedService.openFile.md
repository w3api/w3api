---
title: ExtendedService.openFile()
permalink: /Java/ExtendedService/openFile/
date: 2021-01-11
key: Java.E.ExtendedService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExtendedService.metodos valor="openFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
FileContents openFile(File file) throws IOException
~~~

## Parámetros
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}

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
