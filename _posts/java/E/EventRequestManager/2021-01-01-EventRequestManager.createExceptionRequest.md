---
title: EventRequestManager.createExceptionRequest()
permalink: Java/EventRequestManager/createExceptionRequest
date: 2021-01-11
key: JavaJava.E.EventRequestManager
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventRequestManager.metodos valor="createExceptionRequest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ExceptionRequest createExceptionRequest(ReferenceType refType, boolean notifyCaught, boolean notifyUncaught)
~~~

## Parámetros
* **boolean notifyUncaught**,  {% include w3api/param_description.html metodo=_dato parametro="boolean notifyUncaught" %}
* **ReferenceType refType**,  {% include w3api/param_description.html metodo=_dato parametro="ReferenceType refType" %}
* **boolean notifyCaught**,  {% include w3api/param_description.html metodo=_dato parametro="boolean notifyCaught" %}

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
