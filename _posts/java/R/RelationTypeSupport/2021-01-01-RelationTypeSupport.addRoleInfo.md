---
title: RelationTypeSupport.addRoleInfo()
permalink: Java/RelationTypeSupport/addRoleInfo
date: 2021-01-11
key: Java.R.RelationTypeSupport
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationTypeSupport.metodos valor="addRoleInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void addRoleInfo(RoleInfo roleInfo) throws IllegalArgumentException, InvalidRelationTypeException
~~~

## Parámetros
* **RoleInfo roleInfo**,  {% include w3api/param_description.html metodo=_dato parametro="RoleInfo roleInfo" %}

## Excepciones
[InvalidRelationTypeException](/Java/InvalidRelationTypeException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationTypeSupport](/Java/RelationTypeSupport/)

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
