---
title: RoleUnresolvedList.add()
permalink: Java/RoleUnresolvedList/add
date: 2021-01-11
key: Java.R.RoleUnresolvedList
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RoleUnresolvedList.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void add(int index, RoleUnresolved role) throws IllegalArgumentException, IndexOutOfBoundsException
public void add(RoleUnresolved role) throws IllegalArgumentException
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **RoleUnresolved role**,  {% include w3api/param_description.html metodo=_dato parametro="RoleUnresolved role" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
