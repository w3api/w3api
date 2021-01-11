---
title: SubjectDelegationPermission.SubjectDelegationPermission()
permalink: Java/SubjectDelegationPermission/SubjectDelegationPermission
date: 2021-01-11
key: JavaJava.S.SubjectDelegationPermission
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubjectDelegationPermission.constructores valor="SubjectDelegationPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SubjectDelegationPermission(String name)
public SubjectDelegationPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SubjectDelegationPermission](/Java/SubjectDelegationPermission/)

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
