---
title: DelegationPermission.DelegationPermission()
permalink: Java/DelegationPermission/DelegationPermission
date: 2021-01-11
key: JavaJava.D.DelegationPermission
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DelegationPermission.constructores valor="DelegationPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DelegationPermission(String principals)
public DelegationPermission(String principals, String actions)
~~~

## Parámetros
* **String principals**,  {% include w3api/param_description.html metodo=_dato parametro="String principals" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DelegationPermission](/Java/DelegationPermission/)

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
