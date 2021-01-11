---
title: NotifyingMeter.validate()
permalink: Java/NotifyingMeter/validate
date: 2021-01-11
key: JavaJava.N.NotifyingMeter
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NotifyingMeter.metodos valor="validate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected long validate(long previous, long amount, ResourceId id)
~~~

## Parámetros
* **long previous**,  {% include w3api/param_description.html metodo=_dato parametro="long previous" %}
* **long amount**,  {% include w3api/param_description.html metodo=_dato parametro="long amount" %}
* **ResourceId id**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceId id" %}

## Clase Padre
[NotifyingMeter](/Java/NotifyingMeter/)

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
