---
title: BasicAttribute.BasicAttribute()
permalink: /Java/BasicAttribute/BasicAttribute/
date: 2021-01-11
key: Java.B.BasicAttribute
category: Java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicAttribute.constructores valor="BasicAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BasicAttribute(String id)
public BasicAttribute(String id, boolean ordered)
public BasicAttribute(String id, Object value)
public BasicAttribute(String id, Object value, boolean ordered)
~~~

## Parámetros
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **boolean ordered**,  {% include w3api/param_description.html metodo=_dato parametro="boolean ordered" %}

## Clase Padre
[BasicAttribute](/Java/BasicAttribute/)

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
