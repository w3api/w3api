---
title: ThrottledMeter.create()
permalink: Java/ThrottledMeter/create
date: 2021-01-04
key: JavaJava.T.ThrottledMeter
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThrottledMeter.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ThrottledMeter create(ResourceType type, long ratePerSec, ResourceApprover approver)
public static ThrottledMeter create(ResourceType type, long ratePerSec, ResourceRequest parent, ResourceApprover approver)
public static ThrottledMeter create(ResourceType type, ResourceRequest parent, ResourceApprover approver)
~~~

## Parámetros
* **ResourceRequest parent**,  {% include w3api/param_description.html metodo=_data parametro="ResourceRequest parent" %}
* **ResourceType type**,  {% include w3api/param_description.html metodo=_data parametro="ResourceType type" %}
* **ResourceApprover approver**,  {% include w3api/param_description.html metodo=_data parametro="ResourceApprover approver" %}
* **long ratePerSec**,  {% include w3api/param_description.html metodo=_data parametro="long ratePerSec" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ThrottledMeter](/Java/ThrottledMeter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThrottledMeter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
