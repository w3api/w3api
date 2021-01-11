---
title: EventRequestManager.createBreakpointRequest()
permalink: Java/EventRequestManager/createBreakpointRequest
date: 2021-01-11
key: JavaJava.E.EventRequestManager
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventRequestManager.metodos valor="createBreakpointRequest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
BreakpointRequest createBreakpointRequest(Location location)
~~~

## Parámetros
* **Location location**,  {% include w3api/param_description.html metodo=_dato parametro="Location location" %}

## Excepciones
[NativeMethodException](/Java/NativeMethodException/)

## Clase Padre
[EventRequestManager](/Java/EventRequestManager/)

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
