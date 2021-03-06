---
title: ResourceApprover.request()
permalink: /Java/ResourceApprover/request/
date: 2021-01-11
key: Java.R.ResourceApprover
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceApprover.metodos valor="request" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long request(ResourceMeter meter, long previous, long amount, ResourceId id)
~~~

## Parámetros
* **long previous**,  {% include w3api/param_description.html metodo=_dato parametro="long previous" %}
* **long amount**,  {% include w3api/param_description.html metodo=_dato parametro="long amount" %}
* **ResourceMeter meter**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceMeter meter" %}
* **ResourceId id**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceId id" %}

## Excepciones
[ResourceRequestDeniedException](/Java/ResourceRequestDeniedException/)

## Clase Padre
[ResourceApprover](/Java/ResourceApprover/)

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
