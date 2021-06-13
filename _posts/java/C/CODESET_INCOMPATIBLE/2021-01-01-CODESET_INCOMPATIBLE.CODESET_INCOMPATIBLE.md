---
title: CODESET_INCOMPATIBLE.CODESET_INCOMPATIBLE()
permalink: /Java/CODESET_INCOMPATIBLE/CODESET_INCOMPATIBLE/
date: 2021-01-11
key: Java.C.CODESET_INCOMPATIBLE
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CODESET_INCOMPATIBLE.constructores valor="CODESET_INCOMPATIBLE" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CODESET_INCOMPATIBLE()
public CODESET_INCOMPATIBLE(int minorCode, CompletionStatus completionStatus)
public CODESET_INCOMPATIBLE(String detailMessage)
public CODESET_INCOMPATIBLE(String detailMessage, int minorCode, CompletionStatus completionStatus)
~~~

## Parámetros
* **CompletionStatus completionStatus**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completionStatus" %}
* **String detailMessage**,  {% include w3api/param_description.html metodo=_dato parametro="String detailMessage" %}
* **int minorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int minorCode" %}

## Clase Padre
[CODESET_INCOMPATIBLE](/Java/CODESET_INCOMPATIBLE/)

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
