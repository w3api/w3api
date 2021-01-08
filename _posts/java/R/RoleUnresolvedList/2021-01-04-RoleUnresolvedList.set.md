---
title: RoleUnresolvedList.set()
permalink: Java/RoleUnresolvedList/set
date: 2021-01-04
key: JavaJava.R.RoleUnresolvedList
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RoleUnresolvedList.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void set(int index, RoleUnresolved role) throws IllegalArgumentException, IndexOutOfBoundsException
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **RoleUnresolved role**,  {% include w3api/param_description.html metodo=_data parametro="RoleUnresolved role" %}

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
{%- for _ldc in site.data.Java.R.RoleUnresolvedList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
