---
title: ResourceRequest.request()
permalink: Java/ResourceRequest/request
date: 2021-01-04
key: JavaJava.R.ResourceRequest
category: java
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
* **long amount**,  {% include w3api/param_description.html metodo=_data parametro="long amount" %}
* **ResourceId id**,  {% include w3api/param_description.html metodo=_data parametro="ResourceId id" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [ResourceRequestDeniedException](/Java/ResourceRequestDeniedException/)

## Clase Padre
[ResourceRequest](/Java/ResourceRequest/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
