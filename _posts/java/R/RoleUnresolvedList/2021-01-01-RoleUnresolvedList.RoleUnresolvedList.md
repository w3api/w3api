---
title: RoleUnresolvedList.RoleUnresolvedList()
permalink: Java/RoleUnresolvedList/RoleUnresolvedList
date: 2021-01-11
key: Java.R.RoleUnresolvedList
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RoleUnresolvedList.constructores valor="RoleUnresolvedList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RoleUnresolvedList()
public RoleUnresolvedList(int initialCapacity)
public RoleUnresolvedList(List<RoleUnresolved> list) throws IllegalArgumentException
~~~

## Parámetros
* **List&lt;RoleUnresolved&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<RoleUnresolved> list" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RoleUnresolvedList](/Java/RoleUnresolvedList/)

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
