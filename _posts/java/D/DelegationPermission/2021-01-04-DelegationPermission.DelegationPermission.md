---
title: DelegationPermission.DelegationPermission()
permalink: Java/DelegationPermission/DelegationPermission
date: 2021-01-04
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
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}
* **String principals**,  {% include w3api/param_description.html metodo=_data parametro="String principals" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DelegationPermission](/Java/DelegationPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DelegationPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
