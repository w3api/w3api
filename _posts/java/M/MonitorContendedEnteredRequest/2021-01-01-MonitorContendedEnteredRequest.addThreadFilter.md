---
title: MonitorContendedEnteredRequest.addThreadFilter()
permalink: /Java/MonitorContendedEnteredRequest/addThreadFilter/
date: 2021-01-11
key: Java.M.MonitorContendedEnteredRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MonitorContendedEnteredRequest.metodos valor="addThreadFilter" %}

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
[MonitorContendedEnteredRequest](/Java/MonitorContendedEnteredRequest/)

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
