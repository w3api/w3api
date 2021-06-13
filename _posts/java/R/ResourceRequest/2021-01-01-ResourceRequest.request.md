---
title: ResourceRequest.request()
permalink: /Java/ResourceRequest/request/
date: 2021-01-11
key: Java.R.ResourceRequest
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceRequest.metodos valor="request" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long request(long amount, ResourceId id)
~~~

## Parámetros
* **long amount**,  {% include w3api/param_description.html metodo=_dato parametro="long amount" %}
* **ResourceId id**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceId id" %}

## Excepciones
[ResourceRequestDeniedException](/Java/ResourceRequestDeniedException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[ResourceRequest](/Java/ResourceRequest/)

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
