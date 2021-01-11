---
title: EventRequest.addCountFilter()
permalink: Java/EventRequest/addCountFilter
date: 2021-01-11
key: JavaJava.E.EventRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventRequest.metodos valor="addCountFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addCountFilter(int count)
~~~

## Parámetros
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[EventRequest](/Java/EventRequest/)

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
