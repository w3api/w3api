---
title: BreakpointRequest.addThreadFilter()
permalink: /Java/BreakpointRequest/addThreadFilter/
date: 2021-01-11
key: Java.B.BreakpointRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BreakpointRequest.metodos valor="addThreadFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addThreadFilter(ThreadReference thread)
~~~

## Parámetros
* **ThreadReference thread**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadReference thread" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/)

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
