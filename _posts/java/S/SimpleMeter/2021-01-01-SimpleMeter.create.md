---
title: SimpleMeter.create()
permalink: Java/SimpleMeter/create
date: 2021-01-11
key: JavaJava.S.SimpleMeter
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleMeter.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SimpleMeter create(ResourceType type)
public static SimpleMeter create(ResourceType type, ResourceRequest parent)
~~~

## Parámetros
* **ResourceRequest parent**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceRequest parent" %}
* **ResourceType type**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceType type" %}

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
