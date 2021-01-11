---
title: EventRequest.setEnabled()
permalink: Java/EventRequest/setEnabled
date: 2021-01-11
key: JavaJava.E.EventRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventRequest.metodos valor="setEnabled" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setEnabled(boolean val)
~~~

## Parámetros
* **boolean val**,  {% include w3api/param_description.html metodo=_dato parametro="boolean val" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/), [IllegalThreadStateException](/Java/IllegalThreadStateException/)

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
