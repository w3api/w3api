---
title: EventRequest.setSuspendPolicy()
permalink: Java/EventRequest/setSuspendPolicy
date: 2021-01-04
key: JavaJava.E.EventRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventRequest.metodos valor="setSuspendPolicy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setSuspendPolicy(int policy)
~~~

## Parámetros
* **int policy**,  {% include w3api/param_description.html metodo=_data parametro="int policy" %}

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
{%- for _ldc in site.data.Java.E.EventRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
