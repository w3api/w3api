---
title: RelationSupport.getRole()
permalink: Java/RelationSupport/getRole
date: 2021-01-11
key: JavaJava.R.RelationSupport
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationSupport.metodos valor="getRole" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public List<ObjectName> getRole(String roleName) throws IllegalArgumentException, RoleNotFoundException, RelationServiceNotRegisteredException
~~~

## Parámetros
* **String roleName**,  {% include w3api/param_description.html metodo=_dato parametro="String roleName" %}

## Excepciones
[RoleNotFoundException](/Java/RoleNotFoundException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationSupport](/Java/RelationSupport/)

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
