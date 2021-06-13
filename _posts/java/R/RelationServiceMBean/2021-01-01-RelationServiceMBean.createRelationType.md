---
title: RelationServiceMBean.createRelationType()
permalink: Java/RelationServiceMBean/createRelationType
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="createRelationType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void createRelationType(String relationTypeName, RoleInfo[] roleInfoArray) throws IllegalArgumentException, InvalidRelationTypeException
~~~

## Parámetros
* **RoleInfo[] roleInfoArray**,  {% include w3api/param_description.html metodo=_dato parametro="RoleInfo[] roleInfoArray" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relationTypeName" %}

## Excepciones
[InvalidRelationTypeException](/Java/InvalidRelationTypeException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
