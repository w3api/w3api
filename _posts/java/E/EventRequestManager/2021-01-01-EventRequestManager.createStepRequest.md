---
title: EventRequestManager.createStepRequest()
permalink: Java/EventRequestManager/createStepRequest
date: 2021-01-11
key: JavaJava.E.EventRequestManager
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventRequestManager.metodos valor="createStepRequest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
StepRequest createStepRequest(ThreadReference thread, int size, int depth)
~~~

## Parámetros
* **int depth**,  {% include w3api/param_description.html metodo=_dato parametro="int depth" %}
* **ThreadReference thread**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadReference thread" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [DuplicateRequestException](/Java/DuplicateRequestException/)

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
