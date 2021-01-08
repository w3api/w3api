---
title: ACTIVITY_COMPLETED.ACTIVITY_COMPLETED()
permalink: Java/ACTIVITY_COMPLETED/ACTIVITY_COMPLETED
date: 2021-01-04
key: JavaJava.A.ACTIVITY_COMPLETED
category: java
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
* **String detailMessage**,  {% include w3api/param_description.html metodo=_data parametro="String detailMessage" %}
* **CompletionStatus completionStatus**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStatus completionStatus" %}
* **int minorCode**,  {% include w3api/param_description.html metodo=_data parametro="int minorCode" %}

## Clase Padre
[ACTIVITY_COMPLETED](/Java/ACTIVITY_COMPLETED/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ACTIVITY_COMPLETED.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
