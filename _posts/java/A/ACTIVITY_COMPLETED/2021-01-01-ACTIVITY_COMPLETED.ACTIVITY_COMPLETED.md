---
title: ACTIVITY_COMPLETED.ACTIVITY_COMPLETED()
permalink: /Java/ACTIVITY_COMPLETED/ACTIVITY_COMPLETED/
date: 2021-01-11
key: Java.A.ACTIVITY_COMPLETED
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ACTIVITY_COMPLETED.constructores valor="ACTIVITY_COMPLETED" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ACTIVITY_COMPLETED()
public ACTIVITY_COMPLETED(int minorCode, CompletionStatus completionStatus)
public ACTIVITY_COMPLETED(String detailMessage)
public ACTIVITY_COMPLETED(String detailMessage, int minorCode, CompletionStatus completionStatus)
~~~

## Parámetros
* **CompletionStatus completionStatus**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completionStatus" %}
* **String detailMessage**,  {% include w3api/param_description.html metodo=_dato parametro="String detailMessage" %}
* **int minorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int minorCode" %}

## Clase Padre
[ACTIVITY_COMPLETED](/Java/ACTIVITY_COMPLETED/)

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
