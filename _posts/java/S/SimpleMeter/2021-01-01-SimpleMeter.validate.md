---
title: SimpleMeter.validate()
permalink: /Java/SimpleMeter/validate/
date: 2021-01-11
key: Java.S.SimpleMeter
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleMeter.metodos valor="validate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected long validate(long previous, long amount, ResourceId id) throws ResourceRequestDeniedException
~~~

## Parámetros
* **long previous**,  {% include w3api/param_description.html metodo=_dato parametro="long previous" %}
* **long amount**,  {% include w3api/param_description.html metodo=_dato parametro="long amount" %}
* **ResourceId id**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceId id" %}

## Excepciones
[ResourceRequestDeniedException](/Java/ResourceRequestDeniedException/)

## Clase Padre
[SimpleMeter](/Java/SimpleMeter/)

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
