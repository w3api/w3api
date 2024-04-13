---
title: ACTIVITY_REQUIRED.ACTIVITY_REQUIRED()
permalink: /Java/ACTIVITY_REQUIRED/ACTIVITY_REQUIRED/
date: 2021-01-11
key: Java.A.ACTIVITY_REQUIRED
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ACTIVITY_REQUIRED.constructores valor="ACTIVITY_REQUIRED" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ACTIVITY_REQUIRED()
public ACTIVITY_REQUIRED(int minorCode, CompletionStatus completionStatus)
public ACTIVITY_REQUIRED(String detailMessage)
public ACTIVITY_REQUIRED(String detailMessage, int minorCode, CompletionStatus completionStatus)
~~~

## Parámetros
* **CompletionStatus completionStatus**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completionStatus" %}
* **String detailMessage**,  {% include w3api/param_description.html metodo=_dato parametro="String detailMessage" %}
* **int minorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int minorCode" %}

## Clase Padre
[ACTIVITY_REQUIRED](/Java/ACTIVITY_REQUIRED/)

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
