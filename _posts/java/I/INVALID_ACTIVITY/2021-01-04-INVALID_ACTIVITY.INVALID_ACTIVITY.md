---
title: INVALID_ACTIVITY.INVALID_ACTIVITY()
permalink: Java/INVALID_ACTIVITY/INVALID_ACTIVITY
date: 2021-01-04
key: JavaJava.I.INVALID_ACTIVITY
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.INVALID_ACTIVITY.constructores valor="INVALID_ACTIVITY" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public INVALID_ACTIVITY()
public INVALID_ACTIVITY(int minorCode, CompletionStatus completionStatus)
public INVALID_ACTIVITY(String detailMessage)
public INVALID_ACTIVITY(String detailMessage, int minorCode, CompletionStatus completionStatus)
~~~

## Parámetros
* **String detailMessage**,  {% include w3api/param_description.html metodo=_data parametro="String detailMessage" %}
* **CompletionStatus completionStatus**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStatus completionStatus" %}
* **int minorCode**,  {% include w3api/param_description.html metodo=_data parametro="int minorCode" %}

## Clase Padre
[INVALID_ACTIVITY](/Java/INVALID_ACTIVITY/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.INVALID_ACTIVITY.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
