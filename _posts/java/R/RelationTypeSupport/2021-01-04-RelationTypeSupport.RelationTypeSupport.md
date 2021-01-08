---
title: RelationTypeSupport.RelationTypeSupport()
permalink: Java/RelationTypeSupport/RelationTypeSupport
date: 2021-01-04
key: JavaJava.R.RelationTypeSupport
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationTypeSupport.constructores valor="RelationTypeSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected RelationTypeSupport(String relationTypeName)
public RelationTypeSupport(String relationTypeName, RoleInfo[] roleInfoArray) throws IllegalArgumentException, InvalidRelationTypeException
~~~

## Parámetros
* **RoleInfo[] roleInfoArray**,  {% include w3api/param_description.html metodo=_data parametro="RoleInfo[] roleInfoArray" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_data parametro="String relationTypeName" %}

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
{%- for _ldc in site.data.Java.R.RelationTypeSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
