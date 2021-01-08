---
title: ResourceApprover.request()
permalink: Java/ResourceApprover/request
date: 2021-01-04
key: JavaJava.R.ResourceApprover
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
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
* **ResourceMeter meter**,  {% include w3api/param_description.html metodo=_data parametro="ResourceMeter meter" %}
* **long previous**,  {% include w3api/param_description.html metodo=_data parametro="long previous" %}
* **long amount**,  {% include w3api/param_description.html metodo=_data parametro="long amount" %}
* **ResourceId id**,  {% include w3api/param_description.html metodo=_data parametro="ResourceId id" %}

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
{%- for _ldc in site.data.Java.R.ResourceApprover.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
