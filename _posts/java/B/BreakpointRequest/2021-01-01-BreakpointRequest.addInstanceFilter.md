---
title: BreakpointRequest.addInstanceFilter()
permalink: Java/BreakpointRequest/addInstanceFilter
date: 2021-01-11
key: JavaJava.B.BreakpointRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BreakpointRequest.metodos valor="addInstanceFilter" %}

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
[BreakpointRequest](/Java/BreakpointRequest/)

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
