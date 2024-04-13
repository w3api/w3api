---
title: ClassPrepareRequest.addSourceNameFilter()
permalink: /Java/ClassPrepareRequest/addSourceNameFilter/
date: 2021-01-11
key: Java.C.ClassPrepareRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassPrepareRequest.metodos valor="addSourceNameFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addSourceNameFilter(String sourceNamePattern)
~~~

## Parámetros
* **String sourceNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String sourceNamePattern" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ClassPrepareRequest](/Java/ClassPrepareRequest/)

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
