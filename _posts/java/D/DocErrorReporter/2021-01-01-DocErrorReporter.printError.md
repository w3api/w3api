---
title: DocErrorReporter.printError()
permalink: /Java/DocErrorReporter/printError/
date: 2021-01-11
key: Java.D.DocErrorReporter
category: Java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocErrorReporter.metodos valor="printError" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void printError(SourcePosition pos, String msg)
void printError(String msg)
~~~

## Parámetros
* **SourcePosition pos**,  {% include w3api/param_description.html metodo=_dato parametro="SourcePosition pos" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}

## Clase Padre
[DocErrorReporter](/Java/DocErrorReporter/)

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
