---
title: RelationService.sendRelationCreationNotification()
permalink: Java/RelationService/sendRelationCreationNotification
date: 2021-01-11
key: Java.R.RelationService
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="sendRelationCreationNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void sendRelationCreationNotification(String relationId) throws IllegalArgumentException, RelationNotFoundException
~~~

## Parámetros
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/)

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
