---
title: EventRequestManager.createStepRequest()
permalink: Java/EventRequestManager/createStepRequest
date: 2021-01-04
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
* **int depth**,  {% include w3api/param_description.html metodo=_data parametro="int depth" %}
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **ThreadReference thread**,  {% include w3api/param_description.html metodo=_data parametro="ThreadReference thread" %}

## Excepciones
[DuplicateRequestException](/Java/DuplicateRequestException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[EventRequestManager](/Java/EventRequestManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventRequestManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
