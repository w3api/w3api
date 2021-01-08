---
title: NotifyingMeter.create()
permalink: Java/NotifyingMeter/create
date: 2021-01-04
key: JavaJava.N.NotifyingMeter
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NotifyingMeter.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static NotifyingMeter create(ResourceType type, ResourceApprover approver)
public static NotifyingMeter create(ResourceType type, ResourceRequest parent, ResourceApprover approver)
~~~

## Parámetros
* **ResourceRequest parent**,  {% include w3api/param_description.html metodo=_data parametro="ResourceRequest parent" %}
* **ResourceType type**,  {% include w3api/param_description.html metodo=_data parametro="ResourceType type" %}
* **ResourceApprover approver**,  {% include w3api/param_description.html metodo=_data parametro="ResourceApprover approver" %}

## Clase Padre
[NotifyingMeter](/Java/NotifyingMeter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NotifyingMeter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
