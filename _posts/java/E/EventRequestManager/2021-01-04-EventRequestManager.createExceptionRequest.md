---
title: EventRequestManager.createExceptionRequest()
permalink: Java/EventRequestManager/createExceptionRequest
date: 2021-01-04
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
* **ReferenceType refType**,  {% include w3api/param_description.html metodo=_data parametro="ReferenceType refType" %}
* **boolean notifyCaught**,  {% include w3api/param_description.html metodo=_data parametro="boolean notifyCaught" %}
* **boolean notifyUncaught**,  {% include w3api/param_description.html metodo=_data parametro="boolean notifyUncaught" %}

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
