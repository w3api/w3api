---
title: ExceptionRequest.addInstanceFilter()
permalink: Java/ExceptionRequest/addInstanceFilter
date: 2021-01-11
key: JavaJava.E.ExceptionRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExceptionRequest.metodos valor="addInstanceFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addInstanceFilter(ObjectReference instance)
~~~

## Parámetros
* **ObjectReference instance**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectReference instance" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ExceptionRequest](/Java/ExceptionRequest/)

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
