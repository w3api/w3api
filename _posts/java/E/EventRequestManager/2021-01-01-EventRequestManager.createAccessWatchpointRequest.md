---
title: EventRequestManager.createAccessWatchpointRequest()
permalink: /Java/EventRequestManager/createAccessWatchpointRequest/
date: 2021-01-11
key: Java.E.EventRequestManager
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventRequestManager.metodos valor="createAccessWatchpointRequest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AccessWatchpointRequest createAccessWatchpointRequest(Field field)
~~~

## Parámetros
* **Field field**,  {% include w3api/param_description.html metodo=_dato parametro="Field field" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
