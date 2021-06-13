---
title: RelationServiceMBean.getRoleCardinality()
permalink: Java/RelationServiceMBean/getRoleCardinality
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="getRoleCardinality" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Integer getRoleCardinality(String relationId, String roleName) throws IllegalArgumentException, RelationNotFoundException, RoleNotFoundException
~~~

## Parámetros
* **String roleName**,  {% include w3api/param_description.html metodo=_dato parametro="String roleName" %}
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}

## Excepciones
[RoleNotFoundException](/Java/RoleNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/)

## Clase Padre
[RelationServiceMBean](/Java/RelationServiceMBean/)

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
