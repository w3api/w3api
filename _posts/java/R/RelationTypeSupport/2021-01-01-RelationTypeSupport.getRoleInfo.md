---
title: RelationTypeSupport.getRoleInfo()
permalink: /Java/RelationTypeSupport/getRoleInfo/
date: 2021-01-11
key: Java.R.RelationTypeSupport
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationTypeSupport.metodos valor="getRoleInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RoleInfo getRoleInfo(String roleInfoName) throws IllegalArgumentException, RoleInfoNotFoundException
~~~

## Parámetros
* **String roleInfoName**,  {% include w3api/param_description.html metodo=_dato parametro="String roleInfoName" %}

## Excepciones
[RoleInfoNotFoundException](/Java/RoleInfoNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
