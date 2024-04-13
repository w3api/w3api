---
title: RelationService.addRelationType()
permalink: /Java/RelationService/addRelationType/
date: 2021-01-11
key: Java.R.RelationService
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="addRelationType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addRelationType(RelationType relationTypeObj) throws IllegalArgumentException, InvalidRelationTypeException
~~~

## Parámetros
* **RelationType relationTypeObj**,  {% include w3api/param_description.html metodo=_dato parametro="RelationType relationTypeObj" %}

## Excepciones
[InvalidRelationTypeException](/Java/InvalidRelationTypeException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationService](/Java/RelationService/)

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
