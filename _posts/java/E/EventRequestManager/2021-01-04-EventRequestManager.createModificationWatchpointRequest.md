---
title: EventRequestManager.createModificationWatchpointRequest()
permalink: Java/EventRequestManager/createModificationWatchpointRequest
date: 2021-01-04
key: JavaJava.E.EventRequestManager
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventRequestManager.metodos valor="createModificationWatchpointRequest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ModificationWatchpointRequest createModificationWatchpointRequest(Field field)
~~~

## Parámetros
* **Field field**,  {% include w3api/param_description.html metodo=_data parametro="Field field" %}

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
{%- for _ldc in site.data.Java.E.EventRequestManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
