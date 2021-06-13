---
title: BoundedMeter.BoundedMeter()
permalink: /Java/BoundedMeter/BoundedMeter/
date: 2021-01-11
key: JavaJava.B.BoundedMeter
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BoundedMeter.constructores valor="BoundedMeter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected BoundedMeter(ResourceType type, long bound, ResourceRequest parent, ResourceApprover approver)
~~~

## Parámetros
* **ResourceApprover approver**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceApprover approver" %}
* **ResourceRequest parent**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceRequest parent" %}
* **ResourceType type**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceType type" %}
* **long bound**,  {% include w3api/param_description.html metodo=_dato parametro="long bound" %}

## Clase Padre
[BoundedMeter](/Java/BoundedMeter/)

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
