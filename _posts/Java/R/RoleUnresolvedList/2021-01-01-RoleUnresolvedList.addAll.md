---
title: RoleUnresolvedList.addAll()
permalink: /Java/RoleUnresolvedList/addAll/
date: 2021-01-11
key: Java.R.RoleUnresolvedList
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RoleUnresolvedList.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean addAll(int index, RoleUnresolvedList roleList) throws IllegalArgumentException, IndexOutOfBoundsException
public boolean addAll(RoleUnresolvedList roleList) throws IndexOutOfBoundsException
~~~

## Parámetros
* **RoleUnresolvedList roleList**,  {% include w3api/param_description.html metodo=_dato parametro="RoleUnresolvedList roleList" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

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
