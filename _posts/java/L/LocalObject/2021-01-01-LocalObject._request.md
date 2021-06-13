---
title: LocalObject._request()
permalink: Java/LocalObject/_request
date: 2021-01-11
key: Java.L.LocalObject
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalObject.metodos valor="_request" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Request _request(String operation)
public OutputStream _request(String operation, boolean responseExpected)
~~~

## Parámetros
* **String operation**,  {% include w3api/param_description.html metodo=_dato parametro="String operation" %}
* **boolean responseExpected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean responseExpected" %}

## Clase Padre
[LocalObject](/Java/LocalObject/)

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
