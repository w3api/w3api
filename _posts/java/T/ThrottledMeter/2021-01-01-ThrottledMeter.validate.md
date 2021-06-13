---
title: ThrottledMeter.validate()
permalink: /Java/ThrottledMeter/validate/
date: 2021-01-11
key: Java.T.ThrottledMeter
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThrottledMeter.metodos valor="validate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long validate(long previous, long amount, ResourceId id)
~~~

## Parámetros
* **long previous**,  {% include w3api/param_description.html metodo=_dato parametro="long previous" %}
* **long amount**,  {% include w3api/param_description.html metodo=_dato parametro="long amount" %}
* **ResourceId id**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceId id" %}

## Clase Padre
[ThrottledMeter](/Java/ThrottledMeter/)

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
