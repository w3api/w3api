---
title: NO_RESPONSE.NO_RESPONSE()
permalink: /Java/NO_RESPONSE/NO_RESPONSE/
date: 2021-01-11
key: Java.N.NO_RESPONSE
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NO_RESPONSE.constructores valor="NO_RESPONSE" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NO_RESPONSE()
public NO_RESPONSE(int minor, CompletionStatus completed)
public NO_RESPONSE(String s)
public NO_RESPONSE(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completed" %}
* **int minor**,  {% include w3api/param_description.html metodo=_dato parametro="int minor" %}

## Clase Padre
[NO_RESPONSE](/Java/NO_RESPONSE/)

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
